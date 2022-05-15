const display = document.getElementById('display')
document.getElementById('buttons').addEventListener('click', ({target}) => {
  console.log(target.innerText)
  display.innerHTML = target.innerText;
})