<template>
    <div class="w-full">
        <Information title="Registrar Datos del Padre">
            <template #information>
                <div class="p-4 space-y-4 text-gray-700">
                    <!-- Fila 1 -->
                    <div class="grid grid-cols-4 gap-4">
                        <div class="col-span-4 text-secondary font-bold text-shadow-2xs">
                            <h1>Datos Generales</h1>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Tipo de Documento <span
                                    class="text-red-500">(*)</span></label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                <option value="">--Seleccione--</option>
                                <option value="">DNI</option>
                                <option value="">CE</option>
                            </select>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Número de Documento
                                <span class="text-red-500">(*)</span></label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
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
                            <label class="font-semibold text-sm">Fecha de Nacimiento
                                <span class="text-red-500">(*)</span></label>
                            <input type="date" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Primer Nombre <span
                                    class="text-red-500">(*)</span></label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Segundo Nombre <span
                                    class="text-red-500">(*)</span></label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Primer Apellido <span
                                    class="text-red-500">(*)</span></label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Segundo Apellido <span
                                    class="text-red-500">(*)</span></label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                        </div>
                    </div>
                    <!-- Fila 2 -->
                    <div class="grid grid-cols-4 gap-4">
                        <div class="col-span-4 text-secondary font-bold text-shadow-2xs">
                            <h1>Datos de Contactos</h1>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Correo</label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Celular</label>
                            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                        </div>
                        <div class="col-span-2">
                            <label class="font-semibold text-sm">Teléfono fijo</label>

                            <div class="flex gap-2 mt-1">
                                <input type="text" placeholder="Prefijo"
                                    class="w-1/4 px-3 py-1 border border-gray-300 rounded" />

                                <input type="text" placeholder="Número"
                                    class="w-2/4 px-3 py-1 border border-gray-300 rounded" />

                                <input type="text" placeholder="Anexo"
                                    class="w-1/4 px-3 py-1 border border-gray-300 rounded" />
                            </div>
                        </div>
                    </div>
                    <!-- Fila 3 -->
                    <div class="grid grid-cols-3">
                        <div class="col-span-4 text-secondary font-bold text-shadow-2xs">
                            <h1>Datos Laborales</h1>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Vive con usted</label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                <option value="">--Seleccione--</option>
                                <option value="">Si</option>
                                <option value="">No</option>
                            </select>
                        </div>
                        <div class="mx-4">
                            <label class="font-semibold text-sm">Trabaja?</label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                <option value="">--Seleccione--</option>
                                <option value="">Si</option>
                                <option value="">No</option>
                            </select>
                        </div>
                        <div>
                            <label class="font-semibold text-sm">Es trabajador Independiente
                            </label>
                            <select class="w-full px-3 py-1 border border-gray-300 rounded mt-1">
                                <option value="">--Seleccione--</option>
                                <option value="">Si</option>
                                <option value="">No</option>
                            </select>
                        </div>
                        <div class="col-span-3 grid grid-cols-2 gap-4 mt-4">
                            <div class="w-full">
                                <label class="font-semibold text-sm">Grado de Instrucción
                                    <span class="text-red-500">(*)</span></label>
                                <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                            <div class="w-full">
                                <label class="font-semibold text-sm">Profesión u Oficio
                                    <span class="text-red-500">(*)</span></label>
                                <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" />
                            </div>
                        </div>
                    </div>
                    <!-- Fila 4-->
                    <div class="flex flex-row justify-start items-center">
                        <label class="inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="saludPadre" class="sr-only peer" />
                            <span class="select-none ms-3 text-sm font-medium text-heading mr-3">
                                El padre tiene problemas de salud?</span>
                            <div
                                class="relative w-9 h-5 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/30 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-primary">
                            </div>
                        </label>
                        <label class="inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="fallecidoPadre" class="sr-only peer" />
                            <span class="select-none ms-3 text-sm font-medium text-heading mr-3">
                                El padre fallecio?</span>
                            <div
                                class="relative w-9 h-5 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/30 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-primary">
                            </div>
                        </label>
                    </div>

                    <div class="w-full flex justify-between items-center mt-5">
                        <div>
                            <p class="text-white bg-red-500">Campos Obligatorios (*)</p>
                        </div>
                        <button type="submit" class="px-4 py-1 bg-terciary text-white">
                            Registrar
                        </button>
                    </div>
                </div>
            </template>
        </Information>
    </div>
</template>
<script setup lang="ts">
import { ref } from "vue";

const saludPadre = ref(false);
const fallecidoPadre = ref(false);
</script>
