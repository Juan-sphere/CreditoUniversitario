<template>
  <div
    class="min-h-screen flex flex-col items-center justify-center py-12 px-4 bg-cover bg-center relative"
    style="background-image: url(&quot;/images/fondo2.jpg&quot;)"
  >
    <!-- Overlay -->
    <div class="absolute inset-0 bg-black/30"></div>

    <!-- Logo: encima del card, en flujo normal -->
    <div class="relative z-10 mb-4">
      <img
        src="/images/logo.png"
        alt="ACCESSA"
        class="h-24 object-contain drop-shadow-xl"
      />
    </div>

    <!-- Contenido -->
    <div
      class="relative max-w-md w-full bg-white/95 backdrop-blur-sm rounded-xl shadow-2xl px-8 py-8"
    >
      <!-- Título -->
      <div class="text-center mb-5">
        <h2 class="text-2xl font-bold text-gray-900">Registro</h2>
      </div>

      <!-- Info -->
      <div class="mb-5 p-3 bg-blue-50 border border-blue-200 rounded-lg">
        <p class="text-xs text-blue-800">
          Solo estudiantes autorizados pueden registrarse
        </p>
      </div>

      <!-- Formulario -->
      <form @submit.prevent="registrar" class="space-y-4">
        <!-- Universidad -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Universidad</label
          >
          <div class="relative">
            <select
              v-model="form.universidad"
              required
              :disabled="loadingUniversidades || datosAutocompletados"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none pr-10 text-sm"
            >
              <option value="" class="text-sm">
                Selecciona tu universidad
              </option>
              <option v-for="uni in universidades" :key="uni" :value="uni">
                {{ uni }}
              </option>
            </select>
            <!-- Indicador de carga -->
            <div
              v-if="loadingUniversidades"
              class="absolute right-3 top-1/2 transform -translate-y-1/2"
            >
              <div
                class="w-5 h-5 border-2 border-green-500 border-t-transparent rounded-full animate-spin"
              ></div>
            </div>
            <svg
              v-else
              class="absolute right-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400 pointer-events-none"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M19 9l-7 7-7-7"
              ></path>
            </svg>
          </div>
        </div>

        <!-- DNI con autocompletado -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >DNI</label
            >
            <div class="relative">
              <input
                v-model="form.dni"
                @input="buscarEstudiante"
                type="text"
                required
                maxlength="8"
                class="w-full pl-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white pr-10 text-sm"
                placeholder="72695726"
              />
              <!-- Spinner de búsqueda -->
              <div
                v-if="buscandoDNI"
                class="absolute right-3 top-1/2 transform -translate-y-1/2"
              >
                <div
                  class="w-5 h-5 border-2 border-green-500 border-t-transparent rounded-full animate-spin"
                ></div>
              </div>
              <!-- Check verde si encontró -->
              <svg
                v-else-if="datosAutocompletados"
                class="absolute right-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-green-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 13l4 4L19 7"
                ></path>
              </svg>
            </div>
            <p v-if="datosAutocompletados" class="mt-1 text-xs text-green-600">
              ✓ Datos encontrados
            </p>
          </div>

          <!-- Email Universidad (autocompletado) -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Email Universidad</label
            >
            <input
              v-model="form.correo"
              type="email"
              required
              :disabled="datosAutocompletados"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white disabled:bg-gray-50 text-sm"
              placeholder="tu@universidad.edu.pe"
            />
          </div>
        </div>

        <!-- Nombre (solo lectura, autocompletado) -->
        <div v-if="datosAutocompletados">
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Nombre Completo</label
          >
          <input
            :value="nombreCompleto"
            type="text"
            disabled
            class="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-700"
          />
        </div>

        <!-- Contraseña -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Contraseña</label
          >
          <input
            v-model="form.password"
            type="password"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 text-sm focus:ring-blue-500 focus:border-blue-500 bg-white"
            placeholder="Mínimo 6 caracteres"
          />
        </div>

        <!-- Confirmar -->
        <!-- <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Confirmar Contraseña</label
          >
          <input
            v-model="form.confirmar"
            type="password"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white"
            placeholder="Repite tu contraseña"
          />
        </div> -->

        <!-- Error -->
        <div
          v-if="error"
          class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm"
        >
          {{ error }}
        </div>

        <!-- Success -->
        <div
          v-if="success"
          class="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg text-sm"
        >
          {{ success }}
        </div>

        <!-- Botón -->
        <button
          type="submit"
          :disabled="loading || loadingUniversidades || !datosAutocompletados"
          class="w-full py-3 px-4 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition disabled:opacity-50 disabled:cursor-not-allowed shadow-lg"
        >
          <span v-if="!loading">REGISTRARSE</span>
          <span v-else class="flex items-center justify-center gap-2">
            <svg
              class="animate-spin h-5 w-5"
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
            Creando cuenta...
          </span>
        </button>
      </form>

      <!-- Link -->
      <p class="mt-6 text-center text-sm text-gray-600">
        ¿Ya tienes cuenta?
        <NuxtLink to="/" class="text-blue-600 font-medium hover:underline">
          Inicia sesión
        </NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";

