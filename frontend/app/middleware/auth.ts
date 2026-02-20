export default defineNuxtRouteMiddleware((to, from) => {
  // Solo ejecutar en el cliente
  if (process.server) return;

  // Rutas públicas que NO requieren autenticación
  const rutasPublicas = ["/", "/registro", "/analista"];

  // Si la ruta es pública, dejar pasar
  if (rutasPublicas.includes(to.path)) {
    return;
  }

  // Para cualquier otra ruta, verificar si hay usuario
  const usuario = localStorage.getItem("usuario");

  if (!usuario) {
    return navigateTo("/");
  }
});
