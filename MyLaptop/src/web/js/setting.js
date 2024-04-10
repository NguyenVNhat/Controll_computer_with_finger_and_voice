eel.expose(getnewWebsite)
function getnewWebsite(msg){
    eel.getnewWebsite(msg)
}
var button = document.getElementById("button-setting");
button.addEventListener('click', function(){
    var website_name = document.getElementById("website_name").value;
    var url = document.getElementById("url").value;
    getnewWebsite("ADDWEBSITE|||"+website_name+"|||"+url);
});