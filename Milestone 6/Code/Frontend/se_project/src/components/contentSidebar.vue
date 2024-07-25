<template>
    <!-- Sidebar container -->
    <div class="sidebar">
      <!-- Loop through sections to create each section  -->
      <div v-for="(section, index) in sections" :key="index" class="section">
        <!-- Section title with a click event to toggle section visibilty -->
        <div @click="toggleSection(index)" class="section-title">
          {{ section.title }}
          <span>{{ section.isOpen ? '-' : '+' }}</span>
        </div>
        <!-- Section content visible only if the section is open -->
        <div v-if="section.isOpen" class="section-content">
          <ul>
            <!-- Loop through items to create list items -->
            <li v-for="(item, idx) in section.items" :key="idx">{{ item }}</li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "contentSidebar",
    data() {
      return {
        sections: [
          {
            title: "Course Introduction",
            isOpen: false,
            items: ["Introduction Video", "Syllabus", "Instructor Info"]
          },
          {
            title: "Course Project",
            isOpen: false,
            items: ["Project Overview", "Requirements"]
          },
          {
            title: "Week 1",
            isOpen: false,
            items: ["Lecture 1", "Assignment 1"]
          },
          // Add other sections here...
        ]
      };
    },
    methods: {
        // Toggle the open state of the clicked section, close all others.
      toggleSection(index) {
        this.sections.forEach((section, idx) => {
          section.isOpen = idx === index ? !section.isOpen : false;
        });
      }
    }
  };
  </script>
  
  <style>
  /* Styles for the sidebar container */
  .sidebar {
    width: 250px;
    border-right: 1px solid #ccc;
    padding: 10px;
  }
  /* Styles for each section title, making it clickable */
  .section {
    margin-bottom: 10px;
  }
  /* Styles for the section title, making ti clickable */
  .section-title {
    cursor: pointer;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  /* Styles for the section content */
  .section-content {
    padding-left: 10px;
    margin-top: 5px;
  }
  </style>
  