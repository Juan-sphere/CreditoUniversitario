<template>
    <div class="max-w-325 mx-auto">
        <Header />
        <div class="flex gap-5 w-full">
            <Menu class="w-1/4" />
            
            <slot class="w-3/4" />
        </div>
 
    </div>
</template>

<script setup lang="ts">
import Register from '~/components/Register.vue';


</script>

<style scoped>

</style>