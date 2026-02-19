<template>
  <div class="w-full">
    <Information title="Dirección del alumno">
      <template #information>
        <div class="bg-[#FFF9E9] p-4">
          <p class="text-yellow-500">
            Aviso! No Existen registros para la consulta...
          </p>
        </div>
      </template>
    </Information>
    <div class="w-full flex justify-start mt-5">
      <button
        type="button"
        @click="abrirModal"
        class="px-4 py-1 bg-gray-200 text-gray-500 hover:bg-gray-300 transition"
      >
        Nueva Dirección
      </button>
    </div>

    <Teleport to="body">
      <div
        v-if="mostrarModal"
        class="fixed inset-0 z-50 flex items-center justify-center p-4"
        style="
          background-color: rgba(0, 0, 0, 0.25);
          backdrop-filter: blur(4px);
        "
        @click.self="cerrarModal"
      >
        <div class="bg-white rounded-lg shadow-xl p-6 w-full max-w-lg">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-bold">Buscar Dirección</h2>
            <button
              @click="cerrarModal"
              class="text-gray-500 hover:text-gray-700 text-2xl leading-none"
            >
              ×
            </button>
          </div>

          <!-- Input de búsqueda -->
          <div class="mb-3 relative">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Dirección
            </label>
            <input
              ref="inputDireccion"
              v-model="busquedaDireccion"
              type="text"
              placeholder="Ingresa una dirección..."
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              @input="handleInputChange"
              autocomplete="off"
            />

            <!-- Spinner de carga -->
            <div v-if="buscando" class="absolute right-3 top-9">
              <svg
                class="animate-spin h-5 w-5 text-blue-500"
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
            </div>

            <!-- Lista de sugerencias -->
            <ul
              v-if="sugerencias.length > 0"
              class="absolute z-10 w-full mt-1 border border-gray-300 rounded-md shadow-lg bg-white max-h-48 overflow-y-auto"
            >
              <li
                v-for="(sugerencia, index) in sugerencias"
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

            <!-- Mensaje de error Maps -->
            <p v-if="errorMaps" class="mt-2 text-xs text-red-500">
              {{ errorMaps }}
            </p>
          </div>

          <!-- Mapa de confirmación -->
          <div v-if="direccionSeleccionada" class="mb-4">
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
                <strong>{{ direccionSeleccionada.main_text }}</strong>
                <span
                  v-if="direccionSeleccionada.secondary_text"
                  class="text-gray-500 ml-1"
                  >— {{ direccionSeleccionada.secondary_text }}</span
                >
              </p>
            </div>
            <!-- Contenedor del mapa -->
            <div
              ref="mapContainer"
              class="w-full rounded-md overflow-hidden border border-gray-300"
              style="height: 240px"
            ></div>
          </div>

          <div class="flex gap-2 justify-end">
            <button
              @click="cerrarModal"
              class="px-4 py-2 bg-gray-200 text-gray-700 rounded hover:bg-gray-300 transition"
            >
              Cancelar
            </button>
            <button
              @click="guardarDireccion"
              :disabled="!direccionSeleccionada"
              class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition disabled:bg-gray-400 disabled:cursor-not-allowed"
            >
              Guardar
            </button>
          </div>
        </div>
      </div>
    </Teleport>

    <BackNext />
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick, onMounted, markRaw } from "vue";

const mostrarModal = ref(false);
const busquedaDireccion = ref("");
const sugerencias = ref<any[]>([]);
const direccionSeleccionada = ref<any>(null);
const inputDireccion = ref<HTMLInputElement>();
const mapContainer = ref<HTMLDivElement>();
const buscando = ref(false);
const errorMaps = ref("");

let mapsListo = false;
let mapInstance: any = null;
let markerInstance: any = null;
let debounceTimer: ReturnType<typeof setTimeout> | null = null;

onMounted(() => {
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
});

// Renderizar mapa cuando se selecciona una dirección
watch(direccionSeleccionada, async (nueva) => {
  if (!nueva) {
    mapInstance = null;
    markerInstance = null;
    return;
  }
  await nextTick();
  renderizarMapa(nueva.latitude, nueva.longitude);
});

const renderizarMapa = (lat: number, lng: number) => {
  if (!mapContainer.value) return;
  const google = (window as any).google;
  const position = { lat, lng };

  if (mapInstance) {
    mapInstance.setCenter(position);
    markerInstance.setPosition(position);
  } else {
    mapInstance = new google.maps.Map(mapContainer.value, {
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

// Nueva Places API (New): AutocompleteSuggestion
const buscarPredicciones = async (input: string): Promise<any[]> => {
  try {
    const google = (window as any).google;
    const result =
      await google.maps.places.AutocompleteSuggestion.fetchAutocompleteSuggestions(
        {
          input,
          includedRegionCodes: ["pe"],
        },
      );
    return (result.suggestions || []).map((s: any) => markRaw(s));
  } catch (error) {
    console.error("Error al buscar sugerencias:", error);
    return [];
  }
};

const handleInputChange = () => {
  direccionSeleccionada.value = null;
  if (debounceTimer) clearTimeout(debounceTimer);

  if (busquedaDireccion.value.length < 3) {
    sugerencias.value = [];
    return;
  }
  if (!mapsListo) {
    errorMaps.value = "Google Maps aún no está listo. Espera un momento.";
    return;
  }

  errorMaps.value = "";
  buscando.value = true;

  debounceTimer = setTimeout(async () => {
    try {
      sugerencias.value = await buscarPredicciones(busquedaDireccion.value);
    } catch {
      sugerencias.value = [];
    } finally {
      buscando.value = false;
    }
  }, 350);
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

    direccionSeleccionada.value = {
      main_text: mainText,
      secondary_text: secondaryText,
      formatted_address: place.formattedAddress,
      latitude: place.location.lat(),
      longitude: place.location.lng(),
      placeId: placePrediction.placeId,
      addressComponents: place.addressComponents,
    };
    busquedaDireccion.value = mainText;
    sugerencias.value = [];
  } catch (error) {
    console.error("Error al obtener detalles del lugar:", error);
    errorMaps.value = "No se pudieron obtener los detalles de la dirección.";
  }
};

const abrirModal = () => {
  mostrarModal.value = true;
  busquedaDireccion.value = "";
  direccionSeleccionada.value = null;
  sugerencias.value = [];
  errorMaps.value = "";
  mapInstance = null;
  markerInstance = null;
  setTimeout(() => {
    inputDireccion.value?.focus();
  }, 100);
};

const cerrarModal = () => {
  mostrarModal.value = false;
  busquedaDireccion.value = "";
  direccionSeleccionada.value = null;
  sugerencias.value = [];
  mapInstance = null;
  markerInstance = null;
  if (debounceTimer) clearTimeout(debounceTimer);
};

const guardarDireccion = () => {
  if (direccionSeleccionada.value) {
    console.log("Dirección guardada:", direccionSeleccionada.value);
    cerrarModal();
  }
};
</script>
