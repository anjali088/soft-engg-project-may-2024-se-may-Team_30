<template>
    <HeaderBar></HeaderBar>
    <SideBar></SideBar>
</template>



<script>

import HeaderBar from './header.vue';
import SideBar from './sidebar.vue';

export default{
    name: 'LandingPage',
    components: {
        HeaderBar,
        SideBar
    }
}
</script>