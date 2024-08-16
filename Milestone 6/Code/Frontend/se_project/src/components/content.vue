<template>
    <div class="content-box">
      <!-- Title of the content -->
      <h1 class="content-title">{{videoTitle}}</h1>
      <!-- Rating and review section -->
      <div class="content-meta">
        <span class="rating">- / 5 (0 reviews)</span>
        <a href="#" class="review-link">Submit a review</a>
      </div>
      <!-- Embedded YouTube video -->
      <div class="video-container">
        <iframe 
          width="560" 
          height="315" 
          :src="videoUrl"
          :key="videoUrl"
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
        </iframe>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ContentBox',
    props: {
      videoUrl: {
        type: String,
        required: true
      },
      videoTitle: {
        type: String,
        required: true
      },

    }
  }
  </script>
  
  <style scoped>
  .content-box {
    padding: 20px;
    background-color: #fff;
    /* border: 1px solid #ccc; */
    border-radius: 8px;
    max-width: 800px;
    margin: 20px auto;
  }
  
  .content-title {
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  .content-meta {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .rating {
    margin-right: 10px;
  }
  
  .review-link {
    color: #007BFF;
    text-decoration: none;
  }
  
  .review-link:hover {
    text-decoration: underline;
  }
  
  .video-container {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    padding-top: 56.25%;
    position: relative;
    width: 50rem;
    height: 10rem;
  }
  
  .video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  </style>
  