<template>
    <div class="flex justify-center gap-2 mt-15 mb-5">
        <button @click="goBack" :disabled="currentIndex === 0"
            class="border border-gray-300 px-4 py-1 rounded-full text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-100 transition-colors">
            ← Anterior
        </button>
        <button @click="goNext" :disabled="currentIndex === pages.length - 1"
            class="border border-gray-300 px-4 py-1 rounded-full text-secondary disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-100 transition-colors">
            Siguiente →
        </button>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const pages = [
    '/instrucciones',
    '/informacion-personal',
    '/informacion-padres',
    '/composicion-familiar',
    '/personas-externas',
    '/informacion-economica',
    '/patrimonio-familiar',
    '/documentos-sustentacion',
    '/enviar-solicitud'
] as const

const currentIndex = ref(0)

onMounted(() => {
    // Obtener el índice de la página actual
    const path = route.path
    currentIndex.value = pages.findIndex(p => path.endsWith(p))

    // Si no encuentra la página, asume que es la primera
    if (currentIndex.value === -1) {
        currentIndex.value = 0
    }
})

const goBack = () => {
    if (currentIndex.value > 0) {
        currentIndex.value--
        const nextPage = pages[currentIndex.value]
        if (nextPage) router.push(nextPage)
    }
}

const goNext = () => {
    if (currentIndex.value < pages.length - 1) {
        currentIndex.value++
        const nextPage = pages[currentIndex.value]
        if (nextPage) router.push(nextPage)
    }
}
</script>

<style scoped></style>