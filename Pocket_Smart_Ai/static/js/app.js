async function sendMessage() {
    const messageInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const message = messageInput.value.trim();

    if (!message) return;

    // Display user message
    chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
    messageInput.value = '';

    try {
        const response = await fetch('/chat/send?user_id=1&message=' + encodeURIComponent(message), {
            method: 'POST'
        });
        const data = await response.json();
        chatBox.innerHTML += `<div><strong>AI:</strong> ${data.response}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        console.error('Error:', error);
        chatBox.innerHTML += `<div style="color:red;">Error connecting to AI backend.</div>`;
    }
}