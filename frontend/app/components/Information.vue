<template>
  <div class="w-full">
    <div class=" text-white border">
      <div class="bg-secondary p-2">
        <h2 class="text-lg font-bold ">{{ title }}</h2>
      </div>
      <div class="border border-gray-400 ">
        <slot name="information"></slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string;
}
const { title } = defineProps<Props>();
</script>

<style scoped></style>