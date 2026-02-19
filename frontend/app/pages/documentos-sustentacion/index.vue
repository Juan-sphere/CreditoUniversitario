<template>
  <div class="w-full">
    <!-- Título y descripción -->
    <h1 class="text-2xl font-bold mb-2">Documentos de sustentación</h1>

    <!-- Información -->
    <Information title="DOCUMENTOS REQUERIDOS">
      <template #information>
        <div class="bg-blue-50 border border-blue-200 p-4 rounded mb-4">
          <p class="text-gray-700">
            Selecciona los documentos que estás adjuntando. Todos los documentos
            deben ser claros y legibles.
          </p>
        </div>

        <!-- Checklist de documentos -->
        <div class="pl-2">
          <div class="border-b pb-2">
            <label
              class="flex items-start cursor-pointer hover:bg-gray-50 p-2 rounded"
            >
              <input
                type="checkbox"
                v-model="selectedDocuments"
                value="ingresos"
                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400"
              />
              <span class="ml-3">
                <span class="font-semibold text-gray-800"
                  >Documentos de sustento de ingresos</span
                >
                <p class="text-sm text-gray-600">
                  Del postulante y de los miembros del núcleo familiar que
                  contribuyen a la economía familiar
                </p>
              </span>
            </label>
          </div>

          <div class="border-b pb-2">
            <label
              class="flex items-start cursor-pointer hover:bg-gray-50 p-2 rounded"
            >
              <input
                type="checkbox"
                v-model="selectedDocuments"
                value="boletas"
                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400"
              />
              <span class="ml-3">
                <span class="font-semibold text-gray-800"
                  >Boletas de haberes o Ingresos</span
                >
                <p class="text-sm text-gray-600">De los tres últimos meses</p>
              </span>
            </label>
          </div>

          <div class="border-b pb-2">
            <label
              class="flex items-start cursor-pointer hover:bg-gray-50 p-2 rounded"
            >
              <input
                type="checkbox"
                v-model="selectedDocuments"
                value="pdt"
                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400"
              />
              <span class="ml-3">
                <span class="font-semibold text-gray-800"
                  >PDT SUNAT completo (3 hojas)</span
                >
                <p class="text-sm text-gray-600">
                  De los tres últimos meses anteriores a la fecha actual como
                  persona natural con negocio
                </p>
              </span>
            </label>
          </div>

          <div class="border-b pb-2">
            <label
              class="flex items-start cursor-pointer hover:bg-gray-50 p-2 rounded"
            >
              <input
                type="checkbox"
                v-model="selectedDocuments"
                value="tributario"
                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400"
              />
              <span class="ml-3">
                <span class="font-semibold text-gray-800"
                  >Reporte Tributario del último año</span
                >
                <p class="text-sm text-gray-600">SUNAT</p>
              </span>
            </label>
          </div>

          <div class="border-b pb-2">
            <label
              class="flex items-start cursor-pointer hover:bg-gray-50 p-2 rounded"
            >
              <input
                type="checkbox"
                v-model="selectedDocuments"
                value="rus"
                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400"
              />
              <span class="ml-3">
                <span class="font-semibold text-gray-800"
                  >Vouchers de pago del RUS SUNAT</span
                >
                <p class="text-sm text-gray-600">Últimos pagos realizados</p>
              </span>
            </label>
          </div>

          <div class="border-b pb-2">
            <label
              class="flex items-start cursor-pointer hover:bg-gray-50 p-2 rounded"
            >
              <input
                type="checkbox"
                v-model="selectedDocuments"
                value="terceros"
                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400"
              />
              <span class="ml-3">
                <span class="font-semibold text-gray-800"
                  >Reporte Tributario para Terceros SUNAT (actual)</span
                >
                <p class="text-sm text-gray-600">
                  Información fiscal actualizada
                </p>
              </span>
            </label>
          </div>

          <div class="border-b pb-2">
            <label
              class="flex items-start cursor-pointer hover:bg-gray-50 p-2 rounded"
            >
              <input
                type="checkbox"
                v-model="selectedDocuments"
                value="honorarios"
                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400"
              />
              <span class="ml-3">
                <span class="font-semibold text-gray-800"
                  >Reporte SUNAT de Recibos por Honorarios Electrónicos</span
                >
                <p class="text-sm text-gray-600">
                  De los últimos seis meses anteriores a la fecha actual
                </p>
              </span>
            </label>
          </div>

          <div class="pb-2">
            <label
              class="flex items-start cursor-pointer hover:bg-gray-50 p-2 rounded"
            >
              <input
                type="checkbox"
                v-model="selectedDocuments"
                value="servicio"
                class="mt-1 w-4 h-4 text-cyan-400 rounded focus:ring-cyan-400"
              />
              <span class="ml-3">
                <span class="font-semibold text-gray-800"
                  >Recibo de un servicio</span
                >
                <p class="text-sm text-gray-600">
                  Del domicilio declarado como vivienda (luz, agua, internet,
                  gas)
                </p>
              </span>
            </label>
          </div>
        </div>

        <!-- Resumen de selección -->
        <div class="mt-6 p-4 h-full bg-gray-100 rounded">
          <p class="text-sm font-semibold text-gray-700">
            Documentos seleccionados:
            <span class="text-cyan-400">{{ selectedDocuments.length }}</span>
          </p>
        </div>

        <!-- Botón de cargar -->
        <div class="">
          <button
            @click="handleUploadDocuments"
            class="w-full px-4 py-3 bg-cyan-400 text-white rounded font-semibold hover:bg-cyan-500 transition-colors"
          >
            📎 Cargar documentos seleccionados
          </button>
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

const selectedDocuments = ref<string[]>([]);

const handleUploadDocuments = () => {
  if (selectedDocuments.value.length === 0) {
    alert("Por favor selecciona al menos un documento para cargar");
    return;
  }

  console.log("Documentos seleccionados:", selectedDocuments.value);
  alert(`Documentos seleccionados: ${selectedDocuments.value.join(", ")}`);
};
</script>

<style scoped></style>
