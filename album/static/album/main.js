
const copyBtn = [...document.getElementsByClassName("btn")]
console.log(copyBtn)

copyBtn.forEach(btn => btn.addEventListener('click', ()=>{
const imageUrl = document.getElementById("img").src
navigator.clipboard.writeText(imageUrl)
btn.textContent = "copied"
}))