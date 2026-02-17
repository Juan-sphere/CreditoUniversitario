<template>
    <div class="w-full">
        <label class="inline-flex items-center cursor-pointer gap-3 mb-4">
            <span class="text-gray-700 font-semibold">{{ label }}</span>
            <button type="button" role="switch" :aria-checked="enabled"
                class="relative inline-flex h-6 w-11 shrink-0 rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
                :class="enabled ? 'bg-primary' : 'bg-gray-300'" @click="enabled = !enabled">
                <span
                    class="pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out"
                    :class="enabled ? 'translate-x-5' : 'translate-x-0'" />
            </button>
        </label>

        <div v-if="enabled">
            <Information title="Nuevos Datos Laborales">
                <template #information>
                    <div class="p-4 space-y-4 text-gray-700">
                        <!-- Fila 1 -->
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <label class="font-semibold text-sm">Estado laboral <span class="text-red-500">(*)</span></label>
                                <select v-model="form.estadoLaboral" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Remuneración neta Mensual</label>
                                <input v-model="form.remuneracion" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Emite recibos por honorarios?</label>
                                <select v-model="form.emiteRecibos" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                        </div>

                        <!-- Fila 2 -->
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <label class="font-semibold text-sm">Número (R.U.C.)/(R.U.S.)</label>
                                <input v-model="form.ruc" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Condición laboral <span class="text-red-500">(*)</span></label>
                                <select v-model="form.condicionLaboral" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                        </div>

                        <hr class="border-gray-200" />

                        <!-- Fila 3 -->
                        <div class="grid grid-cols-[2fr_1fr_1fr] gap-4">
                            <div>
                                <label class="font-semibold text-sm">Razon Social de Centro Laboral <span class="text-red-500">(*)</span></label>
                                <input v-model="form.razonSocial" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Desde</label>
                                <input v-model="form.desde" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Hasta</label>
                                <input v-model="form.hasta" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                        </div>

                        <!-- Fila 4 -->
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <label class="font-semibold text-sm">Cargo <span class="text-red-500">(*)</span></label>
                                <input v-model="form.cargo" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Tipo de trabajador</label>
                                <select v-model="form.tipoTrabajador" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Correo laboral</label>
                                <input v-model="form.correoLaboral" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                        </div>

                        <!-- Fila 5 -->
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <label class="font-semibold text-sm">Teléfono Laboral</label>
                                <select v-model="form.telefonoLaboral" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                        </div>

                        <!-- Fila 6 -->
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <label class="font-semibold text-sm">Tipo Establecimiento</label>
                                <select v-model="form.tipoEstablecimiento" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Nombre Establecimiento</label>
                                <input v-model="form.nombreEstablecimiento" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                        </div>

                        <hr class="border-gray-200" />

                        <!-- Fila 7 -->
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <label class="font-semibold text-sm">Labor que realiza</label>
                                <input v-model="form.laborRealiza" type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                        </div>

                        <!-- Fila 8 -->
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <label class="font-semibold text-sm">Región / Departamento <span class="text-red-500">(*)</span></label>
                                <select v-model="form.region" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Provincia <span class="text-red-500">(*)</span></label>
                                <select v-model="form.provincia" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Distrito <span class="text-red-500">(*)</span></label>
                                <select v-model="form.distrito" class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">--Seleccione--</option>
                                </select>
                            </div>
                        </div>

                        <!-- Footer -->
                        <div class="flex items-center justify-between mt-4">
                            <span class="text-red-500 text-sm border border-red-500 px-2 py-1 rounded">Campo obligatorio (*)</span>
                            <button type="button" class="px-4 py-1 bg-primary text-white rounded">Grabar</button>
                        </div>
                    </div>
                </template>
            </Information>
        </div>

        <BackNext />
    </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';

const label = 'Activo';
const enabled = ref(false);

const form = reactive({
    estadoLaboral: '',
    remuneracion: '',
    emiteRecibos: '',
    ruc: '',
    condicionLaboral: '',
    razonSocial: '',
    desde: '',
    hasta: '',
    cargo: '',
    tipoTrabajador: '',
    correoLaboral: '',
    telefonoLaboral: '',
    tipoEstablecimiento: '',
    nombreEstablecimiento: '',
    laborRealiza: '',
    region: '',
    provincia: '',
    distrito: '',
});
</script>

<style scoped></style>
