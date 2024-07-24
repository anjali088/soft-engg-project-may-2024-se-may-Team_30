<template>
    <div class="sidebar">
      <div class="sidebar-item">
        <i class="fas fa-book"></i>
        <span>Modules</span>
      </div>
      <div class="sidebar-item">
        <i class="fas fa-graduation-cap"></i>
        <span>Grades</span>
      </div>
      <div class="sidebar-item">
        <i class="fas fa-inbox"></i>
        <span>Inbox</span>
        <span class="notification-badge">15</span>
      </div>
      <div class="sidebar-item">
        <i class="fas fa-comments"></i>
        <span>Discuss</span>
      </div>
      <div class="sidebar-item">
        <i class="fas fa-calculator"></i>
        <span>Calc</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SideBar'
  }
  </script>
  
  <style scoped>
  .sidebar {
    width: 200px;
    background-color: #465A74;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 20px;
  }
  
  .sidebar-item {
    display: flex;
    align-items: center;
    padding: 10px;
    width: 100%;
    text-align: left;
    cursor: pointer;
  }
  
  .sidebar-item i {
    margin-right: 10px;
  }
  
  .sidebar-item .notification-badge {
    background-color: red;
    color: white;
    border-radius: 50%;
    padding: 5px 10px;
    margin-left: auto;
  }
  
  .sidebar-item:hover {
    background-color: #3a4d66;
  }
  </style>
  