<template>
  <div class="w-full">
    <Information title="Información personal">
      <template #information>
        <div class="grid grid-cols-2 gap-4 p-4">
          <div class="grid grid-cols-[auto_1fr] gap-x-4 gap-y-2 items-center">
            <label class="text-gray-700 font-semibold">Nombre</label>
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
            <label class="text-gray-700 font-semibold">DNI</label>
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
            <label class="text-gray-700 font-semibold"
              >Fecha de nacimiento</label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
          <div
            class="grid grid-cols-[auto_1fr] gap-x-4 gap-y-2 items-center self-start"
          >
            <label class="text-gray-700 font-semibold">Género</label>
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
            <label class="text-gray-700 font-semibold"
              >Lugar de Nacimiento</label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
        </div>
      </template>
    </Information>
    <div class="w-full flex justify-end mt-4">
      <button type="submit" class="px-4 py-1 bg-terciary text-white rounded">
        Editar
      </button>
    </div>
    <Register
      :tabs="['Estado Civil', 'Teléfono', 'Dirección']"
      :activeTab="activeTab"
      @tab-change="activeTab = $event"
    >
      <template v-if="activeTab === -1" #register>
        <!-- Slot para cuando no hay tab seleccionado -->
      </template>
    </Register>
    <!-- 
    <NuevoRegistro
      v-if="activeTab === 0"
      :ifTabs="false"
      :tabs="[]"
      title="Estado Civil"
    >
      <template #nuevo-registro>
        <div class="grid grid-cols-2 gap-4 p-2">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Estado Civil <span class="text-red-500">(*)</span></label
            >
            <select class="w-full px-3 py-1 border border-gray-300 rounded">
              <option>--Seleccione--</option>
              <option>Soltero(a)</option>
              <option>Casado(a)</option>
              <option>Divorciado(a)</option>
              <option>Viudo(a)</option>
              <option>Unión Libre</option>
            </select>
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Fecha de Cambio <span class="text-red-500">(*)</span></label
            >
            <input
              type="date"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
        </div>
        <div class="w-full flex justify-between items-center mt-5 pl-2">
          <div>
            <p class="text-white bg-red-500 px-2">Campos Obligatorios (*)</p>
          </div>
          <button type="submit" class="px-4 py-1 bg-terciary text-white">
            Registrar
          </button>
        </div>
      </template>
    </NuevoRegistro>

    <NuevoRegistro
      v-if="activeTab === 1"
      :ifTabs="false"
      :tabs="[]"
      title="Teléfono"
    >
      <template #nuevo-registro>
        <div class="grid grid-cols-2 gap-4 p-2">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Tipo de Teléfono <span class="text-red-500">(*)</span></label
            >
            <select class="w-full px-3 py-1 border border-gray-300 rounded">
              <option>--Seleccione--</option>
              <option>Celular</option>
              <option>Fijo</option>
              <option>Otro</option>
            </select>
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Número <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
              placeholder="Ej: 987654321"
            />
          </div>
        </div>
        <div class="w-full flex justify-between items-center mt-5 pl-2">
          <div>
            <p class="text-white bg-red-500 px-2">Campos Obligatorios (*)</p>
          </div>
          <button type="submit" class="px-4 py-1 bg-terciary text-white">
            Registrar
          </button>
        </div>
      </template>
    </NuevoRegistro>

    <NuevoRegistro
      v-if="activeTab === 2"
      :ifTabs="false"
      :tabs="[]"
      title="Dirección"
    >
      <template #nuevo-registro>
        <div class="grid grid-cols-2 gap-4 p-2">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Calle <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
              placeholder="Nombre de la calle"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Número <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
              placeholder="Número del domicilio"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Distrito <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Provincia <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
        </div>
        <div class="w-full flex justify-between items-center mt-5 pl-2">
          <div>
            <p class="text-white bg-red-500 px-2">Campos Obligatorios (*)</p>
          </div>
          <button type="submit" class="px-4 py-1 bg-terciary text-white">
            Registrar
          </button>
        </div>
      </template>
    </NuevoRegistro> -->

    <div>
      <select
        name="grabar"
        id="grabar"
        class="px-3 py-1 border border-gray-300 rounded mt-5 mr-5 text-left w-1/2"
      >
        <option value="grabar">--Seleccione--</option>
        <option value="grabar">Grabar</option>
      </select>
      <button class="px-4 py-1 bg-terciary text-white rounded">Grabar</button>
    </div>

    <BackNext />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const activeTab = ref(0);
</script>
