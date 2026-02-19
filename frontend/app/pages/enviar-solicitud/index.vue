<template>
    <div class="w-full">
        <Information title="DATOS DE LA SOLICITUD">
            <template #information>
                <div class="p-4 space-y-6 text-gray-700">
                    <!-- Primera fila: Nombre solicitante y Nombre institución -->
                    <div class="grid grid-cols-2 gap-4">
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-2">Nombre del solicitante</label>
                            <input type="text" class="w-full px-3 py-2 border border-gray-300 rounded" />
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-2">Nombre de la Institución donde Cursará el
                                Programa</label>
                            <input type="text" class="w-full px-3 py-2 border border-gray-300 rounded" />
                        </div>
                    </div>

                    <!-- Segunda fila: Beneficio solicitado y Convocatoria -->
                    <div class="grid grid-cols-2 gap-4">
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-2">Beneficio Solicitado</label>
                            <select class="w-full px-3 py-2 border border-gray-300 rounded">
                                <option>--Seleccione--</option>
                            </select>
                        </div>
                        <div class="flex flex-col">
                            <label class="font-semibold text-sm mb-2">Convocatoria</label>
                            <select class="w-full px-3 py-2 border border-gray-300 rounded">
                                <option>--- Seleccionar Convocatoria ---</option>
                            </select>
                        </div>
                    </div>

                    <!-- Tercera fila: Textarea para explicación -->
                    <div class="flex flex-col">
                        <label class="font-semibold text-sm mb-2">Explique usted el motivo o la razón por la cual
                            solicita la beca o recategorización (Máximo 500 caracteres)</label>
                        <textarea class="w-full px-3 py-2 border border-gray-300 rounded resize-none"
                            rows="6"></textarea>
                    </div>

                    <!-- Declaración jurada -->
                    <div class="border-t pt-4">
                        <label class="flex items-start cursor-pointer hover:bg-gray-50 p-3 rounded -mx-3">
                            <input type="checkbox" v-model="declaration"
                                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400" />
                            <span class="ml-3">
                                <p class="text-gray-800 font-semibold">
                                    Declaro que la información presentada en este formulario es verdadera, fidedigna y
                                    actual, y lo hago con carácter de declaración jurada.
                                </p>
                            </span>
                        </label>
                    </div>

                    <!-- Botón Enviar solicitud -->
                    <div class="flex justify-end pt-4">
                        <button @click="handleSubmit" :disabled="!declaration"
                            class="px-6 py-2 bg-terciary text-white rounded font-semibold hover:bg-terciary-dark disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors">
                            Enviar Solicitud
                        </button>
                    </div>
                </div>
            </template>
        </Information>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const declaration = ref(false)

const handleSubmit = () => {
    if (!declaration.value) {
        alert('Debes aceptar la declaración jurada para continuar')
        return
    }

    alert('Solicitud enviada correctamente')
    console.log('Formulario enviado')
}
</script>

<style scoped></style>
