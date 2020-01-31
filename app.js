
require('./bootstrap');

window.Vue = require('vue');

var app = new Vue({
  el: '#app',
  data: {
    name: 'ryuunosuke tawara',
    univ: 'Hukuoka kougyou',
    major: 'Electronic information',
    restSec: 80,
    timer: null,
    OK1: false,
    OK2: false,
    OK3: false,
    OK4: false,
    OK5: false,
    overColor1: 'white',
    overColor2: 'white',
  },
  methods:{
      call:function(){
      this.timer = setInterval(()=> {this.restSec-=5},1000);
      },
      link:function(path){
        location.href = path;
      },
      changeRed:function(num){
      if(num==1)
      {
        if(this.overColor1 == 'white')
        {
          this.overColor1 = 'red';
        }
        else
        {
          this.overColor1 = 'white'; 
        }
      }
      else{
        if(this.overColor2 == 'white')
        {
          this.overColor2 = 'red';
        }
        else
        {
          this.overColor2 = 'white'; 
        }
      }
        
      },
      sw: function(num){
        if(num==4)
        {
        if(this.OK4 == false)
        {
          this.OK4 = true;
        }
        else{
          this.OK4 = false;
        }
      }
      },
    },
  watch:{
    restSec: function(){
      if(this.restSec <= 60){
        this.OK1 = true;
      }
      if(this.restSec <=30){
        this.OK2 = true;
      }
      if(this.restSec <= 0){
        this.OK3 = true;
      }
      if(this.restSec <= -60){
        this.OK5 = true;
      }
        clearInterval(this.timer)
      }
    }
});

