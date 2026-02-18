<template>
  <div
    class="min-h-screen flex items-center justify-center py-12 px-4 relative"
    style="
      background-image: url(&quot;/images/fondo1.jpg&quot;);
      background-size: cover;
      background-position: center;
    "
  >
    <!-- Overlay más suave -->
    <div
      class="absolute inset-0 bg-linear-to-br from-black/50 to-black/30 -z-10"
    ></div>

    <!-- Contenido -->
    <div
      class="relative max-w-md w-full bg-white/95 backdrop-blur-sm rounded-lg shadow-2xl p-8"
    >
      <div class="text-center mb-8">
        <h2 class="text-3xl font-bold text-gray-900">Iniciar Sesión</h2>
        <p class="mt-2 text-sm text-gray-600">Accede con tu DNI o Código</p>
      </div>

      <form @submit.prevent="loginConDNI" class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">
            DNI o Código de Universidad
          </label>
          <input
            v-model="form.identificador"
            type="text"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary bg-white"
            placeholder="DNI99999999 o código"
          />
          <p class="mt-1 text-xs text-gray-500">
            Ejemplos: DNI12345678, CE87654321
          </p>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Contraseña</label
          >
          <input
            v-model="form.password"
            type="password"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary bg-white"
            placeholder="••••••••"
          />
        </div>

        <div
          v-if="error"
          class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm"
        >
          {{ error }}
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 px-4 bg-primary text-white rounded-lg font-medium hover:opacity-90 transition disabled:opacity-50 shadow-lg"
        >
          <span v-if="!loading">INICIAR SESIÓN</span>
          <span v-else>Cargando...</span>
        </button>
      </form>

      <p class="mt-6 text-center text-sm text-gray-600">
        ¿Primera vez aquí?
        <NuxtLink
          to="/registro"
          class="text-primary font-medium hover:underline"
        >
          Regístrate
        </NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

definePageMeta({
  layout: false,
});

const router = useRouter();
const form = ref({ identificador: "", password: "" });
const error = ref("");
const loading = ref(false);

async function loginConDNI() {
  error.value = "";
  loading.value = true;

  try {
    const response = await fetch("http://localhost:5000/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        identificador: form.value.identificador,
        contraseña: form.value.password,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Error al iniciar sesión");
    }

    localStorage.setItem("usuario", JSON.stringify(data.usuario));
    router.push("/instrucciones");
  } catch (err: any) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped></style>
