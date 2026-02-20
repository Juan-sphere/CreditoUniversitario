<template>
  <!-- Contenido principal -->
  <div class="pt-20 px-8 py-8">
    <!-- Título y controles -->
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-3xl font-bold text-gray-900">Postulaciones</h1>

      <!-- Selector de filas por página -->
      <div class="flex items-center gap-2">
        <label class="text-sm text-gray-600">Mostrar:</label>
        <select
          v-model="filasPorPagina"
          class="border border-gray-300 rounded px-3 py-1 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option :value="10">10 filas</option>
          <option :value="25">25 filas</option>
          <option :value="50">50 filas</option>
          <option :value="100">100 filas</option>
        </select>
      </div>
    </div>

    <!-- Filtros -->
    <div class="mb-6">
      <h2 class="text-lg font-semibold mb-4">Filtros</h2>
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <!-- Nombre -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Nombre</label
          >
          <input
            v-model="filtros.nombre"
            type="text"
            placeholder="Buscar por nombre..."
            class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <!-- DNI -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >DNI</label
          >
          <input
            v-model="filtros.dni"
            type="text"
            placeholder="12345678"
            maxlength="8"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <!-- Universidad -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Universidad</label
          >
          <select
            v-model="filtros.universidad"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Todas</option>
            <option v-for="uni in universidades" :key="uni" :value="uni">
              {{ uni }}
            </option>
          </select>
        </div>

        <!-- Resultado -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Resultado</label
          >
          <select
            v-model="filtros.resultado"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Todos</option>
            <option value="no_revisada">No revisada</option>
            <option value="aprobado">Aprobado</option>
            <option value="denegado">Denegado</option>
          </select>
        </div>

        <!-- Evaluador -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Evaluador</label
          >
          <select
            v-model="filtros.evaluador"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Todos</option>
            <option
              v-for="evaluador in evaluadores"
              :key="evaluador.id"
              :value="evaluador.id"
            >
              {{ evaluador.nombres }}
            </option>
          </select>
        </div>

        <!-- Proceso -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Proceso</label
          >
          <select
            v-model="filtros.proceso"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Todos</option>
            <option value="evaluacion_culminada">Evaluación culminada</option>
            <option value="contrato_enviado">Contrato enviado</option>
            <option value="contrato_firmado">Contrato firmado</option>
            <option value="matricula_habilitada">Matrícula habilitada</option>
          </select>
        </div>

        <!-- Fecha Desde -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Fecha Desde</label
          >
          <input
            v-model="filtros.fechaDesde"
            type="date"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <!-- Fecha Hasta -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Fecha Hasta</label
          >
          <input
            v-model="filtros.fechaHasta"
            type="date"
            class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
      </div>

      <!-- Botones -->
      <div class="mt-4 flex gap-2">
        <button
          @click="aplicarFiltros"
          class="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm hover:bg-blue-700 transition"
        >
          Aplicar Filtros
        </button>
        <button
          @click="limpiarFiltros"
          class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg text-sm hover:bg-gray-300 transition"
        >
          Limpiar
        </button>
      </div>
    </div>

    <!-- Tabla de postulaciones -->
    <div class="overflow-x-auto">
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-50 border-b">
            <tr>
              <th class="px-4 py-3 text-left">
                <input type="checkbox" @change="seleccionarTodos" />
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                N°
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                Código
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                Nombre
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                DNI
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                Fecha/Hora
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                Universidad
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                Evaluador
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                Fecha Límite
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                Resultado
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase"
              >
                Proceso
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <!-- Loading -->
            <tr v-if="loading">
              <td colspan="11" class="px-4 py-8 text-center text-gray-500">
                <div class="flex items-center justify-center gap-2">
                  <svg
                    class="animate-spin h-5 w-5 text-blue-600"
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
                  Cargando postulaciones...
                </div>
              </td>
            </tr>

            <!-- Sin resultados -->
            <tr v-else-if="postulaciones.length === 0">
              <td colspan="11" class="px-4 py-8 text-center text-gray-500">
                No hay postulaciones que mostrar
              </td>
            </tr>

            <!-- Filas de datos -->
            <tr
              v-else
              v-for="post in postulaciones"
              :key="post.id"
              @click="verDetalle(post.id)"
              class="hover:bg-gray-50 cursor-pointer transition"
            >
              <td class="px-4 py-3" @click.stop>
                <input type="checkbox" v-model="post.seleccionado" />
              </td>
              <td class="px-4 py-3 text-sm text-gray-900">
                {{ post.numero_correlativo }}
              </td>
              <td class="px-4 py-3 text-sm font-medium text-blue-600">
                {{ post.codigo_postulacion }}
              </td>
              <td class="px-4 py-3 text-sm text-gray-900">
                {{ post.nombre_completo }}
              </td>
              <td class="px-4 py-3 text-sm text-gray-900">{{ post.dni }}</td>
              <td class="px-4 py-3 text-sm text-gray-500">
                {{ formatearFecha(post.fecha_postulacion) }}
              </td>
              <td class="px-4 py-3 text-sm text-gray-900">
                {{ post.universidad }}
              </td>
              <td class="px-4 py-3 text-sm text-gray-500">
                {{ post.evaluador_nombre || "Sin asignar" }}
              </td>
              <td
                class="px-4 py-3 text-sm"
                :class="fechaLimiteClass(post.fecha_limite_evaluacion)"
              >
                {{ formatearFecha(post.fecha_limite_evaluacion) }}
              </td>
              <td class="px-4 py-3">
                <span
                  :class="resultadoBadge(post.resultado)"
                  class="px-2 py-1 text-xs rounded-full"
                >
                  {{ resultadoTexto(post.resultado) }}
                </span>
              </td>
              <td class="px-4 py-3" @click.stop>
                <select
                  v-model="post.proceso"
                  @change="actualizarProceso(post)"
                  class="text-sm border border-gray-300 rounded px-2 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="">Sin proceso</option>
                  <option value="evaluacion_culminada">
                    Evaluación culminada
                  </option>
                  <option value="contrato_enviado">Contrato enviado</option>
                  <option value="contrato_firmado">Contrato firmado</option>
                  <option value="matricula_habilitada">
                    Matrícula habilitada
                  </option>
                </select>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Paginación -->
    <div class="mt-4 flex items-center justify-between">
      <div class="text-sm text-gray-600">
        Mostrando {{ postulaciones.length }} de
        {{ totalPostulaciones }} postulaciones
      </div>
      <div class="flex gap-2">
        <!-- Aquí puedes agregar botones de paginación si lo necesitas -->
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

