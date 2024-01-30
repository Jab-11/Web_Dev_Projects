let count = 0;

const countLabel = document.getElementById("count");
const incBtn = document.getElementById("incBtn");
const reset = document.getElementById("reset");
const decBtn = document.getElementById("decBtn");

incBtn.onclick = function(){
    count++;
    countLabel.textContent = count;
}
reset.onclick = function(){
    count = 0;
    countLabel.textContent = count;
}
decBtn.onclick = function(){
    count--;
    countLabel.textContent = count;
}
