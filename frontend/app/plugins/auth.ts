export default defineNuxtPlugin((nuxtApp) => {
  const { loadToken } = useAuth();

  // Cargar token desde cookies al iniciar la app
  // La protección de rutas se maneja en middleware/auth.global.ts
  loadToken();
});
