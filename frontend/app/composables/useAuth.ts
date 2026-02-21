export const useAuth = () => {
  const config = useRuntimeConfig();
  const apiBase = config.public.apiBase;

  // Usar cookies en lugar de localStorage (más seguro)
  const tokenCookie = useCookie<string | null>("auth_token", {
    maxAge: 60 * 60 * 24, // 24 horas
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
  });

  const usuarioCookie = useCookie<any>("auth_usuario", {
    maxAge: 60 * 60 * 24, // 24 horas
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
  });

  const token = useState<string | null>("auth.token", () => tokenCookie.value);
  const usuario = useState<any>("auth.usuario", () => usuarioCookie.value);

  // Cargar token desde cookies (sincronizar estado)
  const loadToken = () => {
    if (tokenCookie.value) {
      token.value = tokenCookie.value;
    }
    if (usuarioCookie.value) {
      usuario.value = usuarioCookie.value;
    }
  };

  // Guardar token en cookies
  const setToken = (newToken: string, userData: any = null) => {
    token.value = newToken;
    tokenCookie.value = newToken;

    if (userData) {
      usuario.value = userData;
      usuarioCookie.value = userData;
    }
  };

  // Obtener usuario actual
  const getUsuario = async () => {
    if (!token.value) return null;

    try {
      const response = await $fetch<{ usuario: any }>("/auth/me", {
        baseURL: apiBase,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (response?.usuario) {
        usuario.value = response.usuario;
        usuarioCookie.value = response.usuario;
      }
      return response?.usuario;
    } catch (error) {
      console.error("Error obteniendo usuario:", error);
      return null;
    }
  };

  // Logout - limpia cookies y estado
  const logout = () => {
    token.value = null;
    usuario.value = null;
    tokenCookie.value = null;
    usuarioCookie.value = null;
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
