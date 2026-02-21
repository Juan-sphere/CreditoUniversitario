<template>
  <div class="w-full">
    <!-- Loading Spinner mientras carga datos -->
    <div v-if="cargando" class="flex justify-center items-center h-96">
      <LoadingSpinner />
    </div>

    <!-- Contenido principal -->
    <div v-else>
      <!-- Título y descripción -->
      <h1 class="text-2xl font-bold mb-2">Documentos de sustentación</h1>

      <!-- Información -->
      <Information title="DOCUMENTOS REQUERIDOS">
        <template #information>
          <div class="bg-blue-50 border border-blue-200 p-4 rounded mb-4">
            <p class="text-gray-700">
              Selecciona los documentos que estás adjuntando. Todos los
              documentos deben ser claros y legibles.
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

          <!-- Input file oculto -->
          <input
            ref="fileInput"
            type="file"
            multiple
            accept=".pdf,.doc,.docx,.jpg,.jpeg,.png"
            style="display: none"
            @change="manejarSeleccionArchivos"
          />

          <!-- Resumen de selección -->
          <div class="mt-6 p-4 h-full bg-gray-100 rounded">
            <p class="text-sm font-semibold text-gray-700">
              Documentos seleccionados:
              <span class="text-cyan-400">{{ selectedDocuments.length }}</span>
            </p>
            <p class="text-xs text-gray-600 mt-2">
              Archivos cargados: {{ documentos.length }}
            </p>
          </div>

          <!-- Botón de cargar -->
          <div class="">
            <button
              @click="seleccionarArchivos"
              :disabled="selectedDocuments.length === 0 || cargandoArchivos"
              class="w-full px-4 py-3 bg-cyan-400 text-white rounded font-semibold hover:bg-cyan-500 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{
                cargandoArchivos
                  ? "📎 Cargando documentos..."
                  : "📎 Cargar documentos seleccionados"
              }}
            </button>
          </div>

          <!-- Lista de archivos cargados -->
          <div
            v-if="documentos.length > 0"
            class="mt-6 p-4 bg-green-50 border border-green-200 rounded"
          >
            <h3 class="font-semibold text-green-800 mb-2">
              ✓ Documentos cargados:
            </h3>
            <ul class="space-y-1">
              <li
                v-for="archivo in documentos"
                :key="archivo.id"
                class="text-sm text-green-700"
              >
                • {{ archivo.tipo_documento }} - {{ archivo.nombre_original }}
              </li>
            </ul>
          </div>
        </template>
      </Information>

      <div class="flex justify-center items-center">
        <BackNext />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { toast } from "vue3-toastify";
import Information from "~/components/Information.vue";
import BackNext from "~/components/BackNext.vue";
import LoadingSpinner from "~/components/LoadingSpinner.vue";
import { useRequiredDocuments } from "~/composables/useRequiredDocuments";

const {
  documentos,
  cargando,
  cargandoArchivos,
  cargarDocumentos,
  crearDocumento,
} = useRequiredDocuments();

const selectedDocuments = ref<string[]>([]);
const fileInput = ref<HTMLInputElement | null>(null);

// Seleccionar archivos
const seleccionarArchivos = () => {
  if (fileInput.value) {
    fileInput.value.click();
  }
};

// Manejar selección de archivos
const manejarSeleccionArchivos = async (event: Event) => {
  const target = event.target as HTMLInputElement;
  const files = target.files;

  if (!files || files.length === 0) {
    return;
  }

  if (selectedDocuments.value.length === 0) {
    toast.error("Por favor selecciona al menos un tipo de documento");
    return;
  }

  try {
    // Procesar cada archivo
    for (let i = 0; i < files.length; i++) {
      const file = files.item(i);
      if (!file) continue;

      const tipoDocumento =
        selectedDocuments.value[i] || selectedDocuments.value[0];
      if (!tipoDocumento) {
        toast.warning("Por favor selecciona un tipo de documento");
        continue;
      }

      // Crear documento en backend
      await crearDocumento(tipoDocumento, file.name, file.type, file.size);
    }

    selectedDocuments.value = [];
    cargarDocumentos();

    // Limpiar input
    if (fileInput.value) {
      fileInput.value.value = "";
    }
  } catch (error: any) {
    console.error("Error al cargar archivos:", error);
    toast.error(error.data?.detail || "Error al cargar los documentos");
  }
};

onMounted(() => {
  cargarDocumentos();
});
</script>

<style scoped></style>
