export const useAuth = () => {
  const config = useRuntimeConfig();
  const apiBase = config.public.apiBase;

  const token = useState<string | null>("auth.token", () => null);
  const usuario = useState<any>("auth.usuario", () => null);

  // Cargar token desde localStorage
  const loadToken = () => {
    if (process.client) {
      const storedToken = localStorage.getItem("auth_token");
      const storedUsuario = localStorage.getItem("auth_usuario");

      if (storedToken) {
        token.value = storedToken;
      }
      if (storedUsuario) {
        usuario.value = JSON.parse(storedUsuario);
      }
    }
  };

  // Guardar token
  const setToken = (newToken: string, userData: any = null) => {
    token.value = newToken;
    if (process.client) {
      localStorage.setItem("auth_token", newToken);
      if (userData) {
        usuario.value = userData;
        localStorage.setItem("auth_usuario", JSON.stringify(userData));
      }
    }
  };

  // Obtener usuario actual
  const getUsuario = async () => {
    if (!token.value) return null;

    try {
      const response = await $fetch("/auth/me", {
        baseURL: apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (response.usuario) {
        usuario.value = response.usuario;
        if (process.client) {
          localStorage.setItem(
            "auth_usuario",
            JSON.stringify(response.usuario),
          );
        }
      }
      return response.usuario;
    } catch (error) {
      console.error("Error obteniendo usuario:", error);
      return null;
    }
  };

  // Logout
  const logout = () => {
    token.value = null;
    usuario.value = null;
    if (process.client) {
      localStorage.removeItem("auth_token");
      localStorage.removeItem("auth_usuario");
    }
  };

  // Verificar si está autenticado
  const isAuthenticated = () => {
    return token.value !== null;
  };

  return {
    token: readonly(token),
    usuario: readonly(usuario),
    loadToken,
    setToken,
    getUsuario,
    logout,
    isAuthenticated,
  };
};
