<template>
  <div class="w-full">
    <Information title="Patrimonio del núcleo familiar">
      <template #information>
        <div class="p-4 space-y-6">
          <!-- Lista de patrimonios agregados -->
          <div v-if="patrimonios.length === 0" class="bg-[#FFF9E9] p-4 rounded">
            <p class="text-yellow-600">
              No hay patrimonios registrados. Use el botón "Agregar Patrimonios"
              para comenzar.
            </p>
          </div>

          <!-- Cada patrimonio -->
          <div
            v-for="(patrimonio, index) in patrimonios"
            :key="index"
            class="border border-gray-300 rounded p-4 space-y-4"
          >
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-secondary font-bold">
                {{ patrimonio.tipo }} {{ index + 1 }}
              </h3>
              <button
                v-if="patrimonios.length > 1"
                @click="eliminarPatrimonio(index)"
                type="button"
                class="px-2 py-1 bg-red-500 text-blacke rounded text-sm"
              >
                Eliminar
              </button>
            </div>

            <!-- Campos comunes -->
            <div class="grid grid-cols-3 gap-4 text-black">
              <div>
                <label class="font-semibold text-sm mb-1"
                  >Tipo de Patrimonio
                  <span class="text-red-500">(*)</span></label
                >
                <select
                  v-model="patrimonio.tipo"
                  class="w-full px-3 py-1 border border-gray-300 rounded"
                  required
                >
                  <option value="">--Seleccione--</option>
                  <option value="Vivienda">Vivienda</option>
                  <option value="Local comercial">Local comercial</option>
                  <option value="Otro inmueble">Otro inmueble</option>
                  <option value="Vehículo de uso particular">
                    Vehículo de uso particular
                  </option>
                  <option value="Vehículo para alquiler/trabajo">
                    Vehículo para alquiler/trabajo
                  </option>
                </select>
              </div>
              <div>
                <label class="font-semibold text-sm mb-1"
                  >¿Inscrito en registros públicos?
                  <span class="text-red-500">(*)</span></label
                >
                <select
                  v-model="patrimonio.inscrito"
                  class="w-full px-3 py-1 border border-gray-300 rounded"
                  required
                >
                  <option value="">--Seleccione--</option>
                  <option value="Si">Sí</option>
                  <option value="No">No</option>
                </select>
              </div>
              <div>
                <label class="font-semibold text-sm mb-1"
                  >Valor aproximado (S/.)
                  <span class="text-red-500">(*)</span></label
                >
                <input
                  type="number"
                  v-model="patrimonio.valorAproximado"
                  class="w-full px-3 py-1 border border-gray-300 rounded"
                  min="0"
                  step="0.01"
                  required
                />
              </div>
            </div>

            <!-- Campos específicos para inmuebles -->
            <div
              v-if="esInmueble(patrimonio.tipo)"
              class="grid grid-cols-1 gap-4"
            >
              <div>
                <label class="font-semibold text-black text-sm mb-1"
                  >Dirección de ubicación del inmueble
                  <span class="text-red-500">(*)</span></label
                >
                <input
                  type="text"
                  v-model="patrimonio.direccion"
                  class="w-full px-3 py-1 border border-gray-300 rounded"
                  placeholder="Ej: Calle Principal 123, Distrito, Provincia"
                  required
                />
              </div>
            </div>

            <!-- Campos específicos para vehículos -->
            <div
              v-if="esVehiculo(patrimonio.tipo)"
              class="grid grid-cols-3 gap-4"
            >
              <div>
                <label class="font-semibold text-black text-sm mb-1"
                  >Tipo de Vehículo <span class="text-red-500">(*)</span></label
                >
                <select
                  v-model="patrimonio.tipoVehiculo"
                  class="w-full px-3 py-1 border text-black border-gray-300 rounded"
                  required
                >
                  <option value="">--Seleccione--</option>
                  <option value="Automóvil">Automóvil</option>
                  <option value="Camioneta">Camioneta</option>
                  <option value="Motocicleta">Motocicleta</option>
                  <option value="Motocar">Motocar</option>
                  <option value="Camión">Camión</option>
                  <option value="Otro">Otro</option>
                </select>
              </div>
              <div>
                <label class="font-semibold text-black text-sm mb-1"
                  >Número de Placa <span class="text-red-500">(*)</span></label
                >
                <input
                  type="text"
                  v-model="patrimonio.placa"
                  class="w-full px-3 py-1 border border-gray-300 rounded"
                  placeholder="Ej: ABC-1234"
                  required
                />
              </div>
              <div>
                <label class="font-semibold text-black text-sm mb-1"
                  >Año <span class="text-red-500">(*)</span></label
                >
                <input
                  type="number"
                  v-model="patrimonio.anio"
                  class="w-full px-3 py-1 border border-gray-300 rounded"
                  min="1900"
                  max="2100"
                  required
                />
              </div>
            </div>
          </div>

          <!-- Botón para agregar patrimonio -->
          <button
            @click="agregarPatrimonio"
            type="button"
            class="px-4 py-2 bg-primary text-blacke rounded"
          >
            + Agregar Patrimonios
          </button>

          <div class="w-full flex justify-end items-center mt-5">
            <button
              type="submit"
              class="px-4 py-1 bg-terciary text-blacke rounded"
            >
              Grabar
            </button>
          </div>
        </div>
      </template>
    </Information>
    <div class="flex justify-center items-center">
      <BackNext />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

interface Patrimonio {
  tipo: string;
  inscrito: string;
  valorAproximado: number | string;
  // Para inmuebles
  direccion?: string;
  // Para vehículos
  tipoVehiculo?: string;
  placa?: string;
  anio?: number | string;
}

const patrimonios = ref<Patrimonio[]>([]);

const agregarPatrimonio = () => {
  patrimonios.value.push({
    tipo: "",
    inscrito: "",
    valorAproximado: "",
    direccion: "",
    tipoVehiculo: "",
    placa: "",
    anio: "",
  });
};

const eliminarPatrimonio = (index: number) => {
  if (patrimonios.value.length > 1) {
    patrimonios.value.splice(index, 1);
  }
};

const esInmueble = (tipo: string): boolean => {
  return ["Vivienda", "Local comercial", "Otro inmueble"].includes(tipo);
};

const esVehiculo = (tipo: string): boolean => {
  return [
    "Vehículo de uso particular",
    "Vehículo para alquiler/trabajo",
  ].includes(tipo);
};
</script>

<style scoped></style>
