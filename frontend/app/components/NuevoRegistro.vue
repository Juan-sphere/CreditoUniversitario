<template>
  <div class="mt-5">
    <div
      v-if="ifTabs"
      class="flex items-center border border-gray-300 text-center"
      :class="{
        'justify-around w-full': tabs.length >= 3,
        'w-fit': tabs.length < 3,
      }"
    >
      <div
        v-for="(tab, index) in tabs"
        :key="index"
        :class="[
          'py-2 px-4',
          { 'bg-[#F8FBF9]': index === 0, 'bg-[#DCE4E6]': index !== 0 },
        ]"
        :style="tabs.length >= 3 ? { width: `${100 / tabs.length}%` } : {}"
      >
        <h2>{{ tab }}</h2>
      </div>
    </div>
    <div>
      <div class="bg-[#F8FBF9] p-2 border border-gray-300">
        <p>
          {{ title }}
        </p>
      </div>
      <div class="p-5 border border-gray-300">
        <slot name="nuevo-registro"></slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  tabs: string[];
  title: string;
  ifTabs?: boolean;
}>();
</script>

<style scoped></style>
