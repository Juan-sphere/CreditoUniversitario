<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header fijo -->
    <Header />

    <!-- Contenido principal -->
    <div class="pt-20 px-8 py-8 max-w-7xl mx-auto">
      <!-- Botón volver -->
      <button
        @click="volver"
        class="flex items-center gap-2 text-blue-600 hover:text-blue-700 mb-6"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 19l-7-7 7-7"
          />
        </svg>
        Volver a Postulaciones
      </button>

      <!-- Loading -->
      <div v-if="loading" class="flex items-center justify-center py-20">
        <div class="flex items-center gap-3">
          <svg
            class="animate-spin h-8 w-8 text-blue-600"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>
          <span class="text-gray-600">Cargando postulación...</span>
        </div>
      </div>

      <!-- Contenido -->
      <div v-else-if="postulacion" class="space-y-6">
        <!-- Encabezado con código y estado -->
        <div class="bg-white rounded-lg shadow-lg p-6">
          <div class="flex items-center justify-between mb-4">
            <div>
              <h1 class="text-2xl font-bold text-gray-900">
                {{ postulacion.codigo_postulacion }}
              </h1>
              <p class="text-sm text-gray-500">
                Postulación N° {{ postulacion.numero_correlativo }}
              </p>
            </div>
            <div class="flex items-center gap-3">
              <span
                :class="estadoBadge(postulacion.resultado)"
                class="px-4 py-2 rounded-full text-sm font-medium"
              >
                {{ estadoTexto(postulacion.resultado) }}
              </span>
            </div>
          </div>

          <div class="grid grid-cols-3 gap-4 pt-4 border-t">
            <div>
              <p class="text-xs text-gray-500 mb-1">Fecha de postulación</p>
              <p class="font-medium">
                {{ formatearFecha(postulacion.fecha_postulacion) }}
              </p>
            </div>
            <div>
              <p class="text-xs text-gray-500 mb-1">Fecha límite</p>
              <p
                class="font-medium"
                :class="fechaLimiteColor(postulacion.fecha_limite_evaluacion)"
              >
                {{ formatearFecha(postulacion.fecha_limite_evaluacion) }}
              </p>
            </div>
            <div>
              <p class="text-xs text-gray-500 mb-1">Evaluador asignado</p>
              <p class="font-medium">
                {{ postulacion.evaluador_nombre || "Sin asignar" }}
              </p>
            </div>
          </div>
        </div>

        <!-- Resumen de Datos del Postulante -->
        <div class="bg-white rounded-lg shadow p-6">
          <h2 class="text-xl font-bold text-gray-900 mb-4">Resumen de Datos</h2>
          <div class="grid grid-cols-2 md:grid-cols-3 gap-6">
            <div>
              <p class="text-sm text-gray-500 mb-1">Nombre Completo</p>
              <p class="font-medium text-gray-900">
                {{ postulacion.nombre_completo }}
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-500 mb-1">DNI</p>
              <p class="font-medium text-gray-900">{{ postulacion.dni }}</p>
            </div>
            <div>
              <p class="text-sm text-gray-500 mb-1">Edad</p>
              <p class="font-medium text-gray-900">
                {{ datos.edad || "N/A" }} años
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-500 mb-1">Universidad</p>
              <p class="font-medium text-gray-900">
                {{ postulacion.universidad }}
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-500 mb-1">Teléfono</p>
              <p class="font-medium text-gray-900">
                {{ datos.telefono || "N/A" }}
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-500 mb-1">Email Universidad</p>
              <p class="font-medium text-gray-900">
                {{ datos.mail_universidad || "N/A" }}
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-500 mb-1">
                Monto Mensual Universidad
              </p>
              <p class="font-medium text-gray-900">
                S/ {{ formatearMonto(datos.monto_mensual_universidad) }}
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-500 mb-1">Cuota Estimada (30%)</p>
              <p class="font-medium text-blue-600">
                S/ {{ formatearMonto(datos.monto_cuota_estimada) }}
              </p>
            </div>
            <div>
              <p class="text-sm text-gray-500 mb-1">Vive con</p>
              <p class="font-medium text-gray-900">
                {{ datos.vive_con || "N/A" }}
              </p>
            </div>
          </div>
        </div>

        <!-- Balance Presupuestario -->
        <div class="bg-white rounded-lg shadow p-6">
          <h2 class="text-xl font-bold text-gray-900 mb-4">
            Balance Presupuestario
          </h2>

          <div class="grid md:grid-cols-2 gap-6 mb-6">
            <!-- Ingresos -->
            <div>
              <h3 class="font-semibold text-green-700 mb-3">Ingresos</h3>
              <div v-if="datos.detalle_ingresos" class="space-y-2">
                <div
                  v-for="(ingreso, idx) in datos.detalle_ingresos"
                  :key="idx"
                  class="flex justify-between text-sm"
                >
                  <span class="text-gray-600">{{ ingreso.concepto }}</span>
                  <span class="font-medium text-green-600"
                    >S/ {{ formatearMonto(ingreso.monto) }}</span
                  >
                </div>
                <div class="pt-2 border-t flex justify-between font-bold">
                  <span>Total Ingresos:</span>
                  <span class="text-green-600"
                    >S/ {{ calcularTotalIngresos() }}</span
                  >
                </div>
              </div>
              <p v-else class="text-sm text-gray-500">Sin datos</p>
            </div>

            <!-- Gastos -->
            <div>
              <h3 class="font-semibold text-red-700 mb-3">Gastos</h3>
              <div v-if="datos.detalle_gastos" class="space-y-2">
                <div
                  v-for="(gasto, idx) in datos.detalle_gastos"
                  :key="idx"
                  class="flex justify-between text-sm"
                >
                  <span class="text-gray-600">{{ gasto.concepto }}</span>
                  <span class="font-medium text-red-600"
                    >S/ {{ formatearMonto(gasto.monto) }}</span
                  >
                </div>
                <div class="pt-2 border-t flex justify-between font-bold">
                  <span>Total Gastos:</span>
                  <span class="text-red-600"
                    >S/ {{ calcularTotalGastos() }}</span
                  >
                </div>
              </div>
              <p v-else class="text-sm text-gray-500">Sin datos</p>
            </div>
          </div>

          <!-- Balance Final -->
          <div class="bg-gray-50 rounded-lg p-4">
            <div class="flex justify-between items-center">
              <span class="text-lg font-semibold">Balance Final:</span>
              <span
                :class="balanceColor(datos.balance_final)"
                class="text-xl font-bold"
              >
                S/ {{ formatearMonto(datos.balance_final) }}
              </span>
            </div>
          </div>

          <!-- Observaciones económicas -->
          <div
            v-if="datos.deficit_como_cierra"
            class="mt-4 bg-blue-50 border border-blue-200 rounded-lg p-4"
          >
            <p class="text-sm font-medium text-blue-900 mb-1">
              Cómo cierran el déficit:
            </p>
            <p class="text-sm text-blue-800">{{ datos.deficit_como_cierra }}</p>
          </div>

          <div
            v-if="datos.observaciones_economia"
            class="mt-3 bg-yellow-50 border border-yellow-200 rounded-lg p-4"
          >
            <p class="text-sm font-medium text-yellow-900 mb-1">
              Observaciones adicionales:
            </p>
            <p class="text-sm text-yellow-800">
              {{ datos.observaciones_economia }}
            </p>
          </div>
        </div>

        <!-- Personas que Aportan -->
        <div
          v-if="datos.personas_aportan && datos.personas_aportan.length > 0"
          class="bg-white rounded-lg shadow p-6"
        >
          <h2 class="text-xl font-bold text-gray-900 mb-4">
            Personas que Aportan
          </h2>
          <div class="overflow-x-auto">
            <table class="w-full">
              <thead class="bg-gray-50">
                <tr>
                  <th
                    class="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase"
                  >
                    Nombre
                  </th>
                  <th
                    class="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase"
                  >
                    DNI
                  </th>
                  <th
                    class="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase"
                  >
                    Aporte Mensual
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y">
                <tr v-for="(persona, idx) in datos.personas_aportan" :key="idx">
                  <td class="px-4 py-3 text-sm">{{ persona.nombre }}</td>
                  <td class="px-4 py-3 text-sm">{{ persona.dni }}</td>
                  <td class="px-4 py-3 text-sm text-right font-medium">
                    S/ {{ formatearMonto(persona.aporte) }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Documentos -->
        <div
          v-if="datos.documentos && datos.documentos.length > 0"
          class="bg-white rounded-lg shadow p-6"
        >
          <h2 class="text-xl font-bold text-gray-900 mb-4">
            Documentos Adjuntos
          </h2>
          <div class="grid md:grid-cols-2 gap-3">
            <a
              v-for="(doc, idx) in datos.documentos"
              :key="idx"
              :href="doc.url"
              target="_blank"
              class="flex items-center gap-3 p-3 border border-gray-200 rounded-lg hover:bg-gray-50 transition"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 text-blue-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                />
              </svg>
              <div>
                <p class="text-sm font-medium text-gray-900">
                  {{ doc.nombre }}
                </p>
                <p class="text-xs text-gray-500">Click para ver</p>
              </div>
            </a>
          </div>
        </div>

        <!-- Análisis del Evaluador -->
        <div class="bg-white rounded-lg shadow p-6">
          <h2 class="text-xl font-bold text-gray-900 mb-4">
            Análisis del Evaluador
          </h2>

          <div class="space-y-4">
            <!-- Observaciones -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2"
                >Observaciones</label
              >
              <textarea
                v-model="analisis.observaciones"
                rows="4"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Escribe tus observaciones sobre la postulación..."
              ></textarea>
            </div>

            <!-- Informe Final -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2"
                >Informe Final</label
              >
              <textarea
                v-model="analisis.informe_final"
                rows="5"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Redacta el informe final de evaluación..."
              ></textarea>
            </div>

            <!-- Conclusión -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2"
                >Conclusión</label
              >
              <textarea
                v-model="analisis.conclusion"
                rows="3"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Conclusión de la evaluación..."
              ></textarea>
            </div>

            <!-- Cargar archivos -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2"
                >Archivos del Analista</label
              >
              <input
                type="file"
                multiple
                @change="cargarArchivos"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <p class="text-xs text-gray-500 mt-1">
                Puedes cargar múltiples archivos (informes, evaluaciones, etc.)
              </p>
            </div>
          </div>
        </div>

        <!-- Botones de Acción -->
        <div class="bg-white rounded-lg shadow p-6">
          <h2 class="text-xl font-bold text-gray-900 mb-4">
            Conclusión de Evaluación
          </h2>

          <div class="flex gap-4">
            <button
              @click="aprobar"
              :disabled="guardando"
              class="flex-1 bg-green-600 text-white px-6 py-4 rounded-lg font-semibold hover:bg-green-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="!guardando">✓ APROBAR POSTULACIÓN</span>
              <span v-else>Guardando...</span>
            </button>

            <button
              @click="denegar"
              :disabled="guardando"
              class="flex-1 bg-red-600 text-white px-6 py-4 rounded-lg font-semibold hover:bg-red-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="!guardando">✗ DENEGAR POSTULACIÓN</span>
              <span v-else>Guardando...</span>
            </button>

            <button
              @click="guardarBorrador"
              :disabled="guardando"
              class="bg-gray-200 text-gray-700 px-6 py-4 rounded-lg font-semibold hover:bg-gray-300 transition disabled:opacity-50"
            >
              Guardar Borrador
            </button>
          </div>

          <p class="text-xs text-gray-500 mt-3 text-center">
            Al aprobar o denegar, se enviará una notificación al estudiante
          </p>
        </div>
      </div>

      <!-- Error -->
      <div
        v-else
        class="bg-red-50 border border-red-200 rounded-lg p-8 text-center"
      >
        <p class="text-red-800 font-medium">No se pudo cargar la postulación</p>
        <button @click="volver" class="mt-4 text-blue-600 hover:underline">
          Volver a Postulaciones
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

// Estados
const loading = ref(true);
const guardando = ref(false);
const postulacion = ref<any>(null);
const datos = ref<any>({});
const analisis = ref({
  observaciones: "",
  informe_final: "",
  conclusion: "",
});

// Cargar datos
onMounted(async () => {
  await cargarPostulacion();
});

async function cargarPostulacion() {
  loading.value = true;
  try {
    const id = route.params.id;

    // TODO: Implementar endpoint GET /postulaciones/:id
    // Por ahora datos de ejemplo
    postulacion.value = {
      id: 1,
      numero_correlativo: 1,
      codigo_postulacion: "250220001-UNI",
      nombre_completo: "Juan Carlos García López",
      dni: "12345678",
      fecha_postulacion: "2025-02-20T10:30:00",
      universidad: "Universidad Nacional de Ingeniería",
      evaluador_nombre: "Juan Evaluador López",
      fecha_limite_evaluacion: "2025-02-22T10:30:00",
      resultado: "no_revisada",
    };

    datos.value = {
      edad: 22,
      telefono: "987654321",
      mail_universidad: "juan.garcia@uni.edu.pe",
      monto_mensual_universidad: 2500.0,
      monto_cuota_estimada: 750.0,
      vive_con: "Padre y Madre",
      detalle_ingresos: [
        { concepto: "Sueldo padre", monto: 3000 },
        { concepto: "Sueldo madre", monto: 2500 },
      ],
      detalle_gastos: [
        { concepto: "Alimentación", monto: 1200 },
        { concepto: "Servicios", monto: 500 },
        { concepto: "Transporte", monto: 300 },
      ],
      balance_final: 3500,
      deficit_como_cierra: "Con ahorros familiares",
      observaciones_economia: "Familia estable económicamente",
      personas_aportan: [
        { nombre: "Carlos García", dni: "11111111", aporte: 3000 },
        { nombre: "María López", dni: "22222222", aporte: 2500 },
      ],
      documentos: [
        { nombre: "DNI.pdf", url: "#" },
        { nombre: "Recibo_Luz.pdf", url: "#" },
      ],
    };

    // Cargar análisis existente si ya fue evaluado
    if (postulacion.value.observaciones) {
      analisis.value.observaciones = postulacion.value.observaciones;
    }
  } catch (error) {
    console.error("Error cargando postulación:", error);
  } finally {
    loading.value = false;
  }
}

function volver() {
  router.push("/analista");
}

function cargarArchivos(event: Event) {
  const files = (event.target as HTMLInputElement).files;
  console.log("Archivos seleccionados:", files);
  // TODO: Subir archivos al servidor
}

async function aprobar() {
  if (!confirm("¿Estás seguro de aprobar esta postulación?")) return;

  guardando.value = true;
  try {
    // TODO: POST /postulaciones/:id/evaluar
    console.log("Aprobando...", analisis.value);
    alert("Postulación APROBADA");
    router.push("/analista");
  } catch (error) {
    console.error("Error:", error);
  } finally {
    guardando.value = false;
  }
}

async function denegar() {
  if (!confirm("¿Estás seguro de denegar esta postulación?")) return;

  guardando.value = true;
  try {
    // TODO: POST /postulaciones/:id/evaluar
    console.log("Denegando...", analisis.value);
    alert("Postulación DENEGADA");
    router.push("/analista");
  } catch (error) {
    console.error("Error:", error);
  } finally {
    guardando.value = false;
  }
}

async function guardarBorrador() {
  guardando.value = true;
  try {
    // TODO: PATCH /postulaciones/:id
    console.log("Guardando borrador...", analisis.value);
    alert("Borrador guardado");
  } catch (error) {
    console.error("Error:", error);
  } finally {
    guardando.value = false;
  }
}

// Helpers
function formatearFecha(fecha: string) {
  return new Date(fecha).toLocaleString("es-PE", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function formatearMonto(monto: number | null | undefined) {
  return (monto || 0).toFixed(2);
}

function calcularTotalIngresos() {
  if (!datos.value.detalle_ingresos) return "0.00";
  const total = datos.value.detalle_ingresos.reduce(
    (sum: number, i: any) => sum + i.monto,
    0,
  );
  return total.toFixed(2);
}

function calcularTotalGastos() {
  if (!datos.value.detalle_gastos) return "0.00";
  const total = datos.value.detalle_gastos.reduce(
    (sum: number, g: any) => sum + g.monto,
    0,
  );
  return total.toFixed(2);
}

function estadoBadge(estado: string) {
  const badges: Record<string, string> = {
    no_revisada: "bg-yellow-100 text-yellow-800",
    aprobado: "bg-green-100 text-green-800",
    denegado: "bg-red-100 text-red-800",
  };
  return badges[estado] || "bg-gray-100 text-gray-800";
}

function estadoTexto(estado: string) {
  const textos: Record<string, string> = {
    no_revisada: "No Revisada",
    aprobado: "Aprobado",
    denegado: "Denegado",
  };
  return textos[estado] || estado;
}

function fechaLimiteColor(fecha: string) {
  const limite = new Date(fecha);
  const ahora = new Date();
  const horasRestantes =
    (limite.getTime() - ahora.getTime()) / (1000 * 60 * 60);

  if (horasRestantes < 0) return "text-red-600";
  if (horasRestantes < 24) return "text-orange-600";
  return "text-gray-900";
}

function balanceColor(balance: number) {
  if (balance < 0) return "text-red-600";
  if (balance > 0) return "text-green-600";
  return "text-gray-900";
}
</script>
