export default defineNuxtRouteMiddleware((to, from) => {
  const rutasPublicasExactas = ["/", "/registro"];

  const prefijosPublicos = ["/analista"];

  if (rutasPublicasExactas.includes(to.path)) {
    return;
  }

  for (const prefijo of prefijosPublicos) {
    if (to.path.startsWith(prefijo)) {
      return;
    }
  }

  const tokenCookie = useCookie("auth_token");

  if (!tokenCookie.value) {
    console.log("[AUTH] No hay token, redirigiendo a login");
    return navigateTo("/");
  }
});
