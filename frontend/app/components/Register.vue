<template>
    <div>
        <div class="flex items-center justify-around mt-5 border border-gray-300 text-center">
            <div class="bg-[#fff] w-1/3 py-2">
                <h2>Estado Civil</h2>
            </div>
            <div class="bg-[#DCE4E6] w-1/3 py-2">
                <h2>Teléfono</h2>
            </div>
            <div class="bg-[#DCE4E6] w-1/3 py-2">
                <h2>Dirección</h2>
            </div>
        </div>
        <div>
             <div class="p-5 bg-[#FFF9E9]">
            <slot name="register">
                <p class="text-yellow-500">
                    Aviso! No Existen registros para la consulta...
                </p>
            </slot>
         </div>
        </div>
    </div>

</template>

<script setup lang="ts">

</script>

<style scoped>

</style>