<template>
    <div class="w-full">
        <div class="mb-4 flex justify-end">
            <button class="px-4 py-1 bg-gray-300 text-gray-700 rounded font-semibold hover:bg-gray-400">
                📎 Adjuntar archivo
            </button>
        </div>

        <Information title="ARCHIVOS ADJUNTOS">
            <template #information>
                <div class="bg-[#FFF9E9] p-4">
                    <p class="text-yellow-500">
                        Aviso! No Existen registros para la Consulta...
                    </p>
                </div>
            </template>
        </Information>

        <div class="flex justify-between items-center mt-6">
            <BackNext />
            <button class="px-6 py-2 bg-cyan-400 text-white rounded font-semibold hover:bg-cyan-500">
                Ver y Enviar Solicitud
            </button>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped></style>
