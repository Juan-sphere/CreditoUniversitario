<template>
  <div class="w-full">
    <Information title="Información personal">
      <template #information>
        <div class="grid grid-cols-4 gap-4 p-4">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Apellido paterno</label>
            <input
              v-model="apellidoPaterno"
              type="text"
              disabled
              class="w-full px-3 py-1 border border-gray-300 rounded bg-gray-100 cursor-not-allowed"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Apellido materno</label>
            <input
              v-model="apellidoMaterno"
              type="text"
              disabled
              class="w-full px-3 py-1 border border-gray-300 rounded bg-gray-100 cursor-not-allowed"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Nombre</label>
            <input
              v-model="nombre"
              type="text"
              disabled
              class="w-full px-3 py-1 border border-gray-300 rounded bg-gray-100 cursor-not-allowed"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Segundo nombre</label>
            <input
              v-model="segundoNombre"
              type="text"
              disabled
              class="w-full px-3 py-1 border border-gray-300 rounded bg-gray-100 cursor-not-allowed"
            />
          </div>
          <div class="col-span-1 flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">DNI</label>
            <input
              v-model="dni"
              type="text"
              disabled
              class="w-full px-3 py-1 border border-gray-300 rounded bg-gray-100 cursor-not-allowed"
            />
          </div>
          <div class="col-span-2 flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Correo electrónico universidad</label
            >
            <input
              v-model="correoUniversidad"
              type="email"
              disabled
              class="w-full px-3 py-1 border border-gray-300 rounded text-black bg-gray-100 cursor-not-allowed"
              required
            />
          </div>
        </div>
      </template>
    </Information>

    <!-- Loading Spinner mientras carga datos -->
    <LoadingSpinner v-if="cargandoDatos" />

    <!-- Contenido actual -->
    <Register
      v-else
      :tabs="[
        'Inf. Adicional',
        'Correo Electrónico',
        'Dirección',
        'Datos Laborales',
      ]"
      :activeTab="activeTab"
      @tab-change="activeTab = $event"
    >
      <template #register>
        <!-- Información adicional -->
        <div class="p-2" v-if="activeTab === 0">
          <div class="grid grid-cols-2 gap-4">
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Estado Civil <span class="text-red-500">(*)</span></label
              >
              <select
                v-model="estadoCivil"
                class="w-full px-3 py-1 border border-gray-300 rounded"
              >
                <option value="">--Seleccione--</option>
                <option>Soltero(a)</option>
                <option>Casado(a)</option>
                <option>Divorciado(a)</option>
                <option>Viudo(a)</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Es conviviente? <span class="text-red-500">(*)</span></label
              >
              <select
                v-model="esConviviente"
                class="w-full px-3 py-1 border border-gray-300 rounded"
              >
                <option value="">--Seleccione--</option>
                <option value="true">Sí</option>
                <option value="false">No</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Fecha de nacimiento
                <span class="text-red-500">(*)</span></label
              >
              <input
                v-model="fechaNacimiento"
                type="date"
                class="w-full px-3 py-1 border border-gray-300 rounded"
              />
            </div>
            <ProvinceSelect
              v-model="lugarNacimiento"
              label="Lugar de nacimiento"
              :required="true"
            />
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Sexo <span class="text-red-500">(*)</span></label
              >
              <select
                v-model="sexo"
                class="w-full px-3 py-1 border border-gray-300 rounded"
              >
                <option value="">--Seleccione--</option>
                <option>Masculino</option>
                <option>Femenino</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Telefono celular <span class="text-red-500">(*)</span></label
              >
              <input
                v-model="telefonoCelular"
                type="text"
                class="w-full px-3 py-1 border border-gray-300 rounded"
                required
              />
            </div>
          </div>
          <div class="w-full flex justify-between items-center mt-5">
            <CampoObligatorio />
            <button
              type="button"
              :disabled="!tab0Valido"
              @click="guardarTab0"
              class="px-4 py-1 bg-terciary text-white disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Siguiente
            </button>
          </div>
        </div>
        <!-- Correo electrónico universidad -->
        <div class="p-2" v-if="activeTab === 1">
          <div class="grid grid-cols-2 gap-4">
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Correo electrónico personal
                <span class="text-red-500">(*)</span></label
              >
              <input
                v-model="correoPersonal"
                type="email"
                class="w-full px-3 py-1 border text-black border-gray-300 rounded"
                placeholder="usuario@dominio.com"
                required
              />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Correo electrónico laboral
                <span class="text-red-500">(*)</span></label
              >
              <input
                v-model="correoLaboral"
                type="email"
                class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="usuario@dominio.com"
                required
              />
            </div>
          </div>
          <div class="w-full flex justify-between items-center mt-5">
            <CampoObligatorio />
            <button
              type="button"
              :disabled="!tab1Valido"
              @click="guardarTab1"
              class="px-4 py-1 bg-terciary text-white disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Siguiente
            </button>
          </div>
        </div>
        <!-- Dirección -->
        <div class="p-2" v-if="activeTab === 2">
          <div class="grid grid-cols-2 gap-4">
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Tipo de vía <span class="text-red-500">(*)</span></label
              >
              <select
                v-model="tipoVia"
                class="w-full px-3 py-1 border border-gray-300 rounded"
                required
                @change="limpiarConfirmacion"
              >
                <option value="">--Seleccione--</option>
                <option>Calle</option>
                <option>Pasaje</option>
                <option>Jirón</option>
                <option>Avenida</option>
                <option>Sin nombre</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Nombre de la vía <span class="text-red-500">(*)</span></label
              >
              <input
                type="text"
                v-model="nombreVia"
                class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="Nombre de la calle o avenida"
                required
                @input="limpiarConfirmacion"
              />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Número de vivienda <span class="text-red-500">(*)</span></label
              >
              <input
                type="text"
                v-model="numeroVivienda"
                class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="Número del domicilio"
                required
                @input="limpiarConfirmacion"
              />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Urbanización <span class="text-red-500">(*)</span></label
              >
              <input
                type="text"
                v-model="urbanizacion"
                class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="Nombre de urbanización"
                required
                @input="limpiarConfirmacion"
              />
            </div>
            <div class="flex flex-col gap-2 col-span-2">
              <label class="text-gray-700 font-semibold"
                >Distrito <span class="text-red-500">(*)</span></label
              >
              <select
                v-model="distrito"
                class="w-full px-3 py-1 border border-gray-300 rounded"
                required
                @change="limpiarConfirmacion"
              >
                <option value="">--Seleccione--</option>
                <option>Ancón</option>
                <option>Ate</option>
                <option>Barranco</option>
                <option>Breña</option>
                <option>Carabayllo</option>
                <option>Chaclacayo</option>
                <option>Chorrillos</option>
                <option>Comas</option>
                <option>Cono Este</option>
                <option>Cono Norte</option>
                <option>Cono Oeste</option>
                <option>El Agustino</option>
                <option>Huacho</option>
                <option>Junín</option>
                <option>La Caleta</option>
                <option>La Molina</option>
                <option>La Perla</option>
                <option>La Punta</option>
                <option>Lince</option>
                <option>Lurín</option>
                <option>Lima</option>
                <option>Los Olivos</option>
                <option>Magdalena</option>
                <option>Magdalena del Mar</option>
                <option>Miraflores</option>
                <option>Pachacamac</option>
                <option>Pucusana</option>
                <option>Puente Piedra</option>
                <option>Punta Hermosa</option>
                <option>Punta Negra</option>
                <option>Rímac</option>
                <option>San Bartolo</option>
                <option>San Isidro</option>
                <option>San Martín de Porres</option>
                <option>San Miguel</option>
                <option>Santa Anita</option>
                <option>Santa María del Mar</option>
                <option>Santa Rosa</option>
                <option>Santiago de Surco</option>
                <option>Surquillo</option>
                <option>Villa El Salvador</option>
                <option>Villa María del Triunfo</option>
                <option>Vitarte</option>
              </select>
            </div>
          </div>

          <!-- Sugerencias y mapa -->
          <div class="mt-4" v-if="direccionQuery">
            <!-- Spinner de búsqueda -->
            <div
              v-if="buscandoDireccion"
              class="flex items-center gap-2 text-sm text-gray-500 mb-2"
            >
              <svg
                class="animate-spin h-4 w-4 text-blue-500"
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
                />
                <path
                  class="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8v8H4z"
                />
              </svg>
              <span>Buscando dirección...</span>
            </div>

            <!-- Lista de sugerencias -->
            <div
              v-if="sugerenciasDireccion.length > 0 && !direccionConfirmada"
              class="border border-gray-300 rounded shadow-md bg-white"
            >
              <p
                class="px-3 py-1 text-xs text-gray-400 border-b border-gray-100"
              >
                Selecciona una opción para confirmar la ubicación:
              </p>
              <ul class="max-h-48 overflow-y-auto">
                <li
                  v-for="(sugerencia, index) in sugerenciasDireccion"
                  :key="index"
                  @click="seleccionarDireccion(sugerencia)"
                  class="px-3 py-2 hover:bg-blue-50 cursor-pointer text-sm border-b border-gray-100 last:border-0"
                >
                  <span class="font-medium">{{
                    sugerencia.placePrediction?.mainText?.text ||
                    sugerencia.placePrediction?.text?.text
                  }}</span>
                  <span
                    v-if="sugerencia.placePrediction?.secondaryText?.text"
                    class="block text-xs text-gray-500 mt-0.5"
                  >
                    {{ sugerencia.placePrediction.secondaryText.text }}
                  </span>
                </li>
              </ul>
            </div>

            <!-- Error de Maps -->
            <p v-if="errorMaps" class="text-xs text-red-500 mt-1">
              {{ errorMaps }}
            </p>
          </div>

          <!-- Dirección confirmada + mapa -->
          <div v-if="direccionConfirmada" class="mt-4">
            <div class="flex items-center gap-2 mb-2">
              <svg
                class="w-4 h-4 text-green-600 shrink-0"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                  clip-rule="evenodd"
                />
              </svg>
              <p class="text-sm text-gray-700 truncate">
                <strong>{{ direccionConfirmada.main_text }}</strong>
                <span
                  v-if="direccionConfirmada.secondary_text"
                  class="text-gray-500 ml-1"
                >
                  — {{ direccionConfirmada.secondary_text }}
                </span>
              </p>
            </div>
            <div
              ref="mapContainerDireccion"
              class="w-full rounded border border-gray-300"
              style="height: 220px"
            ></div>
          </div>

          <div class="w-full flex justify-between items-center mt-5">
            <CampoObligatorio />
            <button
              type="button"
              :disabled="!tab2Valido"
              @click="guardarTab2"
              class="px-4 py-1 bg-terciary text-white disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Siguiente
            </button>
          </div>
        </div>
        <!-- Datos laborales -->
        <div class="flex flex-col gap-4 p-2" v-if="activeTab === 3">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >¿El postulante trabaja?
              <span class="text-red-500">(*)</span></label
            >
            <select
              v-model="postulanteTrabaja"
              class="w-full px-3 py-1 border border-gray-300 rounded"
              required
            >
              <option value="">--Seleccione--</option>
              <option value="Si">Sí</option>
              <option value="No">No</option>
            </select>
          </div>

          <template v-if="postulanteTrabaja === 'Si'">
            <div>
              <label class="text-gray-700 font-semibold"
                >Tipo de trabajo <span class="text-red-500">(*)</span></label
              >
              <div class="grid grid-cols-1 gap-2 mt-2 pl-2">
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    id="trabajo1"
                    value="Trabajo dependiente formal en planilla"
                    v-model="tiposTrabajo"
                    class="w-4 h-4"
                  />
                  <label for="trabajo1" class="ml-2 text-gray-700"
                    >Trabajo dependiente formal en planilla</label
                  >
                </div>
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    id="trabajo2"
                    value="Trabajo dependiente formal en Recibo por Honorarios"
                    v-model="tiposTrabajo"
                    class="w-4 h-4"
                  />
                  <label for="trabajo2" class="ml-2 text-gray-700"
                    >Trabajo dependiente formal en Recibo por Honorarios</label
                  >
                </div>
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    id="trabajo3"
                    value="Trabajo dependiente informal"
                    v-model="tiposTrabajo"
                    class="w-4 h-4"
                  />
                  <label for="trabajo3" class="ml-2 text-gray-700"
                    >Trabajo dependiente informal</label
                  >
                </div>
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    id="trabajo4"
                    value="Trabajo independiente informal"
                    v-model="tiposTrabajo"
                    class="w-4 h-4"
                  />
                  <label for="trabajo4" class="ml-2 text-gray-700"
                    >Trabajo independiente informal</label
                  >
                </div>
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    id="trabajo5"
                    value="Empresa/Negocio propio formal"
                    v-model="tiposTrabajo"
                    class="w-4 h-4"
                  />
                  <label for="trabajo5" class="ml-2 text-gray-700"
                    >Empresa/Negocio propio formal</label
                  >
                </div>
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    id="trabajo6"
                    value="Empresa/Negocio propio informal"
                    v-model="tiposTrabajo"
                    class="w-4 h-4"
                  />
                  <label for="trabajo6" class="ml-2 text-gray-700"
                    >Empresa/Negocio propio informal</label
                  >
                </div>
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    id="trabajo7"
                    value="Practicante pre-profesional"
                    v-model="tiposTrabajo"
                    class="w-4 h-4"
                  />
                  <label for="trabajo7" class="ml-2 text-gray-700"
                    >Practicante pre-profesional</label
                  >
                </div>
              </div>
            </div>

            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold"
                >Ingresos mensuales (S/.)
                <span class="text-red-500">(*)</span></label
              >
              <input
                v-model="ingresosMensuales"
                type="number"
                class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="Ej: 2500.00"
                min="0"
                step="0.01"
                required
              />
            </div>
          </template>

          <div class="w-full flex justify-between items-center mt-5 pl-2">
            <CampoObligatorio />
            <button
              type="button"
              :disabled="!tab3Valido"
              @click="guardarTab3"
              class="px-4 py-1 bg-terciary text-white disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Siguiente
            </button>
          </div>
        </div>
      </template>
    </Register>

    <div class="flex items-center justify-end gap-3 mt-4">
      <p v-if="errorGuardado" class="text-sm text-red-600">
        {{ errorGuardado }}
      </p>
      <button
        type="button"
        :disabled="guardando || !todoValido"
        @click="guardarTodo"
        class="px-6 py-1 bg-primary text-white rounded disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {{
          guardando
            ? esActualizacion
              ? "Actualizando..."
              : "Guardando..."
            : esActualizacion
              ? "Actualizar"
              : "Guardar"
        }}
      </button>
    </div>

    <BackNext />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, nextTick, onMounted, markRaw } from "vue";
