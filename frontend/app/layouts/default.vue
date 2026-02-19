<template>
  <div class="max-w-350 mx-auto">
    <div class="pt-20">
      <Header />
      <div class="flex gap-5 w-full">
        <Menu class="w-1/4 shrink-0" />

        <div class="w-3/4 min-w-0">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Register from "~/components/Register.vue";
</script>

<style scoped></style>
