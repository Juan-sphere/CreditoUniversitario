import { RUTAS_PUBLICAS } from "~/utils/routes-config";

export default defineNuxtPlugin((nuxtApp) => {
  const { loadToken, isAuthenticated } = useAuth();
  const router = useRouter();

  if (process.client) {
    loadToken();
  }

  router.beforeEach((to, from, next) => {
    if (RUTAS_PUBLICAS.includes(to.path)) {
      next();
      return;
    }

    if (!isAuthenticated()) {
      next("/");
    } else {
      next();
    }
  });
});
