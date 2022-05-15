const timeH = document.querySelector('h1');
let timeSecond = 30;

timeH.innerHTML = '00:${timeSecond}';
const countDown = setInterval(()=>{
    timeSecond--;
    displayTime(timeSecond);

    if (timeSecond <= 0 || timeSecond<1){
        clearInterval(countDown);
    }
},1000)

function displayTime(second){
    const sec = Math.floor(second % 60);
    timeH.innerHTML= '00:${sec<10? 0; } ${sec}'
}