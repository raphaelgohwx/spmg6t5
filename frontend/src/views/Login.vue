<template>
    <div>
      <navbar />
      <div class="home-container">
        <h1 class="home-title">Welcome to the Job Application Management Portal</h1>
        <p class="home-description">Your gateway to managing job applications and role listings!</p>
        <p class="home-instruction">Please login using the dropdown list at the top right to access role listings and start managing job applications.</p>
      </div>
    </div>
  </template>
  
  <script>
  import navbar from "@/components/navbar.vue";
  
  export default {
    components: {
      navbar,
    },
  };
  </script>
  
  <style scoped>
  .home-container {
    text-align: center;
    padding: 20px;
  }
  
  .home-title {
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .home-description {
    font-size: 20px;
    margin-bottom: 10px;
    color: #333;
  }
  
  .home-instruction {
    font-size: 18px;
    color: #666;
  }
  </style>
  