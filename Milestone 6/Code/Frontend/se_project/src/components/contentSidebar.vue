<template>
  <!-- Sidebar container -->
  <div class="sidebar">
    <!-- Loop through sections to create each section -->
    <div v-for="(section, index) in sections" :key="index" class="section">
      <!-- Section title with a click event to toggle section visibility -->
      <div @click="toggleSection(index)" class="section-title">
        {{ section.title }}
        <span>{{ section.isOpen ? '-' : '+' }}</span>
      </div>
      <!-- Section content visible only if the section is open -->
      <div v-if="section.isOpen" class="section-content">
        <ul>
          <!-- Loop through items to create list items -->
          <li 
            v-for="item in section.items" 
            :key="item.id"
            @click.prevent="handleItemClick(item.video_url, item.title, item.id)">
            {{ item.title }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "ContentSidebar",
  data() {
    return {
      sections: []  // Initialize sections as an empty array
    };
  },
  methods: {
    // Toggle the open state of the clicked section, close all others.
    toggleSection(index) {
      this.sections.forEach((section, idx) => {
        section.isOpen = idx === index ? !section.isOpen : false;
      });
    },
    // Handle item click
    handleItemClick(url, title, id){
      // Emit am evemt to the parent component with the item's id and title
      if (url){
        this.$emit('change-video', url, title, id, true); //Emit an event with the video url.
        localStorage.setItem('lec_id', id);
      }else{
        this.$emit('change-video', url, title, id, false); //Emit an event with the video url.
        localStorage.setItem('lec_id', id);
      }
    },
    // Fetch content from the server
    getContent() {
    console.log("Fetching content...");
    const path = 'http://127.0.0.1:5000/content';
    axios.get(path)
      .then((res) => {
        console.log("Content fetched:", res.data);

        // Check if res.data contains the sections array directly
        let sections = res.data;

        // If the data is wrapped in an object, adjust this based on actual structure
        if (sections.sections) {
          sections = sections.sections;
        }

        // Store fetched data in localStorage
        localStorage.setItem('content', JSON.stringify(sections));

        // Update sections with the fetched data
        this.sections = sections.map(section => ({
          ...section,
          isOpen: false  // Ensure all sections are initially closed
        }));
      })
      .catch((error) => {
        console.error("Error fetching content:", error);
      });
    } 
  },
  created() {
    // Fetch content when the component is created
    this.getContent();
  }
};
</script>

<style scoped>
/* Styles for the sidebar container */
.sidebar {
  width: 275px;
  border-right: 1px solid #ccc;
  padding: 10px;
}

/* Styles for each section */
.section {
  margin-bottom: 10px;
}

/* Styles for the section title, making it clickable */
/* .section-title {
  cursor: pointer;
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  align-items: center;
} */
.section-title {
  cursor: pointer;
  font-weight: bold;
  display: flex;
  justify-content: space-between; /* Aligns text to the left */
  align-items: center;
  position: relative;
  padding-bottom: 10px; /* Adds some space between text and underline */
}

.section-title::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 1.3px; /* Thickness of the bold line */
  background-color: rgba(0, 0, 0, 0.618); /* Color of the line */
  font-weight: bold; /* Ensures the line is bold */
}


/* Styles for the section content */
.section-content {
  padding-left: 0px;
  margin-top: 5px;
  list-style-type: none; /* Removes the bullet points */
}

.section-content li {
  position: relative;
  padding-bottom: 10px; /* Adds space between text and the underline */
  margin-bottom: 10px; /* Adds space between the line and the next item */
  text-align: left; /* Aligns the text to the leftmost side */
}

.section-content li::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 1px; /* Thickness of the line */
  background-color: rgba(0, 0, 0, 0.539); /* Color of the line */
}



</style>
