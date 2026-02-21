import { ref } from "vue";
import { toast } from "vue3-toastify";
import { useAuth } from "~/composables/useAuth";

interface Documento {
  id: number;
  tipo_documento: string;
  nombre_original: string;
  object_name: string;
  mime_type: string;
  size_bytes: number;
  estado: string;
  bucket_name: string;
}

const BUCKET_NAME = "credito-universitario-docs-2026";
const DOCUMENT_TYPES = [
  "ingresos",
  "boletas",
  "pdt",
  "tributario",
  "rus",
  "terceros",
  "honorarios",
  "servicio",
];

export const useRequiredDocuments = () => {
  const config = useRuntimeConfig();
  const apiBase = config.public.apiBase as string;
  const { token } = useAuth();

  const documentos = ref<Documento[]>([]);
  const cargando = ref(false);
  const cargandoArchivos = ref(false);

  // Cargar todos los documentos del usuario
  const cargarDocumentos = async () => {
    try {
      cargando.value = true;
      const response = await $fetch<any>(
        `${apiBase}/auth/documentos-sustentacion`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );

      if (response?.data && Array.isArray(response.data)) {
        documentos.value = response.data;
      }
      return response?.data || [];
    } catch (error: any) {
      console.error("[useRequiredDocuments] Error al cargar:", error.message);
      toast.error("Error al cargar los documentos");
      return [];
    } finally {
      cargando.value = false;
    }
  };

  // Cargar documentos de un tipo específico
  const cargarDocumentosPorTipo = async (tipo: string) => {
    try {
      const response = await $fetch<any>(
        `${apiBase}/auth/documentos-sustentacion/tipo/${tipo}`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );
      return response?.data || [];
    } catch (error: any) {
      console.error("[useRequiredDocuments] Error al cargar por tipo:", error);
      return [];
    }
  };

  // Obtener un documento específico
  const obtenerDocumento = async (id: number) => {
    try {
      const response = await $fetch<any>(
        `${apiBase}/auth/documentos-sustentacion/${id}`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );
      return response?.data;
    } catch (error: any) {
      console.error("[useRequiredDocuments] Error al obtener:", error);
      return null;
    }
  };

  // Crear documento (carga archivo)
  const crearDocumento = async (
    tipoDocumento: string,
    nombreOriginal: string,
    mimeType: string,
    sizeBytes: number,
    objectName?: string,
  ) => {
    try {
      cargandoArchivos.value = true;
      const response = await $fetch<any>(
        `${apiBase}/auth/documentos-sustentacion`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
          body: {
            tipo_documento: tipoDocumento,
            bucket_name: BUCKET_NAME,
            object_name:
              objectName ||
              `usuarios/${token.value}/${tipoDocumento}/${Date.now()}-${nombreOriginal}`,
            nombre_original: nombreOriginal,
            mime_type: mimeType,
            size_bytes: sizeBytes,
          },
        },
      );

      if (response?.data?.id) {
        documentos.value.push({
          id: response.data.id,
          tipo_documento: tipoDocumento,
          nombre_original: nombreOriginal,
          object_name: response.data.object_name,
          mime_type: mimeType,
          size_bytes: sizeBytes,
          estado: "PENDIENTE",
          bucket_name: BUCKET_NAME,
        });
        toast.success(`✓ ${nombreOriginal} cargado exitosamente`);
        return response.data;
      }
      return null;
    } catch (error: any) {
      console.error("[useRequiredDocuments] Error al crear:", error);
      toast.error(error.data?.detail || "Error al cargar el documento");
      return null;
    } finally {
      cargandoArchivos.value = false;
    }
  };

  // Actualizar documento (estado, observaciones)
  const actualizarDocumento = async (
    id: number,
    estado?: string,
    observaciones?: string,
  ) => {
    try {
      const response = await $fetch<any>(
        `${apiBase}/auth/documentos-sustentacion/${id}`,
        {
          method: "PUT",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
          body: {
            estado: estado,
            observaciones: observaciones,
          },
        },
      );

      if (response?.data) {
        // Actualizar en lista local
        const index = documentos.value.findIndex((d) => d.id === id);
        if (index > -1 && estado) {
          const doc = documentos.value[index];
          if (doc) {
            doc.estado = estado;
          }
        }
        toast.success("Documento actualizado");
        return response.data;
      }
      return null;
    } catch (error: any) {
      console.error("[useRequiredDocuments] Error al actualizar:", error);
      toast.error("Error al actualizar el documento");
      return null;
    }
  };

  // Eliminar documento
  const eliminarDocumento = async (id: number) => {
    try {
      const response = await $fetch<any>(
        `${apiBase}/auth/documentos-sustentacion/${id}`,
        {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        },
      );

      if (response?.success) {
        documentos.value = documentos.value.filter((d) => d.id !== id);
        toast.success("Documento eliminado");
        return true;
      }
      return false;
    } catch (error: any) {
      console.error("[useRequiredDocuments] Error al eliminar:", error);
      toast.error("Error al eliminar el documento");
      return false;
    }
  };

  return {
    documentos,
    cargando,
    cargandoArchivos,
    BUCKET_NAME,
    DOCUMENT_TYPES,
    cargarDocumentos,
    cargarDocumentosPorTipo,
    obtenerDocumento,
    crearDocumento,
    actualizarDocumento,
    eliminarDocumento,
  };
};
