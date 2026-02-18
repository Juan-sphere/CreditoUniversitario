<template>
    <div class="w-full">
        <Information title="Registrar Familiar">
            <template #information>
                <div class="p-4 space-y-4 text-gray-700 overflow-hidden">
                    <div class="grid grid-cols-4 gap-4">
                        <div class="col-span-4 text-secondary font-bold text-shadow-2xs">
                            <h1>Datos Generales</h1>
                        </div>
                        <div class="col-span-4">
                            <label class="font-semibold text-sm">Nombre <span class="text-red-500">(*)</span></label>
                            <div class="flex gap-2 mt-1">
                                <input type="text" placeholder="Primer Nombre"
                                    class="flex-1 px-3 py-1 border border-gray-300 rounded" />
                                <input type="text" placeholder="Segundo Nombre"
                                    class="flex-1 px-3 py-1 border border-gray-300 rounded" />
                                <input type="text" placeholder="Primer Apellido"
                                    class="flex-1 px-3 py-1 border border-gray-300 rounded" />
                                <input type="text" placeholder="Segundo Apellido"
                                    class="flex-1 px-3 py-1 border border-gray-300 rounded" />
                            </div>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Parentesco <span
                                    class="text-red-500">(*)</span></label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                <option value="">--Seleccione--</option>
                                <option value="">Padre</option>
                                <option value="">Madre</option>
                            </select>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Estado Civil <span
                                    class="text-red-500">(*)</span></label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                <option value="">--Seleccione--</option>
                                <option value="">Soltero</option>
                                <option value="">Casado</option>
                                <option value="">Divorciado</option>
                                <option value="">Viudo</option>
                            </select>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Es familia dependiente? <span
                                    class="text-red-500">(*)</span></label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                <option value="">--Seleccione--</option>
                                <option value="">Sí</option>
                                <option value="">No</option>
                            </select>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Vive con usted? <span
                                    class="text-red-500">(*)</span></label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                <option value="">--Seleccione--</option>
                                <option value="">Sí</option>
                                <option value="">No</option>
                            </select>
                        </div>
                        <div class="col-span-4 grid grid-cols-3 gap-4">
                            <div class="flex flex-col">
                                <label class="font-semibold text-sm">Fecha de Nacimiento <span
                                        class="text-red-500">(*)</span></label>
                                <input type="date" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                            <div class="flex flex-col">
                                <label class="font-semibold text-sm">Grado de instrucción <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                            <div class="flex flex-col">
                                <label class="font-semibold text-sm">Profesión Ocupación <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                        </div>
                        <div>
                            <div>
                                <label class="font-semibold text-sm">Trabaja </label>
                                <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">No</option>
                                    <option value="">Si</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Estudia </label>
                                <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                    <option value="">No</option>
                                    <option value="">Si</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row justify-start items-center">
                        <label class="inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="saludMadre" class="sr-only peer" />
                            <span class="select-none ms-3 text-sm font-medium text-heading mr-3">El familiar tiene
                                problemas de salud?</span>
                            <div
                                class="relative w-9 h-5 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/30 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-primary">
                            </div>
                        </label>
                        <label class="inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="fallecidoMadre" class="sr-only peer" />
                            <span class="select-none ms-3 text-sm font-medium text-heading mr-3">El familiar
                                fallecio?</span>
                            <div
                                class="relative w-9 h-5 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/30 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-primary">
                            </div>
                        </label>
                    </div>
                    <div class="w-full flex justify-end items-center mt-5">
                        <button type="submit" class="px-4 py-1 bg-terciary text-white">
                            Grabar
                        </button>
                    </div>
                </div>
            </template>
        </Information>
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const saludMadre = ref(false);
const fallecidoMadre = ref(false);
</script>