<template>
    <div class="w-full">
        <!-- Toggle Tiene Vehículos -->
        <div class="bg-white border border-gray-300 p-4 mb-4">
            <div class="flex items-center gap-3">
                <span class="text-gray-700 font-semibold">Tiene Vehículos:</span>
                <button type="button" role="switch" :aria-checked="tieneVehiculos"
                    class="relative inline-flex h-6 w-11 shrink-0 rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
                    :class="tieneVehiculos ? 'bg-primary' : 'bg-gray-300'" @click="tieneVehiculos = !tieneVehiculos">
                    <span
                        class="pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out"
                        :class="tieneVehiculos ? 'translate-x-5' : 'translate-x-0'" />
                </button>
            </div>
        </div>

        <Information title="DATOS DEL PATRIMONIO">
            <template #information>
                <div class="bg-[#FFF9E9] p-4">
                    <p class="text-yellow-500">
                        Aviso! No Existen registros para la Consulta...
                    </p>
                </div>
            </template>
        </Information>

        <NuevoRegistro :tabs="['Nueva información de vehículo']" title="Nueva información de vehículo" :ifTabs="false">
            <template #nuevo-registro>
                <div class="space-y-4 p-4">
                    <!-- Fila 1: Tipo de Patrimonio, SubTipo/Concepto, Tipo de Bien -->
                    <div class="grid grid-cols-3 gap-4">
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Tipo de Patrimonio <span
                                    class="text-red-500">(*)</span></label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded">
                                <option>VEHICULO</option>
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

                    <!-- Fila 2: Año, Marca del Vehículo, Placa del Vehículo -->
                    <div class="grid grid-cols-3 gap-4">
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Año <span class="text-red-500">(*)</span></label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Marca del Vehículo</label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-1">Placa del Vehículo <span
                                    class="text-red-500">(*)</span></label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        </div>
                    </div>

                    <!-- Fila 3: Moneda, Valor Aproximado -->
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
import { ref } from 'vue'

const tieneVehiculos = ref(false)
</script>

<style scoped></style>
