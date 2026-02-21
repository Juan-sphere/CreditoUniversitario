<template>
  <div class="w-full animate-pulse">
    <!-- Tabs skeleton -->
    <div class="flex gap-2 mb-4 px-4">
      <div v-for="i in 4" :key="i" class="h-10 bg-gray-300 rounded w-24"></div>
    </div>

    <!-- Contenido skeleton -->
    <div class="p-4 space-y-4">
      <!-- Grid de campos -->
      <div class="grid grid-cols-2 gap-4">
        <div v-for="i in 4" :key="`field-${i}`" class="flex flex-col gap-2">
          <div class="h-4 bg-gray-300 rounded w-20"></div>
          <div class="h-8 bg-gray-200 rounded"></div>
        </div>
      </div>

      <!-- Espaciador -->
      <div class="mt-6"></div>

      <!-- Más campos -->
      <div class="grid grid-cols-2 gap-4">
        <div
          v-for="i in 2"
          :key="`field-extra-${i}`"
          class="flex flex-col gap-2"
        >
          <div class="h-4 bg-gray-300 rounded w-20"></div>
          <div class="h-8 bg-gray-200 rounded"></div>
        </div>
      </div>

      <!-- Botones skeleton -->
      <div class="flex justify-between items-center mt-6">
        <div class="h-4 bg-gray-300 rounded w-32"></div>
        <div class="h-10 bg-gray-300 rounded w-24"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Skeleton loader component para información personal
</script>
