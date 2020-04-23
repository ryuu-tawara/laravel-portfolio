import scrapy

import re
from datetime import date
from myproject.items import Weather_Item
from bs4 import BeautifulSoup
from urllib.request import urlopen


class WeatherSpider(scrapy.Spider):
    
    custom_settings = {
        
    'FEED_EXPORTERS' : {
        'csv': 'myproject.Exporters.Exporter'
    },

    }
    name = 'Weather'
    start_urls = ['https://tenki.jp/forecast/9/43/',
                  'https://weather.yahoo.co.jp/weather/jp/40/',
                  'https://www.jma.go.jp/jp/yoho/346.html',
                  ]
    def parse(self, response):

        if re.search(r'https://tenki.jp/\w*',response.url):
            for url in response.css('div#forecast-map a::attr("href")').getall(): #リンク
                html = urlopen(response.url)
                bs = BeautifulSoup(html, 'html.parser')
                town = re.search(r'\w+市', bs.find('a', {'href':url}).text).group()
                yield response.follow(url, callback=self.tenki_page, meta={'city':town})

        elif re.search(r'https://weather.yahoo.co.jp/\w*', response.url):
            for url in response.css('div#map ul a::attr("href")').getall(): #リンク
                html = urlopen(response.url)
                bs = BeautifulSoup(html, 'html.parser')
                town = bs.find('a', {'href':url}).dl.dt.text 
                yield response.follow(url, callback=self.yahoo_page, meta={'city':town})

        elif re.search(r'https://www.jma.go.jp/\w*', response.url):
            yield scrapy.Request(response.url, callback=self.kisyou_page)

    def tenki_page(self, response):

        city_item = response.meta.get('city')

        Weather = Weather_Item()
        Weather['time'] = 'Te-' + str(date.today().year)+'年'+response.css('.today-weather h3::text').re(r'0?\d+\w+\d+\w')[0]+'-'+city_item#日付
        Weather['city'] = city_item
        Weather['hight_t'] = response.css('.today-weather .high-temp .value::text').get()#最高気温
        Weather['low_t'] = response.css('.today-weather .low-temp .value::text').get()#最低気温

        zero_six = response.css('.today-weather .rain-probability td:nth-child(2)::text').get()#00-06
        Weather['zero_six'] = str(zero_six)+'%' if zero_six is not None else zero_six #00-06 

        six_twelve = response.css('.today-weather .rain-probability td:nth-child(3)::text').get() #06-12
        Weather['six_twelve'] = str(six_twelve)+'%' if six_twelve is not None else six_twelve #06-12

        twelve_eighteenth = response.css('.today-weather .rain-probability td:nth-child(4)::text').get() #12-18
        Weather['twelve_eighteenth'] = str(twelve_eighteenth)+'%' if twelve_eighteenth is not None else twelve_eighteenth #12-18

        eighteenth_zero = response.css('.today-weather .rain-probability td:nth-child(5)::text').get()#18-24
        Weather['eighteenth_zero'] = str(eighteenth_zero) + '%' if eighteenth_zero is not None else eighteenth_zero#18-24
        yield Weather

        Weather['time'] = 'Te-' + str(date.today().year)+ '年' + response.css('.tomorrow-weather h3::text').re(r'0?\d+\w+\d+\w')[0]+'-'+city_item#日付 
        Weather['city'] = city_item
        Weather['hight_t'] = response.css('.tomorrow-weather .high-temp .value::text').get()#最高気温
        Weather['low_t'] = response.css('.tomorrow-weather .low-temp .value::text').get()#最低気温

        zero_six = response.css('.tomorrow-weather .rain-probability td:nth-child(2)::text').get()#00-06
        Weather['zero_six'] = str(zero_six)+'%' if zero_six is not None else zero_six #00-06 

        six_twelve = response.css('.tomorrow-weather .rain-probability td:nth-child(3)::text').get() #06-12
        Weather['six_twelve'] = str(six_twelve)+'%' if six_twelve is not None else six_twelve #06-12

        twelve_eighteenth = response.css('.tomorrow-weather .rain-probability td:nth-child(4)::text').get() #12-18
        Weather['twelve_eighteenth'] = str(twelve_eighteenth)+'%' if twelve_eighteenth is not None else twelve_eighteenth #12-18

        eighteenth_zero = response.css('.tomorrow-weather .rain-probability td:nth-child(5)::text').get()#18-24
        Weather['eighteenth_zero'] = str(eighteenth_zero) + '%' if eighteenth_zero is not None else eighteenth_zero#18-24
        yield Weather
    
    def yahoo_page(self, response):

        city_item = response.meta.get('city')

        Weather = Weather_Item()
        times = ['Ya-' +str(date.today().year)+'年0'+_[:-3]for _ in response.css('div.forecastCity > table tr > td > div > p.date::text').getall()]  #日付 
        hight_ts = response.css('div.forecastCity > table tr > td > div > ul.temp > li.high > em::text').getall() #最高気温 
        low_ts = response.css('div.forecastCity > table tr > td > div > ul.temp > li.low > em::text').getall() #最低気温
        zero_sixes = response.css('div.forecastCity > table tr > td > div > table tr.precip > td:nth-child(2)::text').getall() #00-06
        six_twelves = response.css('div.forecastCity > table tr > td > div > table tr.precip > td:nth-child(3)::text').getall() #06-12
        twelve_eighteenths = response.css('div.forecastCity > table tr > td > div > table tr.precip > td:nth-child(4)::text').getall() #12-18
        eighteenth_zero = response.css('div.forecastCity > table tr > td > div > table tr.precip > td:nth-child(5)::text').getall() #18-24
        Weather['time'] = times[0]+'-'+city_item+'市'
        Weather['city'] = city_item+'市'
        Weather['hight_t'] = hight_ts[0]
        Weather['low_t'] = low_ts[0]
        Weather['zero_six'] = zero_sixes[0]
        Weather['six_twelve'] = six_twelves[0]
        Weather['twelve_eighteenth'] = twelve_eighteenths[0]
        Weather['eighteenth_zero'] = eighteenth_zero[0]
        yield Weather
        Weather['time'] = times[1]+'-'+city_item+'市'
        Weather['city'] = city_item+'市'
        Weather['hight_t'] = hight_ts[1]
        Weather['low_t'] = low_ts[1]
        Weather['zero_six'] = zero_sixes[1]
        Weather['six_twelve'] = six_twelves[1]
        Weather['twelve_eighteenth'] = twelve_eighteenths[1]
        Weather['eighteenth_zero'] = eighteenth_zero[1]
        yield Weather
    
    def kisyou_page(self, response):
        Weather = Weather_Item()

        cities = response.css('div table#forecasttablefont div::text').getall() #~市をリスト取得
        y_m_ds = [str(date.today().year)+'年0'+str(date.today().month)+'月'+re.search(r'\d+\w', _).group()  for _ in response.css('div table#forecasttablefont th.weather::text').getall() if len(_) > 3]
        
        for _ in range(4):
            del y_m_ds[_*2+2]

        num = 1
        c_num = 0

        for y_m_d in y_m_ds:
            if(num <= 2):
                c_num = 0
            elif (2 < num and num <= 4):
                c_num = 1
            elif (4 < num and num <= 6):
                c_num = 2
            elif (6 < num and num <= 8):
                c_num = 3
            try:
                min_t = response.css('div > table#forecasttablefont tr:nth-child('+ str(4*(c_num+1)-(num%2)) +') td.temp > div > table.temp  tr:nth-child(2) > td.min::text').get()
                min_t = re.search(r'\d+', min_t).group()
            except:
                min_t = "--"
            try:
                max_t = response.css('div > table#forecasttablefont tr:nth-child('+ str(4*(c_num+1)-(num%2)) +') td.temp > div > table.temp  tr:nth-child(2) > td.max::text').get()
                max_t = re.search(r'\d+', max_t).group()
            except:
                max_t = "--"
            Weather['time'] = 'Ki-'+ y_m_d + '-' + cities[c_num]
            Weather['city'] = cities[c_num]
            Weather['hight_t'] = max_t
            Weather['low_t'] = min_t
            Weather['zero_six'] = response.css('div > table#forecasttablefont tr:nth-child('+ str(4*(c_num+1)-(num%2)) +') table.rain tr:nth-child(1) td:nth-child(2)::text').get() #00-06
            Weather['six_twelve'] = response.css('div > table#forecasttablefont tr:nth-child('+ str(4*(c_num+1)-(num%2)) +') table.rain tr:nth-child(2) td:nth-child(2)::text').get() #06-12
            Weather['twelve_eighteenth'] = response.css('div > table#forecasttablefont tr:nth-child('+ str(4*(c_num+1)-(num%2)) +') table.rain tr:nth-child(3) td:nth-child(2)::text').get() #12-18
            Weather['eighteenth_zero'] = response.css('div > table#forecasttablefont tr:nth-child('+ str(4*(c_num+1)-(num%2)) +') table.rain tr:nth-child(4) td:nth-child(2)::text').get() #18-24
            yield Weather
            num += 1





    
        
