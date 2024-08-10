<template>
    <div class="chat-container" :class="{ minimized: isMinimized }">
      <div class="chat-window">
        <div class="chat-header">
          SuperSeek Bot
          <button class="minimize-button" @click="toggleMinimize">
            {{ isMinimized ? '▲' : '▼' }}
          </button>
        </div>
        <div v-if="!isMinimized">
          <div class="prefix-options">
            <button v-for="(prefix, index) in prefixes" :key="index" @click="selectPrefix(prefix)">
              {{ prefix }}
            </button>
          </div>
          <div ref="chatMessages" class="chat-messages">
            <div v-for="(message, index) in messages" :key="index" :class="['chat-message', message.sender]">
              {{ message.text }}
            </div>
          </div>
          <div class="chat-bar">
            <input
              type="text"
              v-model="newMessage"
              @keyup.enter="sendMessage"
              placeholder="Type your message..."
            />
            <button @click="sendMessage">Send</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name:'chatBox',
    data() {
      return {
        newMessage: '',
        messages: [],
        isMinimized: false,
        prefixes: ['A', 'B', 'C', 'D'],
      };
    },
    methods: {
      sendMessage() {
        if (this.newMessage.trim() !== '') {
          this.messages.push({ text: this.newMessage, sender: 'user' });
          this.newMessage = '';
          this.simulateAiResponse();
          this.scrollToBottom();
        }
      },
      simulateAiResponse() {
        setTimeout(() => {
          this.messages.push({ text: 'AI response goes here...', sender: 'ai' });
          this.scrollToBottom();
        }, 1000);
      },
      toggleMinimize() {
        this.isMinimized = !this.isMinimized;
      },
      selectPrefix(prefix) {
        this.messages.push({ text: prefix, sender: 'user' });
        this.simulateAiResponse();
        this.scrollToBottom();
      },
      scrollToBottom() {
        this.$nextTick(() => {
          const chatMessages = this.$refs.chatMessages;
          if (chatMessages) {
            chatMessages.scrollTop = chatMessages.scrollHeight;
          }
        });
      },
    },
  };
  </script>
  
  <style scoped>
  .chat-container {
    position: fixed;
    bottom: 0;
    right: 0;
    width: 300px;
    border: 1px solid #ccc;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: height 0.3s ease;
  }
  
  .chat-container.minimized {
    height: 50px;
    overflow: hidden;
  }
  
  .chat-window {
    display: flex;
    flex-direction: column;
    height: 400px;
  }
  
  .chat-header {
    padding: 10px;
    background-color: #3a4d66;
    color: white;
    text-align: center;
    border-radius: 8px 8px 0 0;
    position: relative;
  }
  
  .minimize-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    color: white;
    font-size: 14px;
    cursor: pointer;
  }
  
  .prefix-options {
    display: flex;
    flex-wrap: wrap;
    padding: 10px;
    gap: 10px;
    background-color: #f9f9f9;
  }
  
  .prefix-options button {
    flex: 1;
    padding: 8px;
    background-color: #3a4d66;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .chat-messages {
    flex: 1;
    padding: 10px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
    height: 250px; /* Set a fixed height to make it scrollable */
  }
  
  .chat-message {
    padding: 8px;
    border-radius: 5px;
    max-width: 70%;
    word-wrap: break-word;
  }
  
  .chat-message.user {
    align-self: flex-end;
    background-color: #007bff;
    color: white;
  }
  
  .chat-message.ai {
    align-self: flex-start;
    background-color: #f1f1f1;
  }
  
  .chat-bar {
    display: flex;
    padding: 10px;
    border-top: 1px solid #ccc;
  }
  
  .chat-bar input {
    flex: 1;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-right: 10px;
  }
  
  .chat-bar button {
    padding: 8px 12px;
    border: none;
    background-color: #3a4d66;
    color: white;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  