definePageMeta({
  layout: false,
});

const router = useRouter();
const form = ref({
  universidad: "",
  dni: "",
  correo: "",
  password: "",
  confirmar: "",
});
const estudianteData = ref<any>(null);
const error = ref("");
const success = ref("");
const loading = ref(false);
const buscandoDNI = ref(false);
const datosAutocompletados = ref(false);
const universidades = ref<string[]>([]);
const loadingUniversidades = ref(false);

let timeoutId: ReturnType<typeof setTimeout>;

const nombreCompleto = computed(() => {
  if (!estudianteData.value) return "";
  const { nombres, apellido_paterno, apellido_materno } = estudianteData.value;
  return `${nombres} ${apellido_paterno} ${apellido_materno}`;
});

// Cargar universidades
onMounted(async () => {
  loadingUniversidades.value = true;
  try {
    const response = await fetch("http://localhost:5000/auth/universidades");
    const data = await response.json();
    universidades.value = data;
  } catch (err) {
    console.error("Error cargando universidades:", err);
  } finally {
    loadingUniversidades.value = false;
  }
});

// Buscar estudiante por DNI (con debounce)
async function buscarEstudiante() {
  clearTimeout(timeoutId);

  if (form.value.dni.length !== 8) {
    datosAutocompletados.value = false;
    estudianteData.value = null;
    return;
  }

  buscandoDNI.value = true;
  datosAutocompletados.value = false;

  timeoutId = setTimeout(async () => {
    try {
      const response = await fetch(
        `http://localhost:5000/auth/buscar-estudiante/${form.value.dni}`,
      );

      if (response.ok) {
        const data = await response.json();
        estudianteData.value = data;

        // Autocompletar campos
        form.value.universidad = data.universidad;
        form.value.correo = data.correo_universidad;
        datosAutocompletados.value = true;
      } else {
        datosAutocompletados.value = false;
        estudianteData.value = null;
      }
    } catch (err) {
      console.error("Error buscando estudiante:", err);
      datosAutocompletados.value = false;
    } finally {
      buscandoDNI.value = false;
    }
  }, 500); // Espera 500ms después de que el usuario deje de escribir
}

async function registrar() {
  error.value = "";
  success.value = "";

  if (!datosAutocompletados.value) {
    error.value = "DNI no encontrado en la base de estudiantes habilitados";
    return;
  }

  if (form.value.password !== form.value.confirmar) {
    error.value = "Las contraseñas no coinciden";
    return;
  }

  loading.value = true;

  try {
    const response = await fetch("http://localhost:5000/auth/registro", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        universidad: form.value.universidad,
        dni: form.value.dni,
        correo_universidad: form.value.correo,
        contraseña: form.value.password,
        confirmar_contraseña: form.value.confirmar,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Error al registrar");
    }

    success.value = "¡Cuenta creada! Redirigiendo...";

    setTimeout(() => {
      router.push("/");
    }, 2000);
  } catch (err: any) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped></style>
