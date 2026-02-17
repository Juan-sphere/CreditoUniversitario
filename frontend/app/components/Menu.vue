<template>
    <div class="border-2 border-primary flex flex-col items-start">
        <NuxtLink v-for="item in menuItems" :key="item.label" :to="item.path" class="item py-1 px-4 hover:bg-secondary w-full h-full hover:text-white">
            {{ item.label }}
        </NuxtLink>
    </div>
</template>

<script setup lang="ts">
const menuItems = [
    { label: 'Instrucciones', path: '/' },
    { label: 'Información Personal', path: '/' },
    { label: 'Dirección del Alumno', path: '/' },
    { label: 'Datos laborales del Alumno', path: '/' },
    { label: 'Colegio de procedencia', path: '/' },
    { label: 'Información del Padre', path: '/' },
    { label: 'Información de la Madre', path: '/' },
    { label: 'Composición Familiar', path: '/' },
    { label: 'Información Socioeconómica', path: '/' },
    { label: 'Datos de Vivienda', path: '/' },
    { label: 'Datos de Vehículo', path: '/' },
    { label: 'Archivos Adjuntos', path: '/' },
    { label: 'Enviar Solicitud', path: '/' },
]
</script>

<style scoped>

</style>