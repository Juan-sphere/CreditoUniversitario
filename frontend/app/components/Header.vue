<template>
  <div class="bg-dark text-white shadow-lg fixed top-0 left-0 right-0 z-50">
    <div class="max-w-325 mx-auto h-16 flex items-center">
      <!-- Logo izquierda -->
      <div class="flex-none">
        <img
          src="/images/logo.png"
          alt="Logo"
          class="h-12 w-auto object-contain"
        />
      </div>

      <!-- Menú centro -->
      <div class="flex-1 flex justify-center gap-8">
        <div class="cursor-pointer text-sm hover:opacity-80 transition">
          BANDEJA
        </div>
        <div class="cursor-pointer text-sm hover:opacity-80 transition">
          CAMBIAR CONTRASEÑA
        </div>
        <div class="cursor-pointer text-sm hover:opacity-80 transition">
          FORMATOS
        </div>
        <div class="cursor-pointer text-sm hover:opacity-80 transition">
          ESTADO SOLICITUD
        </div>
      </div>

      <!-- Usuario y Dropdown (derecha) -->
      <div class="relative" ref="dropdown">
        <button
          @click="toggleDropdown"
          class="flex items-center gap-3 px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg transition"
        >
          <!-- Icono de persona -->
          <div
            class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center"
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
                d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
              />
            </svg>
          </div>
          <div class="text-left">
            <div class="text-xs opacity-75">Bienvenido</div>
            <div class="font-medium">{{ nombreUsuario }}</div>
          </div>
          <!-- Flecha -->
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4 transition-transform"
            :class="{ 'rotate-180': isOpen }"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M19 9l-7 7-7-7"
            />
          </svg>
        </button>

        <!-- Dropdown Menu -->
        <transition
          enter-active-class="transition ease-out duration-100"
          enter-from-class="transform opacity-0 scale-95"
          enter-to-class="transform opacity-100 scale-100"
          leave-active-class="transition ease-in duration-75"
          leave-from-class="transform opacity-100 scale-100"
          leave-to-class="transform opacity-0 scale-95"
        >
          <div
            v-if="isOpen"
            class="absolute right-0 mt-2 w-56 bg-white rounded-lg shadow-xl py-2 text-gray-700"
          >
            <!-- Info usuario -->
            <div class="px-4 py-3 border-b border-gray-100">
              <p class="text-sm font-medium text-gray-900">
                {{ nombreCompleto || "Pepe Garcia" }}
              </p>
              <p class="text-xs text-gray-500 truncate">{{ universidad }}</p>
            </div>

            <!-- Opción cerrar sesión -->
            <button
              @click="cerrarSesion"
              class="w-full text-left px-4 py-2 text-sm hover:bg-red-50 hover:text-red-600 transition flex items-center gap-2"
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
              Cerrar Sesión
            </button>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const isOpen = ref(false);
const dropdown = ref<HTMLElement | null>(null);

const usuario = ref<any>(null);

// Cargar datos del usuario
onMounted(() => {
  const usuarioData = localStorage.getItem("usuario");
  if (usuarioData) {
    usuario.value = JSON.parse(usuarioData);
  }

  // Cerrar dropdown al hacer click fuera
  document.addEventListener("click", handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener("click", handleClickOutside);
});

const nombreUsuario = computed(() => {
  if (!usuario.value) return "Usuario";
  return usuario.value.nombres || "Usuario";
});

const nombreCompleto = computed(() => {
  if (!usuario.value) return "";
  return `${usuario.value.nombres} ${usuario.value.apellidos || ""}`.trim();
});

const universidad = computed(() => {
  if (!usuario.value) return "";
  return usuario.value.universidad || "";
});

function toggleDropdown() {
  isOpen.value = !isOpen.value;
}

function handleClickOutside(event: MouseEvent) {
  if (dropdown.value && !dropdown.value.contains(event.target as Node)) {
    isOpen.value = false;
  }
}

function cerrarSesion() {
  localStorage.removeItem("usuario");
  router.push("/");
}
</script>

<style scoped></style>