import { toast } from "vue3-toastify";

const config = useRuntimeConfig();
const { token, loadToken } = useAuth();

// Cookie directa para asegurar que siempre tenga el valor más reciente
const tokenCookie = useCookie<string | null>("auth_token");

// Cargar token desde cookies al inicializar
loadToken();

const activeTab = ref(0);
const guardando = ref(false);
const errorGuardado = ref("");
const postulanteTrabaja = ref("");
const tiposTrabajo = ref<string[]>([]);
const esActualizacion = ref(false);
const cargandoDatos = ref(true);

// Campos de información personal (solo lectura, vienen del usuario autenticado)
const apellidoPaterno = ref("");
const apellidoMaterno = ref("");
const nombre = ref("");
const segundoNombre = ref("");
const dni = ref("");
const correoUniversidad = ref("");

// Tab 0: Información adicional
const estadoCivil = ref("");
const esConviviente = ref("");
const fechaNacimiento = ref("");
const sexo = ref("");
const telefonoCelular = ref("");

// Tab 1: Correo
const correoPersonal = ref("");
const correoLaboral = ref("");

// Tab 2: Dirección
const tipoVia = ref("");
const nombreVia = ref("");
const numeroVivienda = ref("");
const urbanizacion = ref("");
const distrito = ref("");

