<template>
  <div
    class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4"
  >
    <div class="max-w-md w-full bg-white rounded-lg shadow-lg p-8">
      <div class="text-center mb-8">
        <h2 class="text-3xl font-bold text-gray-900">Crear Cuenta</h2>
        <p class="mt-2 text-sm text-gray-600">Regístrate en el sistema</p>
      </div>

      <form @submit.prevent="registrarConEmail" class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Nombre Completo</label
          >
          <input
            v-model="form.nombre"
            type="text"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary"
            placeholder="Juan Pérez"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Email</label
          >
          <input
            v-model="form.email"
            type="email"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary"
            placeholder="tu@ejemplo.com"
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
            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary"
            placeholder="Mínimo 6 caracteres"
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
          class="w-full py-3 px-4 bg-primary text-white rounded-lg font-medium hover:opacity-90 transition disabled:opacity-50"
        >
          <span v-if="!loading">CREAR CUENTA</span>
          <span v-else>Creando...</span>
        </button>
      </form>

      <p class="mt-6 text-center text-sm text-gray-600">
        ¿Ya tienes cuenta?
        <router-link
          to="/auth/login"
          class="text-primary font-medium hover:underline"
        >
          Inicia sesión
        </router-link>
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
const form = ref({ nombre: "", email: "", password: "" });
const error = ref("");
const success = ref("");
const loading = ref(false);

async function registrarConEmail() {
  error.value = "";
  success.value = "";
  loading.value = true;

  try {
    const response = await fetch("http://localhost:5000/auth/registro", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        nombre: form.value.nombre,
        email: form.value.email,
        contraseña: form.value.password,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Error al registrar");
    }

    success.value = "Cuenta creada! Redirigiendo...";
    localStorage.setItem("usuario", JSON.stringify(data.usuario));

    setTimeout(() => {
      router.push("/instrucciones");
    }, 1500);
  } catch (err: any) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped></style>
