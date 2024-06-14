
eel.expose(signalVoice);
eel.expose(setUserInput);
eel.expose(setAppInput);
eel.expose(getTextApp);
// eel.expose(setFrame);

// function setFrame(){
//     setFrameCam();
// }
// function setFrameCam() {
//     const url = "http://127.0.0.1:5000/";
//     var element = document.getElementById("cameraDiv");
//     var iframe = document.createElement("iframe");
//     iframe.src = url;
//     iframe.width = "100%";
//     iframe.height = "100%";
//     element.appendChild(iframe);
// }




function signalVoice(msg){
    eel.signalVoice(msg)
}
function getUserinput(msg)
{
    eel.getUserinput(msg)
}
function updateurl(msg)
{
    eel.updateurl(msg)
}
function getTextApp(msg)
{
    eel.getTextApp(msg)
}
function setUserInput(msg) {
    addUserMsg(msg);
}
function setAppInput(msg){
    addAppMsg(msg);
}


function addUserMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message from ready rtol">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    index = element.childElementCount - 1;
    setTimeout(changeClass.bind(null, element, index, "message from"), 500);
}

function addAppMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message to ready ltor">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    index = element.childElementCount - 1;
    setTimeout(changeClass.bind(null, element, index, "message to"), 500);
}

function changeClass(element, index, newClass) {

    element.children[index].className = newClass;
}
function handleInput() {
    var userInput = document.getElementById('userInput');
    var value = userInput.value;
    getTextApp(value);
    addUserMsg(value);
    userInput.value = ""; 
}

var button_enter = document.getElementById('userInputButton');
button_enter.addEventListener('click', handleInput);

var userInput = document.getElementById('userInput');
userInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        handleInput();
        getUserinput(msg);
    }
});

var voiceButton = document.getElementById('voiceButton');
voiceButton.addEventListener('click',function() {
    var userInput = document.getElementById('userInput');
    var button_enter = document.getElementById('userInputButton');
    if ( userInput.style.display == "block"){
        signalVoice("True")
        userInput.style.display = "none";
        button_enter.style.display = "none";
        voiceButton.classList.add('voiceButton');
        
    }
    else{
        signalVoice("False")
        userInput.style.display = "block";
        button_enter.style.display = "block";
        voiceButton.classList.remove('voiceButton');
        
    }
   
})



