<template>
    <div class="header">
      <div class="header-left">
        <img src="@/assets/logo.jpg" alt="IIT Madras Logo" class="logo" />
        <span class="title">IIT Madras</span>
      </div>
      <div class="header-center">
        <span>May 2024 - Software Engineering</span>
      </div>
      <div class="header-right">
        <span>21f1002317@ds.study.iitm.ac.in</span>
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
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #F9FAFB;
    padding: 10px 20px;
    color: #465A74;
    border-bottom: 1px solid #E5E7EB;
  }
  
  .header-left {
    display: flex;
    align-items: center;
  }
  
  .logo {
    height: 40px;
    margin-right: 10px;
  }
  
  .title {
    font-weight: bold;
    font-size: 18px;
  }
  
  .header-center {
    flex-grow: 1;
    text-align: center;
    font-size: 16px;
  }
  
  .header-right {
    display: flex;
    align-items: center;
    font-size: 14px;
  }
  
  .header-right i {
    margin-left: 10px;
    cursor: pointer;
  }
  </style>
  