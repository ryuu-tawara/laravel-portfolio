from scrapy.exporters import CsvItemExporter
import re

class Exporter(CsvItemExporter):
    def __init__(self, file, include_headers_line=True, join_multivalued=',', **kwargs):
        super().__init__(file, include_headers_line, join_multivalued)

    def start_exporting(self):
        self.items = []

    def export_item(self, item):
        self.items.append(dict(item))

    def finish_exporting(self):
        # ここでself.itemsをソートする
        self.items.sort(key=lambda x: x["city"])

        if self.include_headers_line:
            values = [x for x in self.items[0]]
            self.csv_writer.writerow(values)

        for item in self.items:
            values = [item[x] for x in item]
            self.csv_writer.writerow(values)
        

          