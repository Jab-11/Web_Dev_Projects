let msg = ["Initializing Hacking", "Reading your Files", "Password files Detected", "Sending all passwords and personal files to server", "Cleaning up"];
let con = document.querySelector(".con");

async function addMsg(m) {
    if (con.innerHTML == "") {
        con.innerHTML = m;
    } else {
        con.innerHTML += "<br>" + m;
    }
}

function randomDelay() {
    return Math.floor(7 * Math.random());
}


async function displayMsg() {
    for (let i = 0; i < msg.length; i++) {
        let intervalId; 
        await new Promise(resolve => {
            let c = con.innerHTML;
            intervalId = setInterval(() => {
                con.innerHTML += ".";
                if (con.innerHTML.endsWith("....")) {
                    resolve(con.innerHTML = c);
                }
            }, 200);
            setTimeout(() => {
                resolve();
            }, randomDelay() * 1000);
        });
        clearInterval(intervalId); 
        await addMsg(msg[i]); 
    }
}

displayMsg();
