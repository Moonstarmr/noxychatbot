const responses = {
  "(hi|hello|hey)": "Hello! How can I help you?",
  "(what is your name\\??)": "My name is Noxy. I'm a simple chatbot created by Moonstar.",
  "(how are you\\??)": "I'm doing great, thank you!",
  "(what can you do\\??)": "I can answer some predefined questions.",
  "(do you love me\\??)": "I'm sorry, my developer is very strict about emotions!",
  "(who created you\\??)": "I was created by Moonstar.",
  "(tell me a joke)": "Why did the computer go to therapy? It had too many bytes of emotional baggage!",
  "(bye|goodbye)": "Goodbye! Have a great day!"
};

const chatWindow = document.getElementById("chat-window");
const input = document.getElementById("user-input");

function sendMessage() {
  const userText = input.value.trim();
  if (!userText) return;

  appendMessage("user", userText);
  input.value = "";

  const response = getBotResponse(userText);

  setTimeout(() => {
    appendMessage("bot", response);
  }, 500);
}

function appendMessage(sender, text) {
  const msg = document.createElement("div");
  msg.className = sender;
  msg.textContent = text;
  chatWindow.appendChild(msg);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function getBotResponse(userText) {
  userText = userText.toLowerCase();

  for (let pattern in responses) {
    const regex = new RegExp(pattern, "i");
    if (regex.test(userText)) {
      return responses[pattern];
    }
  }

  return "Sorry, I don't understand that.";
}
