<template>
  <!-- Sidebar component -->
    <div class="sidebar">
      <!-- Sidebar item for modules -->
      <div class="sidebar-item">
        <i class="fas fa-book"></i>
        <span>Modules</span>
      </div>
      <!-- Sidebar item for grades -->
      <div class="sidebar-item">
        <i class="fas fa-graduation-cap"></i>
        <span>Grades</span>
      </div>
      <!-- Sidebar item for inbox with a notification badge -->
      <div class="sidebar-item">
        <i class="fas fa-inbox"></i>
        <span>Inbox</span>
        <span class="notification-badge">15</span>
      </div>
      <!-- Sidebar item for discuss -->
      <div class="sidebar-item">
        <i class="fas fa-comments"></i>
        <span>Discuss</span>
      </div>
      <!-- Sidebar item for calculator -->
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
  /* Styles for the sidebar container */
  .sidebar {
    width: 70px;
    background-color: #465A74;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 20px;
  }

  /* Styles for each sidebar item */
  .sidebar-item {
    display: flex;
    align-items: center;
    padding: 10px;
    width: 100%;
    text-align: left;
    cursor: pointer;
    flex-direction: column;
  }
  /* Margin for icons within sidebar items */
  .sidebar-item i {
    margin-right: 10px;
  }
  /* Styles fot the notification badge in the Inbox item */
  .sidebar-item .notification-badge {
    background-color: red;
    color: white;
    border-radius: 50%;
    padding: 5px 10px;
    margin-left: auto;
  }
  /* Hover effect of sidebar items */
  .sidebar-item:hover {
    background-color: #3a4d66;
  }
  </style>
  