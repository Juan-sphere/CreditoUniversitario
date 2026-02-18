<template>
  <div class="w-full">
    <Information title="Colegio de procedencia">
      <template #information>
        <div class="bg-[#FFF9E9] p-4">
          <p class="text-yellow-500">
            Aviso! No Existen registros para la consulta...
          </p>
        </div>
      </template>
    </Information>
    <NuevoRegistro
      :ifTabs="true"
      :tabs="['Nuevo registro']"
      title="Registrar Colegio de procedencia"
    >
      <template #nuevo-registro>
        <div class="grid grid-cols-2 gap-4 p-2">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Nombre Institución <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Tipo de Institución <span class="text-red-500">(*)</span></label
            >
            <select class="w-full px-3 py-1 border border-gray-300 rounded">
              <option>--Seleccione--</option>
            </select>
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Año fin de Estudios <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Desempeño Académico <span class="text-red-500">(*)</span></label
            >
            <select class="w-full px-3 py-1 border border-gray-300 rounded">
              <option>--Seleccione--</option>
            </select>
          </div>
          <div class="flex flex-col gap-2 col-span-2">
            <div class="flex flex-col gap-2">
              <span class="text-gray-700 font-semibold"
                >Recibio Beca <span class="text-red-500">(*)</span>
              </span>
              <button
                type="button"
                role="switch"
                :aria-checked="enabled"
                class="relative inline-flex h-6 w-11 shrink-0 rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
                :class="enabled ? 'bg-primary' : 'bg-gray-300'"
                @click="enabled = !enabled"
              >
                <span
                  class="pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out"
                  :class="enabled ? 'translate-x-5' : 'translate-x-0'"
                />
              </button>
            </div>
          </div>
          <div class="w-full flex justify-start mt-5">
            <button type="submit" class="px-4 py-1 bg-terciary text-white">
              Registrar
            </button>
          </div>
        </div>
      </template>
    </NuevoRegistro>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const label = "Activo";
const enabled = ref(false);
</script>
<style scoped></style>
