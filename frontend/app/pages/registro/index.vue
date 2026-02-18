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
        <h2 class="text-3xl font-bold text-gray-900">Crear Cuenta</h2>
        <p class="mt-2 text-sm text-gray-600">Regístrate con tu DNI o Código</p>
      </div>

      <!-- Info box -->
      <div class="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
        <p class="text-sm text-blue-800">
          Solo estudiantes habilitados pueden registrarse.
        </p>
      </div>

      <form @submit.prevent="registrarConDNI" class="space-y-5">
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
            Formato: DNI12345678, CE87654321
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
            placeholder="Mínimo 6 caracteres"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">
            Confirmar Contraseña
          </label>
          <input
            v-model="form.confirmar_password"
            type="password"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary bg-white"
            placeholder="Repite tu contraseña"
          />
        </div>

        <div
          v-if="error"
          class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm"
        >
          {{ error }}
        </div>

        <div
          v-if="success"
          class="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg text-sm"
        >
          {{ success }}
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 px-4 bg-primary text-white rounded-lg font-medium hover:opacity-90 transition disabled:opacity-50 shadow-lg"
        >
          <span v-if="!loading">CREAR CUENTA</span>
          <span v-else>Creando...</span>
        </button>
      </form>

      <p class="mt-6 text-center text-sm text-gray-600">
        ¿Ya tienes cuenta?
        <NuxtLink to="/" class="text-primary font-medium hover:underline">
          Inicia sesión
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
const form = ref({
  identificador: "",
  password: "",
  confirmar_password: "",
});
const error = ref("");
const success = ref("");
const loading = ref(false);

async function registrarConDNI() {
  error.value = "";
  success.value = "";

  if (form.value.password !== form.value.confirmar_password) {
    error.value = "Las contraseñas no coinciden";
    return;
  }

  loading.value = true;

  try {
    const response = await fetch("http://localhost:5000/auth/registro", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        identificador: form.value.identificador,
        contraseña: form.value.password,
        confirmar_contraseña: form.value.confirmar_password,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Error al registrar");
    }

    success.value =
      data.mensaje || "Cuenta creada! Revisa tu correo para verificar.";
    form.value = { identificador: "", password: "", confirmar_password: "" };

    setTimeout(() => {
      router.push("/");
    }, 3000);
  } catch (err: any) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped></style>
