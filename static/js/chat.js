const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/");

chatSocket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><b>${data.sender}:</b> ${data.message}</p>`;
};

function sendMessage() {
    const messageInput = document.getElementById("message-input");
    const message = messageInput.value;
    chatSocket.send(JSON.stringify({ message: message, sender: "User1" }));
    messageInput.value = "";
}
