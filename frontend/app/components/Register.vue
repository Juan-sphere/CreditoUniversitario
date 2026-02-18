<template>
  <div>
    <div
      class="flex items-center mt-5 border border-gray-300 text-center"
      :class="{
        'justify-around w-full': tabs.length >= 3,
        'w-fit': tabs.length < 3,
      }"
    >
      <div
        v-for="(tab, index) in tabs"
        :key="index"
        @click="emit('tab-change', index)"
        :class="[
          'py-2 px-4 cursor-pointer transition-colors',
          {
            'bg-[#fff]': index === activeTab,
            'bg-[#DCE4E6]': index !== activeTab,
          },
        ]"
        :style="tabs.length >= 3 ? { width: `${100 / tabs.length}%` } : {}"
      >
        <h2>{{ tab }}</h2>
      </div>
    </div>
    <div>
      <div class="bg-yellow-100">
        <slot name="register">
          <p class="text-yellow-500 p-5">
            Aviso! No Existen registros para la consulta...
          </p>
        </slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  tabs: string[];
  activeTab?: number;
}>();

const emit = defineEmits<{
  "tab-change": [index: number];
}>();
</script>

<style scoped></style>
