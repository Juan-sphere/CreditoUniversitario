<template>
    <div class="w-full">
        <Information title="DATOS DEL PATRIMONIO">
            <template #information>
                <div class="bg-[#FFF9E9] p-4">
                    <p class="text-yellow-500">
                        Aviso! No Existen registros para la Consulta...
                    </p>
                </div>
            </template>
        </Information>

        <NuevoRegistro :tabs="['Nueva información de vivienda']" title="Nueva información de vivienda" :ifTabs="false">
            <template #nuevo-registro>
                <div class="space-y-4 p-4">
                    <div class="grid grid-cols-3 gap-4">
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Tipo de vivienda <span
                                    class="text-red-500">(*)</span></label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded">
                                <option>--Seleccione--</option>
                            </select>
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">SubTipo / Concepto</label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded">
                                <option>--Seleccione--</option>
                            </select>
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Tipo de Bien <span
                                    class="text-red-500">(*)</span></label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded">
                                <option>--Seleccione--</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid grid-cols-3 gap-4">
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Reside desde <span
                                    class="text-red-500">(*)</span></label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Área del Terreno de la vivienda en M2</label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Área Construida de la vivienda en M2</label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Moneda</label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded">
                                <option>--Seleccione--</option>
                            </select>
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Valor Aproximado</label>
                            <input type="text" value="0" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        </div>
                    </div>

                    <div class="w-full flex justify-start items-center mt-5">
                        <button type="submit" class="px-4 py-1 bg-terciary text-white">
                            Grabar
                        </button>
                    </div>
                </div>
            </template>
        </NuevoRegistro>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped></style>