// Tab 3: Datos laborales
const ingresosMensuales = ref<number | null>(null);

// Lugar de nacimiento
const lugarNacimiento = ref("");

// Validación por tab
const tab0Valido = computed(
  () =>
    !!estadoCivil.value &&
    esConviviente.value !== "" &&
    !!fechaNacimiento.value &&
    !!lugarNacimiento.value &&
    !!sexo.value &&
    !!telefonoCelular.value,
);

const tab1Valido = computed(
  () => !!correoPersonal.value && !!correoLaboral.value,
);

const tab2Valido = computed(
  () =>
    !!tipoVia.value &&
    !!nombreVia.value &&
    !!numeroVivienda.value &&
    !!urbanizacion.value &&
    !!distrito.value,
);

const tab3Valido = computed(() => {
  if (!postulanteTrabaja.value) return false;
  if (postulanteTrabaja.value === "Si") {
    return tiposTrabajo.value.length > 0 && ingresosMensuales.value !== null;
  }
  return true;
});

const todoValido = computed(
  () =>
    tab0Valido.value &&
    tab1Valido.value &&
    tab2Valido.value &&
    tab3Valido.value,
);

// "Siguiente" solo valida y avanza al siguiente tab
function guardarTab0() {
  activeTab.value = 1;
}
function guardarTab1() {
  activeTab.value = 2;
}
function guardarTab2() {
  activeTab.value = 3;
}
function guardarTab3() {
  /* queda en tab 3, esperar Guardar */
}

