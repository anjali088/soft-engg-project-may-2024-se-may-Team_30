<template>
  <!-- Header container -->
    <div class="header">
      <!-- Left side of the header contatining the logo and title -->
      <div class="header-left">
        <img src="@/assets/logo.jpg" alt="IIT Madras Logo" class="logo" />
        <span class="title">IIT Madras</span>
      </div>
      <!-- center part of the header with a text span -->
      <div class="header-center">
        <span><b>May 2024 - Software Engineering</b></span>
      </div>
      <!-- Right side of the header containing the email and sign-out icon -->
      <div class="header-right">
        <span><b>21f1111111@ds.study.iitm.ac.in</b></span>
        <i class="fas fa-sign-out-alt"></i>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HeaderBar'
  }
  </script>
  
  <style scoped>
  /* Styles for the header container */
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #F9FAFB;
    padding: 10px 20px;
    color: #465A74;
    border-bottom: 1px solid #E5E7EB;
  }
  
  /* Styles for the left side of the header */
  .header-left {
    display: flex;
    align-items: center;
  }

  /* Styles for the right side of the header */
  .header-right span {
  margin-right: 10px; /* Adjust the value as needed */
  }

  
  /* Styles for the logo image */
  .logo {
    height: 40px;
    margin-right: 10px;
  }
  
  /* Styles for the title text  */
  .title {
    font-weight: bold;
    font-size: 18px;
  }
  
  /* Styles for the center part of the header */
  .header-center {
    flex-grow: 1;
    text-align: center;
    font-size: 16px;
  }
  
  /* Styles for the right side of the header */
  .header-right {
    display: flex;
    align-items: center;
    font-size: 14px;
  }
  
  /* Styles for the sign-out icon */
  .header-right i {
    margin-left: 10px;
    cursor: pointer;
  }
  </style>
  