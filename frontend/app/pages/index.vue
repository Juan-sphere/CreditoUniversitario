<template>
  <div
    class="min-h-screen flex flex-col items-center justify-center py-12 px-4 bg-cover bg-center relative"
    style="background-image: url(&quot;/images/fondo1.jpg&quot;)"
  >
    <!-- Overlay -->
    <div class="absolute inset-0 bg-black/30"></div>

    <!-- Logo: encima del card, en flujo normal -->
    <div class="relative z-10 mb-4">
      <img
        src="/images/logo.png"
        alt="ACCESSA"
        class="h-34 object-contain drop-shadow-xl"
      />
    </div>

    <!-- Contenido -->
    <div
      class="relative max-w-md w-full bg-white/95 backdrop-blur-sm rounded-xl shadow-2xl px-8 py-8"
    >
      <!-- Título -->
      <div class="text-center mb-5">
        <h2 class="text-2xl font-bold text-gray-900">Iniciar Sesión</h2>
      </div>

      <!-- Formulario -->
      <form @submit.prevent="login" class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >DNI</label
          >
          <input
            v-model="form.dni"
            type="text"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white"
            placeholder="12345678"
            maxlength="8"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Contraseña</label
          >
          <input
            v-model="form.password"
            type="password"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white"
            placeholder="••••••••"
          />
        </div>

        <!-- Error -->
        <div
          v-if="error"
          class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm"
        >
          {{ error }}
        </div>

        <!-- Botón -->
        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 px-4 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition disabled:opacity-50 shadow-lg"
        >
          <span v-if="!loading">INICIAR SESIÓN</span>
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
            Cargando...
          </span>
        </button>
      </form>

      <!-- Links -->
      <div class="mt-6 text-center space-y-2">
        <p class="text-sm text-gray-600">
          ¿Primera vez aquí?
          <NuxtLink
            to="/registro"
            class="text-blue-600 font-medium hover:underline"
          >
            Regístrate
          </NuxtLink>
        </p>
        <p class="text-sm">
          <a href="#" class="text-gray-500 hover:text-gray-700"
            >¿Olvidaste tu contraseña?</a
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { log } from "node:console";
import { ref } from "vue";
import { useRouter } from "vue-router";

definePageMeta({
  layout: false,
  middleware: [], // Desactivar middleware auth en esta página pública
});

const router = useRouter();
const config = useRuntimeConfig();
const { setToken } = useAuth();

const form = ref({ dni: "", password: "" });
const error = ref("");
const loading = ref(false);

async function login() {
  error.value = "";
  loading.value = true;

  try {
    const response = await $fetch<{
      success: boolean;
      detail?: string;
      access_token: string;
      usuario: any;
    }>("/auth/login", {
      baseURL: config.public.apiBase,
      method: "POST",
      body: {
        dni: form.value.dni,
        contraseña: form.value.password,
      },
    });
    console.log(response);

    if (!response.success) {
      throw new Error(response.detail || "Error al iniciar sesión");
    }

    // Guardar token y usuario
    setToken(response.access_token, response.usuario);

    // Redirigir a la siguiente página
    router.push("/instrucciones");
  } catch (err: any) {
    // Capturar el mensaje de error correctamente
    // FastAPI devuelve el error en err.data.detail
    error.value = err.data?.detail || err.message || "Error al iniciar sesión";
    console.error("Error de login:", err);
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped></style>