// "Guardar" envía todo a la API de una sola vez
async function guardarTodo() {
  guardando.value = true;
  errorGuardado.value = "";

  // Usar el token directamente de la cookie para asegurar el valor más reciente
  const currentToken = tokenCookie.value;

  if (!currentToken) {
    errorGuardado.value =
      "Sesión expirada. Por favor, inicia sesión nuevamente.";
    guardando.value = false;
    return;
  }

  console.log("[DEBUG] Token disponible:", currentToken ? "Sí" : "No");

  try {
    await $fetch("/auth/informacion-personal", {
      baseURL: config.public.apiBase,
      method: "POST",
      headers: { Authorization: `Bearer ${currentToken}` },
      body: {
        estado_civil: estadoCivil.value || undefined,
        es_conviviente:
          esConviviente.value !== ""
            ? esConviviente.value === "true"
            : undefined,
        fecha_nacimiento: fechaNacimiento.value || undefined,
        lugar_nacimiento: lugarNacimiento.value || undefined,
        sexo: sexo.value || undefined,
        telefono_celular: telefonoCelular.value || undefined,
        correo_personal: correoPersonal.value || undefined,
        correo_laboral: correoLaboral.value || undefined,
        tipo_via: tipoVia.value || undefined,
        nombre_via: nombreVia.value || undefined,
        numero_vivienda: numeroVivienda.value || undefined,
        urbanizacion: urbanizacion.value || undefined,
        distrito: distrito.value || undefined,
        trabaja:
          postulanteTrabaja.value !== ""
            ? postulanteTrabaja.value === "Si"
            : undefined,
        tipo_trabajo: tiposTrabajo.value.length
          ? tiposTrabajo.value.join(", ")
          : undefined,
        ingresos_mensuales: ingresosMensuales.value ?? undefined,
      },
    });
    toast.success(
      esActualizacion.value
        ? "¡Información actualizada correctamente!"
        : "¡Información guardada correctamente!",
    );
    esActualizacion.value = true;
    setTimeout(() => navigateTo("/informacion-padres"), 1500);
  } catch (e: any) {
    const mensaje = e?.data?.detail || "Error al guardar. Intenta de nuevo.";
    errorGuardado.value = mensaje;
    toast.error(mensaje);
  } finally {
    guardando.value = false;
  }
}

