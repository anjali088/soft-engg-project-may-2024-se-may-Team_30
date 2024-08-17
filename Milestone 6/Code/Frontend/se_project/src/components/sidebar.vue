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
        <i class="fas fa-calculator open-calculator" @click="showCalculator"></i>
        <CalculatorBox ref="calculator"></CalculatorBox>
        <span>Calc</span>
      </div>
    </div>
  </template>
  
  <script>
  import CalculatorBox from './calculator.vue';

  export default {
    name: 'SideBar',
    components: {
      CalculatorBox
    },
    methods: {
      showCalculator(){
        this.$refs.calculator.openCalculator()
      }
    }
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
    height: 700px;
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

  i.open-calculator{
    padding: 10px 20px;
    font-size: 1em;
    background: #444;
    color: #fff;
    border-radius: 5px;
    cursor: pointer;
    display: inline-block;
  }
  </style>
  