window.onload = function(){

var msec = (new Date()).getTime();
new Ajax.Request("weather.csv", {
method: "get",
parameters: "cache="+msec,
//アクセスに成功したら
onSuccess:function(httpObj){

// URLのパラメータを取得
var urlParam = location.search.substring(1);
 
// URLにパラメータが存在する場合
if(urlParam) {
  // 「&」が含まれている場合は「&」で分割
  var param = urlParam.split('&');
  // パラメータを格納する用の配列を用意
  var paramArray = [];
    // 用意した配列にパラメータを格納
  for (var i = 0; i < param.length; i++) {
    var paramItem = param[i].split('=');
    paramArray[paramItem[0]] = decodeURI(paramItem[1]);
  }
}
//cssのtextの取得
var text = httpObj.responseText;//全てのtextの取得
var LF = String.fromCharCode(10);//改行の取得
var tabText = text.split(LF);//tabTextは一行ごとのリスト
var tbl = "<table border='1'>";//代入する文字

for (var i=0; i<tabText.length; i++){
    var cText = tabText[i].split(",");//一行をコンマで分ける
    tbl += "<tr>";
    //urlパラメータがあるか
    if(urlParam) {

        for (var j=0; j<cText.length; j++){
            //urlパラメータに対応する要素のみ挿入する
            if(i == 0){
                tbl += "<td>"+cText[j]+"</td>";
            }
            else　if(paramArray["City"].search(cText[1]) != -1){
                tbl += "<td>"+cText[j]+"</td>";//ここで値が挿入される
            }
            else{
                break;
            }
        }
        
    }
    else{

        for (var j=0; j<cText.length; j++){
                tbl += "<td>"+cText[j]+"</td>";//ここで値が挿入される
            }

    }
    tbl +="</tr>";
    //要素が無い時に削除する
    if(tbl.slice(-9) == "<tr></tr>"){
        tbl = tbl.slice(0, -9);
    }
    
}

tbl += "</table>";

$("tableData").innerHTML = tbl;

},
//アクセスに失敗したら
onFailure:function(httpObj){
$("tableData").innerHTML = "エラーで読み込めませんでした";
}
});
}