// Estado del buscador de dirección
const sugerenciasDireccion = ref<any[]>([]);
const direccionConfirmada = ref<any>(null);
const mapContainerDireccion = ref<HTMLDivElement>();
const buscandoDireccion = ref(false);
const errorMaps = ref("");

let mapsListo = false;
let mapInstance: any = null;
let markerInstance: any = null;
let debounceTimer: ReturnType<typeof setTimeout> | null = null;

// Concatenación de los campos para usar como query de búsqueda
const direccionQuery = computed(() => {
  const partes = [
    tipoVia.value,
    nombreVia.value,
    numeroVivienda.value,
    urbanizacion.value,
    distrito.value,
  ].filter((v) => v && v.trim() !== "");
  return partes.length >= 2 ? partes.join(" ") : "";
});

onMounted(async () => {
  // Cargar datos del usuario autenticado
  const { usuario } = useAuth();

  if (usuario.value) {
    // Los datos vienen del login y están guardados en localStorage
    apellidoPaterno.value = usuario.value.apellido_paterno || "";
    apellidoMaterno.value = usuario.value.apellido_materno || "";
    nombre.value = usuario.value.nombre || "";
    segundoNombre.value = usuario.value.segundo_nombre || "";
    dni.value = usuario.value.numero_documento || "";
    correoUniversidad.value = usuario.value.correo_universidad || "";
  }

  // Cargar información personal guardada previamente
  const currentToken = tokenCookie.value;
  if (currentToken) {
    try {
      const response = await $fetch<{ data: any }>(
        "/auth/informacion-personal",
        {
          baseURL: config.public.apiBase,
          method: "GET",
          headers: { Authorization: `Bearer ${currentToken}` },
        },
      );

      if (response.data) {
        const info = response.data;
        // Tab 0: Información adicional
        estadoCivil.value = info.estado_civil || "";
        esConviviente.value =
          info.es_conviviente !== null ? String(info.es_conviviente) : "";
        fechaNacimiento.value = info.fecha_nacimiento || "";
        lugarNacimiento.value = info.lugar_nacimiento || "";
        sexo.value = info.sexo || "";
        telefonoCelular.value = info.telefono_celular || "";

        // Tab 1: Correo
        correoPersonal.value = info.correo_personal || "";
        correoLaboral.value = info.correo_laboral || "";

        // Tab 2: Dirección
        tipoVia.value = info.tipo_via || "";
        nombreVia.value = info.nombre_via || "";
        numeroVivienda.value = info.numero_vivienda || "";
        urbanizacion.value = info.urbanizacion || "";
        distrito.value = info.distrito || "";

        // Tab 3: Datos laborales
        postulanteTrabaja.value =
          info.trabaja !== null ? (info.trabaja ? "Si" : "No") : "";
        if (info.tipo_trabajo && info.tipo_trabajo !== "No tiene") {
          tiposTrabajo.value = info.tipo_trabajo.split(", ");
        }
        ingresosMensuales.value = info.ingresos_mensuales;

        esActualizacion.value = true;
        console.log("[INFO-PERSONAL] ✓ Datos cargados correctamente");
      }
    } catch (e) {
      console.error("[INFO-PERSONAL] Error al cargar datos:", e);
    }
  }

  // Cargar Google Maps
  const esNuevoAPI = () =>
    !!(window as any).google?.maps?.places?.AutocompleteSuggestion;

  if (esNuevoAPI()) {
    mapsListo = true;
  } else {
    const interval = setInterval(() => {
      if (esNuevoAPI()) {
        clearInterval(interval);
        mapsListo = true;
      }
    }, 100);
    setTimeout(() => {
      clearInterval(interval);
      if (!mapsListo) {
        errorMaps.value = "Error al cargar Google Maps. Verifica la API Key.";
      }
    }, 10000);
  }

  // Datos cargados
  cargandoDatos.value = false;
});

