export default defineNuxtRouteMiddleware((to, from) => {
  // Rutas públicas que no requieren autenticación
  const rutasPublicas = ["/", "/registro"];

  // Si la ruta es pública, permitir acceso
  if (rutasPublicas.includes(to.path)) {
    return;
  }

  // Cargar el token desde el composable
  const { token, loadToken } = useAuth();

  // Cargar token desde localStorage si no está cargado
  if (!token.value) {
    loadToken();
  }

  // Si no hay token, redirigir a login
  if (!token.value) {
    return navigateTo("/");
  }
});
