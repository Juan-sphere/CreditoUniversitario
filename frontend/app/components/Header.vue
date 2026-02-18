<template>
  <div
    class="bg-primary text-white h-10 flex items-center justify-between px-6 my-5"
  >
    <!-- Menú izquierdo -->
    <div class="flex gap-6">
      <div class="cursor-pointer hover:opacity-80">BANDEJA</div>
      <div class="cursor-pointer hover:opacity-80">CAMBIAR CONTRASEÑA</div>
      <div class="cursor-pointer hover:opacity-80">FORMATOS</div>
      <div class="cursor-pointer hover:opacity-80">ESTADO SOLICITUD</div>
    </div>

    <!-- Botón Cerrar Sesión (derecha) -->
    <button
      @click="cerrarSesion"
      class="flex items-center gap-2 px-3 py-1 bg-white/10 hover:bg-white/20 rounded transition text-sm"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-4 w-4"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
        />
      </svg>
      <span>Cerrar Sesión</span>
    </button>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

function cerrarSesion() {
  // Limpiar localStorage
  localStorage.removeItem("usuario");

  // Redirigir al login
  router.push("/");
}
</script>

<style scoped></style>
