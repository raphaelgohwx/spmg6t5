<template>
  <div>

    <!-- Include the LJPSNavigation component -->
    <navbar/>
  </div>
</template>

<script>
import navbar from '@/components/navbar.vue'; // Import the component

export default {
  components: {
    navbar, // Register the component
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>