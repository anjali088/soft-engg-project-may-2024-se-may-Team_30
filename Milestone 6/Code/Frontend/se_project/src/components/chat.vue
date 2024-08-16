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
          <button @click="handleSummaryClick">Summary</button>
          <button @click="handleBClick">B</button>
          <button @click="handleCClick">C</button>
          <button @click="handleDClick">D</button>
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
import axios from 'axios';
export default {
  name: 'chatBox',
  props: {
    lectureId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      newMessage: '',
      messages: [],
      isMinimized: false,
      prefixes: ['Summary', 'B', 'C', 'D'],
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
    response(res){
      setTimeout(() => {
        console.log(res);
        this.messages.push({text: res, sender: 'ai'});
        this.scrollToBottom();
      }, 10);
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
    handleSummaryClick() {
      this.messages.push({ text: 'Summary', sender: 'user' });
      console.log("lecture ID",localStorage.getItem('lec_id'));
      const lecId = localStorage.getItem('lec_id');
      const path = `http://127.0.0.1:5000/get_summary/${lecId}`;
      axios.get(path)
        .then((res)=>{
          this.response(res.data.summary);
        })
        .catch((error)=>{
          console.log("Error fetching summary:", error);
        })
      // this.simulateAiResponse();
      this.scrollToBottom();
    },
    handleBClick() {
      this.messages.push({ text: 'B', sender: 'user' });
      this.simulateAiResponse();
      this.scrollToBottom();
    },
    handleCClick() {
      this.messages.push({ text: 'C', sender: 'user' });
      this.simulateAiResponse();
      this.scrollToBottom();
    },
    handleDClick() {
      this.messages.push({ text: 'D', sender: 'user' });
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
    width: 600px;
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
  