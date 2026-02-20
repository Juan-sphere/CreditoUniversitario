export default defineNuxtRouteMiddleware((to, from) => {
  // Rutas públicas que no requieren autenticación
  const rutasPublicas = ["/", "/registro"];

  if (rutasPublicas.includes(to.path)) {
    return;
  }

  const { token, loadToken, isAuthenticated } = useAuth();

  if (!token.value) {
    loadToken();
  }

  if (!isAuthenticated()) {
    return navigateTo("/");
  }
});