// ==================== INTERFACES ====================
interface Evaluador {
  id: number;
  nombres: string;
  correo: string;
}

interface Postulacion {
  id: number;
  numero_correlativo: number;
  codigo_postulacion: string;
  nombre_completo: string;
  dni: string;
  fecha_postulacion: string;
  universidad: string;
  evaluador_nombre: string | null;
  fecha_limite_evaluacion: string;
  resultado: string;
  proceso: string;
  seleccionado: boolean;
}

// ==================== ROUTER ====================
const router = useRouter();

// ==================== ESTADOS ====================
const loading = ref(false);
const filasPorPagina = ref(25);
const postulaciones = ref<Postulacion[]>([]);
const universidades = ref<string[]>([]);
const evaluadores = ref<Evaluador[]>([]);
const totalPostulaciones = ref(0);

// ==================== FILTROS ====================
const filtros = ref({
  nombre: "",
  dni: "",
  universidad: "",
  resultado: "",
  evaluador: "",
  proceso: "",
  fechaDesde: "",
  fechaHasta: "",
});

// ==================== LIFECYCLE ====================
onMounted(async () => {
  await cargarUniversidades();
  await cargarEvaluadores();
  await cargarPostulaciones();
});

// ==================== FUNCIONES DE CARGA ====================
async function cargarUniversidades() {
  try {
    const response = await fetch("http://localhost:5000/auth/universidades");
    const data = await response.json();
    universidades.value = data;
  } catch (error) {
    console.error("Error cargando universidades:", error);
  }
}

async function cargarEvaluadores() {
  try {
    const response = await fetch("http://localhost:5000/auth/analistas");
    const data = await response.json();
    evaluadores.value = data;
  } catch (error) {
    console.error("Error cargando evaluadores:", error);
  }
}

async function cargarPostulaciones() {
  loading.value = true;
  try {
    // TODO: Implementar endpoint /postulaciones con filtros
    // Por ahora datos de ejemplo
    postulaciones.value = [
      {
        id: 1,
        numero_correlativo: 1,
        codigo_postulacion: "250220001-UNI",
        nombre_completo: "Juan Carlos García López",
        dni: "12345678",
        fecha_postulacion: "2025-02-20T10:30:00",
        universidad: "Universidad Nacional de Ingeniería",
        evaluador_nombre: "Juan Evaluador",
        fecha_limite_evaluacion: "2025-02-22T10:30:00",
        resultado: "no_revisada",
        proceso: "",
        seleccionado: false,
      },
    ];
    totalPostulaciones.value = postulaciones.value.length;
  } catch (error) {
    console.error("Error cargando postulaciones:", error);
  } finally {
    loading.value = false;
  }
}

// ==================== FUNCIONES DE FILTROS ====================
function aplicarFiltros() {
  // TODO: Aplicar filtros a la consulta
  cargarPostulaciones();
}

function limpiarFiltros() {
  filtros.value = {
    nombre: "",
    dni: "",
    universidad: "",
    resultado: "",
    evaluador: "",
    proceso: "",
    fechaDesde: "",
    fechaHasta: "",
  };
  cargarPostulaciones();
}

// ==================== FUNCIONES DE SELECCIÓN ====================
function seleccionarTodos(event: Event) {
  const checked = (event.target as HTMLInputElement).checked;
  postulaciones.value.forEach((p) => (p.seleccionado = checked));
}

// ==================== NAVEGACIÓN ====================
function verDetalle(id: number) {
  router.push(`/analista/postulacion/${id}`);
}

// ==================== ACTUALIZACIÓN ====================
async function actualizarProceso(postulacion: Postulacion) {
  try {
    // TODO: Implementar endpoint PATCH /postulaciones/:id/proceso
    console.log("Actualizando proceso:", postulacion);
  } catch (error) {
    console.error("Error actualizando proceso:", error);
  }
}

// ==================== FORMATEO ====================
function formatearFecha(fecha: string) {
  const date = new Date(fecha);
  return date.toLocaleString("es-PE", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function fechaLimiteClass(fecha: string) {
  const limite = new Date(fecha);
  const ahora = new Date();
  const horasRestantes =
    (limite.getTime() - ahora.getTime()) / (1000 * 60 * 60);

  if (horasRestantes < 0) return "text-red-600 font-semibold";
  if (horasRestantes < 24) return "text-orange-600 font-semibold";
  return "text-gray-500";
}

function resultadoBadge(resultado: string) {
  const badges: Record<string, string> = {
    no_revisada: "bg-yellow-100 text-yellow-800",
    aprobado: "bg-green-100 text-green-800",
    denegado: "bg-red-100 text-red-800",
  };
  return badges[resultado] || "bg-gray-100 text-gray-800";
}

function resultadoTexto(resultado: string) {
  const textos: Record<string, string> = {
    no_revisada: "No revisada",
    aprobado: "Aprobado",
    denegado: "Denegado",
  };
  return textos[resultado] || resultado;
}
</script>
