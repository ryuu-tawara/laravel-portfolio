window.onload = function(){

    var startBtn = document.getElementById('start');
    var timer = document.getElementById('count_time');
    var sound = document.getElementById("sound");

    var second = 0;
    var minute = 25;
    var pomo = 0;
    var rest = 0;
    var cout = 0;

    function hoge(){
        second -= 1;

        if(second < 0 ){
            second = 59;
            minute -= 1;
        }
        else if(pomo != 0 && pomo == 8 && rest == 0){
            minute = 30;
            second = 0; 
            rest = 1;
            sound.load();
        }
        else if(rest == 1 && minute == 0 && second == 0){
            sound.play();
            alert('30分が経過しました！');
            minute = 25;
            second = 0;
            rest = 0;
            pomo = 0;
            cout += 1;
            sound.load();
        }
        else if(minute == 0 && second == 0 && pomo % 2 == 1 && pomo != 8){
            sound.play();
            alert('5分が経過しました！');
            second = 0;
            minute = 25;
            pomo += 1;
            sound.load();
        }
        else if(minute == 0 && second == 0 && pomo != 8 ){
            sound.play();
            alert('25分が経過しました！');
            pomo += 1;
            minute = 5;
            second = 0;
            sound.load();
        }
        timer.innerHTML = minute + '分' + second +'秒' + cout +'回目';
    };

    startBtn.onclick = function(){
        setInterval(hoge, 1000);
        sound.load();
    }
    
    timer.innerHTML = minute + '分' + second +'秒' + cout +'回目';
    
};