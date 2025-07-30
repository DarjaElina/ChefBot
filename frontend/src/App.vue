<template>
  <div>
    <input v-model="message" placeholder="Type your message" />
    <button @click="sendMessage">Send</button>
    <p>Reply: {{ reply }}</p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      message: "",
      reply: "",
      error: "",
    };
  },
  methods: {
    async sendMessage() {
      try {
        this.error = "";
        const res = await axios.post("http://127.0.0.1:8000/sendMessage", {
          text: this.message,
        });
        this.reply = res.data.reply;
      } catch (error) {
        this.error = `Oh ribbity! ${error.message || "Try again please!"}`;
        console.error(error);
      }
    },
  },
};
</script>

<!-- Comments
v-model links input to the message variable
button runs sendMessage function when clicked
<p>Reply: {{ reply }}</p> shows reply from server

Show error message while there is one:
<p v-if="error">{{ error }}</p>

error: ''     // Store error message to show on page
this.error = ''  // Clear previous error before sending new request to make sure old errors don’t confuse the user
this.error = error.message || 'Oh ribbity! Something went wrong.' // Show error message on page 
console.error(error) // Log error message to console

this.error = `Oh ribbity! ${error.message || "Try again please!"}`; //Try again runs if error.message doesn't. Default.

methods: {} Function that sends message to backend and gets the reply from sendMessage

export default {  Exports component
  data() {  function that returns data for this component
    return { 
      message: '',  Holds the user message
      reply: ''    Holds the reply from server
    }
  }, 
      
  const res = await axios.post('http://127.0.0.1:8000/sendMessage', 
    text: this.message : Send POST request to backend with the users message text

  this.reply = res.data.reply: Saves the reply from the server to show on the page
}
-->
