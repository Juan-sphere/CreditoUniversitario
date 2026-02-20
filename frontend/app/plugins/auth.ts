export default defineNuxtPlugin(() => {
  const { loadToken } = useAuth();

  // Cargar token del localStorage al iniciar
  if (process.client) {
    loadToken();
  }
});