// Observar la concatenación y disparar búsqueda con debounce
watch(direccionQuery, (query) => {
  if (debounceTimer) clearTimeout(debounceTimer);

  if (!query) {
    sugerenciasDireccion.value = [];
    return;
  }
  if (!mapsListo) {
    errorMaps.value = "Google Maps aún no está listo. Espera un momento.";
    return;
  }

  errorMaps.value = "";
  buscandoDireccion.value = true;

  debounceTimer = setTimeout(async () => {
    try {
      sugerenciasDireccion.value = await buscarPredicciones(query);
    } catch {
      sugerenciasDireccion.value = [];
    } finally {
      buscandoDireccion.value = false;
    }
  }, 400);
});

// Renderizar mapa cuando se confirma una dirección
watch(direccionConfirmada, async (nueva) => {
  if (!nueva) {
    mapInstance = null;
    markerInstance = null;
    return;
  }
  await nextTick();
  renderizarMapa(nueva.latitude, nueva.longitude);
});

const buscarPredicciones = async (input: string): Promise<any[]> => {
  try {
    const google = (window as any).google;
    const result =
      await google.maps.places.AutocompleteSuggestion.fetchAutocompleteSuggestions(
        { input, includedRegionCodes: ["pe"] },
      );
    return (result.suggestions || []).map((s: any) => markRaw(s));
  } catch (error) {
    console.error("Error al buscar sugerencias:", error);
    return [];
  }
};

