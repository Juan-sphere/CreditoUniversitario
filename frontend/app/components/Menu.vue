<template>
    <div class="border-2 border-primary flex flex-col items-start h-fit w-1/3">
        <NuxtLink v-for="item in menuItems" :key="item.label" :to="item.path"
            class="item py-1 px-4 hover:bg-secondary w-full h-full hover:text-white"
            active-class="bg-secondary text-white">
            {{ item.label }}
        </NuxtLink>
    </div>
</template>

<script setup lang="ts">
const menuItems = [
    { label: 'Instrucciones', path: '/instrucciones' },
    { label: 'Información Personal', path: '/informacion-personal' },
    { label: 'Dirección del Alumno', path: '/direccion-alumno' },
    { label: 'Datos laborales del Alumno', path: '/datos-laborales-alumno' },
    { label: 'Colegio de procedencia', path: '/colegio-procedencia' },
    { label: 'Información del Padre', path: '/informacion-padre' },
    { label: 'Información de la Madre', path: '/informacion-madre' },
    { label: 'Composición Familiar', path: '/composicion-familiar' },
    { label: 'Información Socioeconómica', path: '/informacion-socioeconomica' },
    { label: 'Datos de Vivienda', path: '/datos-vivienda' },
    { label: 'Datos de Vehículo', path: '/datos-vehiculo' },
    { label: 'Archivos Adjuntos', path: '/archivos-adjuntos' },
    { label: 'Enviar Solicitud', path: '/enviar-solicitud' },
]
</script>

<style scoped></style>