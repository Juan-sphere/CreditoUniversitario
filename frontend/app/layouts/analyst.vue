<template>
  <!-- Contenido principal (solo si está autenticado) -->
  <div v-if="!isVerifying" class="max-w-350 mx-auto">
    <div class="pt-20">
      <Header />
      <div class="w-full">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { RUTAS_PUBLICAS, PREFIJOS_PUBLICOS } from "~/utils/routes-config";

const router = useRouter();
const { isAuthenticated, loadToken } = useAuth();

const isVerifying = ref(true);

// Función para verificar si una ruta es pública
const esRutaPublica = (path: string) => {
  if (RUTAS_PUBLICAS.includes(path)) return true;
  return PREFIJOS_PUBLICOS.some((prefijo) => path.startsWith(prefijo));
};

onMounted(async () => {
  // Cargar token desde cookies
  loadToken();

  // Verificar si es ruta pública
  if (esRutaPublica(router.currentRoute.value.path)) {
    isVerifying.value = false;
    return;
  }

  if (!isAuthenticated()) {
    await navigateTo("/");
  } else {
    isVerifying.value = false;
  }
});
</script>

<style scoped></style>
