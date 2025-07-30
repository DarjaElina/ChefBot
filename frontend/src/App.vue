<template>
  <div
    class="flex flex-col items-center justify-center min-h-screen bg-lime-50 dark:bg-gray-900 p-6 transition-colors duration-300"
  >
    <div
      class="bg-white dark:bg-gray-800 rounded-2xl shadow-md p-6 w-full max-w-md space-y-4"
    >
      <button
        @click="toggleDarkMode"
        class="mb-4 px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 rounded-md hover:bg-gray-300 dark:hover:bg-gray-600 transition"
      >
        {{ isDark ? "Dark Mode" : "Light Mode" }}
      </button>

      <input
        v-model="message"
        placeholder="Type your message"
        class="w-full px-4 py-2 border border-lime-300 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-lime-400 dark:bg-gray-700 dark:text-white"
      />
      <button
        @click="sendMessage"
        class="w-full bg-lime-500 text-white py-2 rounded-xl hover:bg-lime-600 transition duration-200 dark:bg-lime-600 dark:hover:bg-lime-700"
      >
        Send
      </button>
      <p class="text-gray-700 dark:text-gray-100">
        <span class="font-semibold">Reply:</span> {{ reply }}
      </p>
      <p v-if="error" class="text-rose-600 dark:text-rose-300">{{ error }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import axios, { AxiosError } from "axios";

export default {
  data() {
    return {
      message: "",
      reply: "",
      error: "",
      isDark: document.documentElement.classList.contains("dark"),
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
        // Added a type check for ESLint
        if (error instanceof AxiosError) {
          this.error = `Oh ribbity! ${error.message || "Try again please!"}`;
        }
        console.error(error);
      }
    },
    toggleDarkMode() {
      this.isDark = !this.isDark;
      if (this.isDark) {
        document.documentElement.classList.add("dark");
        localStorage.theme = "dark";
      } else {
        document.documentElement.classList.remove("dark");
        localStorage.theme = "light";
      }
    },
  },
};
</script>
