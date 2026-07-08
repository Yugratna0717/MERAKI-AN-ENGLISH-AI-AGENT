// ======================================================
//                      MERAKI
// ======================================================

const sendBtn = document.getElementById("sendBtn");
const userInput = document.getElementById("userInput");
const responseBox = document.getElementById("response");
const agentBox = document.getElementById("agent");



// ======================================================
// SEND MESSAGE
// ======================================================

async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") {

        alert("Please enter a question.");

        return;

    }

    sendBtn.disabled = true;

    sendBtn.innerHTML = "Thinking...";

    responseBox.innerHTML = "MERAKI is thinking...";

    agentBox.innerHTML = "Selecting Agent...";

    try {

        const res = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await res.json();

        if (data.error) {

            responseBox.innerHTML = data.error;

            agentBox.innerHTML = "-";

            return;

        }

        agentBox.innerHTML = data.agent;

        responseBox.innerHTML = marked.parse(data.response);
    }

    catch (error) {

        responseBox.innerHTML = "Something went wrong.";

        agentBox.innerHTML = "-";

        console.error(error);

    }

    finally {

        sendBtn.disabled = false;

        sendBtn.innerHTML = "Ask MERAKI";

    }

}



// ======================================================
// BUTTON CLICK
// ======================================================

sendBtn.addEventListener("click", sendMessage);



// ======================================================
// PRESS ENTER TO SEND
// SHIFT + ENTER FOR NEW LINE
// ======================================================

userInput.addEventListener("keydown", function(event){

    if(event.key === "Enter" && !event.shiftKey){

        event.preventDefault();

        sendMessage();

    }

});



// ======================================================
// AUTO RESIZE TEXTAREA
// ======================================================

userInput.addEventListener("input", function(){

    this.style.height = "auto";

    this.style.height = this.scrollHeight + "px";

});