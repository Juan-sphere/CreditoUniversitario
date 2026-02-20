<template>
  <!-- Contenido principal (solo si está autenticado) -->
  <div v-if="!isVerifying" class="max-w-350 mx-auto">
    <div class="pt-20">
      <Header />
      <div class="flex gap-5 w-full">
        <Menu class="w-1/4 shrink-0" />

        <div class="w-3/4 min-w-0">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { RUTAS_PUBLICAS } from "~/utils/routes-config";

const router = useRouter();
const { isAuthenticated, loadToken } = useAuth();

const isVerifying = ref(true);

onMounted(async () => {
  // Cargar token desde localStorage
  loadToken();

  // Verificar si es ruta pública
  const esRutaPublica = RUTAS_PUBLICAS.includes(router.currentRoute.value.path);

  if (esRutaPublica) {
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
