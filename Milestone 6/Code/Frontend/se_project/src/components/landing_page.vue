<template>
    <!-- Include the HeaderBar component at the top -->
    <HeaderBar></HeaderBar>
    <!-- Container for the sidebars, including both sideBar and contentSidebar -->
    <div id = "sidebars">
        <!-- Include the SideBar component -->
        <SideBar></SideBar>
        <!-- Include the contentSidebar component -->
        <contentSidebar @change-video="updateVideoUrl"></contentSidebar>
        <ContentBox :video-url="videoUrl" :video-title="videoTitle"></ContentBox>
        <chat></chat>
    </div>
    
    
</template>

<script>

import HeaderBar from './header.vue';
import SideBar from './sidebar.vue';
import contentSidebar from './contentSidebar.vue';
import ContentBox from './content.vue';
import chat from './chat.vue'

export default{
    name: 'LandingPage',
    
    components: {
        HeaderBar,
        SideBar,
        contentSidebar,
        ContentBox,
        chat
    },
    data(){
      return {
        videoUrl: '', // Initiaize video url as an empty string.
        videoTitle: ''
      };
    },
    methods: {
        updateVideoUrl(url, title){
            this.videoUrl = url; // Update the video URL when a link is clicked.
            this.videoTitle = title;
        }
    }
};
</script>

<style scoped>
/* Ensure html and body take up the full viewport */
html, body{
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
}

/* Flex container for the sidebars to align them side by side */
#sidebars{
    display: flex;
    height: 100%;
    width: 100%;
}

</style>