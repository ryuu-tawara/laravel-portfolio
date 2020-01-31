<!DOCTYPE html>
<html>
<head>

<title>Vue app</title>

<meta charset="UTF-8">
<meta name="csrf-token" content="{{ csrf_token() }}">
<link rel="stylesheet" href="{{ asset('css/portfolio.css') }}"></link>

</head>

<body>


<div id="app">

<div class="top">

<img src="fonts/yukiyama.jpg">

<p style="margin-left: 30px">Name:</p>
<transition :src="call()" name="one">
<p v-if="OK1" style="margin-left: 110px">@{{name}}</p>
</transition>

<p style="margin-left: 30px; margin-top: 80px">University:</p>
<transition :src="call()"name="one">
<p @click="link('https://www.fit.ac.jp/')"
@mouseover="changeRed(1)"
@mouseout="changeRed(1)"
:style="{color: overColor1}" 
v-if="OK2"
style="margin-left: 160px; margin-top: 80px">@{{univ}}</p>
</transition>

<p style="margin-left: 30px; margin-top: 130px">Major in:</p>
<transition :src="call()"name="one">
<p @click="link('https://www.fit.ac.jp/gakubu/kougaku/denshi')"
@mouseover="changeRed(2)"
@mouseout="changeRed(2)"
:style="{color: overColor2}" 
v-if="OK3" 
style="margin-left: 150px; margin-top: 130px">@{{major}}</p>
</transition>

</div>

<div class="title">


<p style="margin-left: 590px; margin-top: 70px;"
@mouseover="sw(4)"
@mouseout="sw(4)"
>Web Programer</p>
<transition name="hello">
<p style="margin-left: 870px; margin-top: 220px;"
v-if="OK4">Hello!!</p>
</transition>
</div>
<div class="contents">
<transition name="skill">

<p v-if="OK5" 
style="margin-left: 300px; margin-top: 380px;">&#x1f4d6; Skill</p>

</transition>
<transition name="skill">
<code v-if="OK5"
 style="margin-left: 300px; margin-top: 430px;">
  python

  pygame

  C++  

  PHP 

  Laravel

  javascript

  Vue.js

</code>
</transition>
</div>





<div class="contents">
<transition name="skill">
<p v-if="OK5" 
style="margin-left: 900px; margin-top: 380px;">&#x1f4d6; Collection</p>
</transition>
<!--
<transition name="skill">
<p v-if="OK5"
style="margin-left: 900px; margin-top: 480px;">
鬼ごっこ
</p>
-->
</transition>
</div>



<script src="{{ asset('/js/app.js') }}"></script>

</body>
</html>
