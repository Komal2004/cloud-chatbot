async function sendMessage() {
  const input = document.getElementById("user-input");
  const msg = input.value.trim();
  if (!msg) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class='user'>You: ${msg}</div>`;
  input.value = "";

  const res = await fetch("/get", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `msg=${encodeURIComponent(msg)}`
  });

  const data = await res.json();
  chatBox.innerHTML += `<div class='bot'>Bot: ${data.reply}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}

