<template>
    <div class="content-box">
      <!-- Title of the content -->
      <h1 class="content-title">{{videoTitle}}</h1>
      <!-- Rating and review section -->
      <div class="content-meta">
        <span class="rating">- / 5 (0 reviews)</span>
        <a href="#" class="review-link">Submit a review</a>
      </div>
      <div v-if="isLecture">
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

      <div v-else>
        <div class="assignment-container">
          <h2>{{ assignment.title }}</h2>
          <p>Week: {{ assignment.week }}</p>

          <div v-for="(question, index) in assignment.questions" :key="question.que_id" class="question-block">
            <p>{{ index + 1 }}) {{ question.question_text }}</p>
            <input
              v-if="!question.options"
              type="text"
              v-model="userAnswers[question.que_id]"
              class="text-input"
              placeholder="Your answer here"
            />
          </div>
          
          <button @click="submitAnswers">Submit</button>
        </div>
      </div>
      
    </div>
  </template>
  
  <script>
  import axios from 'axios';

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
      isLecture:{
        type: Boolean,
        required: true
      },
    },
    data(){
      return{
        assignment: {
        assign_id: 1,
        title: "Assgn 1",
        week: 1,
        questions: [
          {
            correct_answer: "15",
            options: null,
            que_id: 1,
            question_text: "What is today date"
          },
          {
            correct_answer: "Code",
            options: null,
            que_id: 2,
            question_text: "Write this code"
          }
        ]
      },
      userAnswers: {}
      }
    },
    watch: {
      isLecture(newVal){
        if (!newVal){
          this.fetchAssignment();     // Fetch assignment questions only if it's not a lecture.
        }
      }
    },
    methods: {
      fetchAssignment(){
        console.log("Fetching assignment");
        const lecId = localStorage.getItem('lec_id');
        const path = `http://127.0.0.1:5000/assignment/${lecId}/1`;
        axios.get(path)
          .then((res)=>{
            console.log(res.data);
            this.assignment = res.data;
          })
          .catch((error)=>{
            console.log("Error Fetching Assignmnet", error);
          })
      },
      submitAnswers(){
        console.log('User Answers:', this.userAnswers);
        const lecId = localStorage.getItem('lec_id');
        const path = `http://127.0.0.1:5000/submit_assignment/${lecId}`;
        const payload = {user_id:1 , answers:this.userAnswers};
        axios.post(path, payload)
          .then((res)=>{
            alert(res);
          })
          .catch((error)=>{
            alert(error);
          });
      },
    }
  }
  </script>
  
  <style scoped>
  .content-box {
    background-color: #fff;
    /* border: 1px solid #ccc; */
    border-radius: 8px;
    max-width: 800px;
    margin: 0px auto;
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

  .assignment-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
}

h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.question-block {
  margin-bottom: 20px;
}

.text-input {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border-radius: 4px;
  border: 1px solid #ccc;
  margin-top: 8px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  color: white;
  background-color: #007BFF;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
  </style>
  