const seleccionarDireccion = async (sugerencia: any) => {
  const placePrediction = sugerencia.placePrediction;
  if (!placePrediction) return;

  try {
    const place = placePrediction.toPlace();
    await place.fetchFields({
      fields: [
        "displayName",
        "formattedAddress",
        "location",
        "addressComponents",
      ],
    });

    const mainText =
      placePrediction.mainText?.text || placePrediction.text?.text || "";
    const secondaryText = placePrediction.secondaryText?.text || "";

    direccionConfirmada.value = {
      main_text: mainText,
      secondary_text: secondaryText,
      formatted_address: place.formattedAddress,
      latitude: place.location.lat(),
      longitude: place.location.lng(),
      placeId: placePrediction.placeId,
      addressComponents: place.addressComponents,
    };
    sugerenciasDireccion.value = [];
  } catch (error) {
    console.error("Error al obtener detalles del lugar:", error);
    errorMaps.value = "No se pudieron obtener los detalles de la dirección.";
  }
};

const renderizarMapa = (lat: number, lng: number) => {
  if (!mapContainerDireccion.value) return;
  const google = (window as any).google;
  const position = { lat, lng };

  if (mapInstance) {
    mapInstance.setCenter(position);
    markerInstance.setPosition(position);
  } else {
    mapInstance = new google.maps.Map(mapContainerDireccion.value, {
      center: position,
      zoom: 16,
      mapTypeControl: false,
      streetViewControl: false,
      fullscreenControl: false,
    });
    markerInstance = new google.maps.Marker({
      position,
      map: mapInstance,
      animation: google.maps.Animation.DROP,
    });
  }
};

const limpiarConfirmacion = () => {
  if (direccionConfirmada.value) {
    direccionConfirmada.value = null;
    mapInstance = null;
    markerInstance = null;
  }
};
</script>
