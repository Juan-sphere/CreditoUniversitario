<template>
  <div class="w-full">
    <!-- Loading Spinner mientras carga datos -->
    <div v-if="cargando" class="flex justify-center items-center h-96">
      <LoadingSpinner />
    </div>

    <!-- Contenido principal -->
    <div v-else>
      <Information title="Composición del núcleo familiar">
        <template #information>
          <div class="p-4 space-y-6 text-gray-700 overflow-hidden">
            <!-- Foreach para cada familiar -->
            <div
              v-for="(familiar, index) in familiares"
              :key="index"
              class="border border-gray-300 rounded p-4 space-y-4"
            >
              <div class="flex justify-between items-center mb-4">
                <h3 class="text-secondary font-bold">
                  Familiar {{ index + 1 }}
                </h3>
                <button
                  v-if="familiares.length > 1"
                  @click="eliminarFamiliar(index)"
                  type="button"
                  class="px-2 py-1 bg-red-500 text-white rounded text-sm"
                >
                  Eliminar
                </button>
              </div>

              <!-- Datos Generales -->
              <div class="grid grid-cols-4 gap-4">
                <div
                  class="col-span-4 text-secondary font-bold text-shadow-2xs"
                >
                  <h4>Datos Generales</h4>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Apellido Paterno
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="familiar.apellidoPaterno"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Apellido Materno
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="familiar.apellidoMaterno"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Nombre <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="familiar.nombre"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm">Segundo Nombre</label>
                  <input
                    type="text"
                    v-model="familiar.segundoNombre"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Parentesco <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.parentesco"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Hermano">Hermano</option>
                    <option value="Hermana">Hermana</option>
                    <option value="Medio hermano">Medio hermano</option>
                    <option value="Media hermana">Media hermana</option>
                    <option value="Pareja de mi madre">
                      Pareja de mi madre
                    </option>
                    <option value="Pareja de mi padre">
                      Pareja de mi padre
                    </option>
                    <option value="Hijo">Hijo</option>
                    <option value="Hija">Hija</option>
                    <option value="Pareja conviviente">
                      Pareja conviviente
                    </option>
                    <option value="Esposa">Esposa</option>
                    <option value="Esposo">Esposo</option>
                    <option value="Hijo(a) de mi pareja">
                      Hijo(a) de mi pareja/esposo/esposa
                    </option>
                    <option value="Abuelo">Abuelo</option>
                    <option value="Abuela">Abuela</option>
                    <option value="Bisabuelo">Bisabuelo</option>
                    <option value="Bisabuela">Bisabuela</option>
                    <option value="Tío">Tío</option>
                    <option value="Tía">Tía</option>
                    <option value="Primo">Primo</option>
                    <option value="Prima">Prima</option>
                    <option value="Sobrino">Sobrino</option>
                    <option value="Sobrina">Sobrina</option>
                    <option value="Cuñado">Cuñado</option>
                    <option value="Cuñada">Cuñada</option>
                    <option value="Tío abuelo">Tío abuelo</option>
                    <option value="Tía abuela">Tía abuela</option>
                    <option value="Otro">Otro</option>
                  </select>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >¿Depende económicamente?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.dependeEconomico"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si">Sí</option>
                    <option value="No">No</option>
                  </select>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Edad <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="number"
                    v-model="familiar.edad"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    min="0"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >¿Estudia? <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.estudia"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si, colegio">Sí, colegio</option>
                    <option value="Si, instituto">
                      Sí, estudia en instituto-academia
                    </option>
                    <option value="Si, universidad">
                      Sí, estudia en universidad
                    </option>
                    <option value="No estudia">No estudia</option>
                  </select>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >¿Trabaja? <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.trabaja"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si">Sí</option>
                    <option value="No">No</option>
                  </select>
                </div>
                <div v-if="familiar.trabaja === 'Si'">
                  <label class="font-semibold text-sm"
                    >Tipo de Trabajo
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.tipoTrabajo"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Independiente informal permanente">
                      Independiente informal permanente
                    </option>
                    <option value="Independiente informal temporal">
                      Independiente informal temporal
                    </option>
                    <option value="Dependiente formal permanente">
                      Dependiente formal permanente
                    </option>
                    <option value="Dependiente formal temporal">
                      Dependiente formal temporal
                    </option>
                  </select>
                </div>
                <div v-if="familiar.trabaja === 'Si'">
                  <label class="font-semibold text-sm"
                    >¿Tiene Empresa/Negocio propio?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.tieneNegocio"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si, informal">
                      Sí, Empresa/Negocio informal
                    </option>
                    <option value="Si, formal">
                      Sí, Empresa/Negocio formal
                    </option>
                    <option value="No">No tiene</option>
                  </select>
                </div>
              </div>

              <!-- Datos Laborales -->
              <div class="grid grid-cols-4 gap-4">
                <div
                  class="col-span-4 text-secondary font-bold text-shadow-2xs"
                >
                  <h4>Datos Laborales y Académicos</h4>
                </div>
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >¿Contribuye a economía familiar?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.contribuyeEconomia"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si">Sí</option>
                    <option value="No">No</option>
                  </select>
                </div>
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >Grado de Instrucción
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.gradoInstruccion"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Sin instrucción">Sin instrucción</option>
                    <option value="Primaria incompleta">
                      Primaria incompleta
                    </option>
                    <option value="Primaria completa">Primaria completa</option>
                    <option value="Secundaria incompleta">
                      Secundaria incompleta
                    </option>
                    <option value="Secundaria completa">
                      Secundaria completa
                    </option>
                    <option value="Técnica incompleta">
                      Técnica incompleta
                    </option>
                    <option value="Técnica completa">Técnica completa</option>
                    <option value="Superior incompleta">
                      Superior incompleta
                    </option>
                    <option value="Superior completa">Superior completa</option>
                    <option value="Postgrado maestría incompleta">
                      Postgrado maestría incompleta
                    </option>
                    <option value="Postgrado maestría completa">
                      Postgrado maestría completa
                    </option>
                    <option value="Postgrado doctorado incompleto">
                      Postgrado doctorado incompleto
                    </option>
                    <option value="Postgrado doctorado completo">
                      Postgrado doctorado completo
                    </option>
                  </select>
                </div>
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >Profesión u Oficio</label
                  >
                  <input
                    type="text"
                    v-model="familiar.profesion"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                  />
                </div>
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >¿Tiene problemas de salud?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="familiar.problemaSalud"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si">Sí</option>
                    <option value="No">No</option>
                  </select>
                </div>
              </div>

              <!-- Botones de Acción -->
              <div class="flex justify-end gap-2 pt-4">
                <button
                  v-if="familiares.length > 1"
                  @click="eliminarFamiliar(index)"
                  type="button"
                  class="px-2 py-1 bg-red-500 text-white rounded text-sm hover:bg-red-600"
                  :disabled="familiar.guardando"
                >
                  Eliminar
                </button>
                <button
                  @click="guardarFamiliar(index)"
                  type="button"
                  class="px-3 py-1 bg-blue-500 text-white rounded text-sm font-semibold hover:bg-blue-600 disabled:opacity-50"
                  :disabled="familiar.guardando"
                >
                  {{
                    familiar.guardando
                      ? "Guardando..."
                      : familiar.id
                        ? "Actualizar"
                        : "Guardar"
                  }}
                </button>
              </div>
            </div>

            <!-- Botón para agregar familiar -->
            <button
              @click="agregarFamiliar"
              type="button"
              class="px-4 py-2 bg-primary text-white rounded"
            >
              + Agregar otro familiar
            </button>
          </div>
        </template>
      </Information>
      <div class="flex justify-center items-center">
        <BackNext />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { toast } from "vue3-toastify";
import Information from "~/components/Information.vue";
import BackNext from "~/components/BackNext.vue";
import LoadingSpinner from "~/components/LoadingSpinner.vue";
import { useAuth } from "~/composables/useAuth";

const config = useRuntimeConfig();
const apiBase = config.public.apiBase as string;
const { token } = useAuth();

interface Familiar {
  id?: number;
  apellidoPaterno: string;
  apellidoMaterno: string;
  nombre: string;
  segundoNombre: string;
  parentesco: string;
  dependeEconomico: string;
  edad: number | string;
  estudia: string;
  trabaja: string;
  tipoTrabajo: string;
  tieneNegocio: string;
  contribuyeEconomia: string;
  gradoInstruccion: string;
  profesion: string;
  problemaSalud: string;
  guardando?: boolean;
}

const familiares = ref<Familiar[]>([]);
const guardandoGlobal = ref(false);
const cargando = ref(false);

// Crear familiar vacío
const crearFamiliarVacio = (): Familiar => ({
  apellidoPaterno: "",
  apellidoMaterno: "",
  nombre: "",
  segundoNombre: "",
  parentesco: "",
  dependeEconomico: "",
  edad: "",
  estudia: "",
  trabaja: "",
  tipoTrabajo: "",
  tieneNegocio: "",
  contribuyeEconomia: "",
  gradoInstruccion: "",
  profesion: "",
  problemaSalud: "",
  guardando: false,
});

// Transformar datos del frontend (camelCase) al backend (snake_case)
const transformarDatos = (familiar: Familiar) => {
  return {
    apellido_paterno: familiar.apellidoPaterno,
    apellido_materno: familiar.apellidoMaterno,
    nombre: familiar.nombre,
    segundo_nombre: familiar.segundoNombre,
    parentesco: familiar.parentesco,
    depende_economicamente: familiar.dependeEconomico === "Si",
    edad: Number(familiar.edad),
    estudia: familiar.estudia === "Si",
    trabaja: familiar.trabaja === "Si",
    tipo_trabajo: familiar.tipoTrabajo,
    tiene_empresa: familiar.tieneNegocio === "Si",
    contribuye_economia: familiar.contribuyeEconomia === "Si",
    grado_instruccion: familiar.gradoInstruccion,
    profesion_oficio: familiar.profesion,
    problemas_salud: familiar.problemaSalud === "Si",
  };
};

// Transformar datos del backend (snake_case) al frontend (camelCase)
const transformarDelBackend = (data: any): Familiar => {
  const familiar: Familiar = {
    id: data.id,
    apellidoPaterno: data.apellido_paterno || "",
    apellidoMaterno: data.apellido_materno || "",
    nombre: data.nombre || "",
    segundoNombre: data.segundo_nombre || "",
    parentesco: data.parentesco || "",
    dependeEconomico: data.depende_economicamente ? "Si" : "No",
    edad: data.edad || "",
    estudia: data.estudia ? "Si" : "No",
    trabaja: data.trabaja ? "Si" : "No",
    tipoTrabajo: data.tipo_trabajo || "",
    tieneNegocio: data.tiene_empresa ? "Si" : "No",
    contribuyeEconomia: data.contribuye_economia ? "Si" : "No",
    gradoInstruccion: data.grado_instruccion || "",
    profesion: data.profesion_oficio || "",
    problemaSalud: data.problemas_salud ? "Si" : "No",
    guardando: false,
  };
  return familiar;
};

// Cargar familiares del backend
const cargarFamiliares = async () => {
  try {
    cargando.value = true;
    const response = await $fetch<any>(`${apiBase}/auth/composicion-familiar`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token.value}`,
      },
    });

    if (response?.data && Array.isArray(response.data)) {
      const familiarTransformados: Familiar[] = response.data.map(
        (item: any): Familiar => transformarDelBackend(item),
      );
      familiares.value = familiarTransformados;
    }

    // Siempre asegurar que hay al menos un formulario vacío para agregar
    if (familiares.value.length === 0) {
      familiares.value = [crearFamiliarVacio()];
    }
  } catch (error: any) {
    console.log("Error al cargar familiares:", error.message);
    familiares.value = [crearFamiliarVacio()];
  } finally {
    cargando.value = false;
  }
};

// Validar campos requeridos
const validarFamiliar = (familiar: Familiar): boolean => {
  const camposRequeridos = [
    { campo: "apellidoPaterno", nombre: "Apellido Paterno" },
    { campo: "apellidoMaterno", nombre: "Apellido Materno" },
    { campo: "nombre", nombre: "Nombre" },
    { campo: "parentesco", nombre: "Parentesco" },
    { campo: "edad", nombre: "Edad" },
    { campo: "gradoInstruccion", nombre: "Grado de Instrucción" },
  ];

  for (const { campo, nombre } of camposRequeridos) {
    const valor = familiar[campo as keyof Familiar];
    if (!valor || valor === "") {
      toast.error(`Por favor completa ${nombre}`);
      return false;
    }
  }
  return true;
};

// Guardar individual
const guardarFamiliar = async (index: number) => {
  const familiar = familiares.value[index];

  if (!validarFamiliar(familiar)) {
    return;
  }

  try {
    familiar.guardando = true;
    const datosTransformados = transformarDatos(familiar);

    if (familiar.id) {
      // Actualizar
      await $fetch(`${apiBase}/auth/composicion-familiar/${familiar.id}`, {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
        body: datosTransformados,
      });
      toast.success("✓ Familiar actualizado");
    } else {
      // Crear
      const response = await $fetch<any>(
        `${apiBase}/auth/composicion-familiar`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
          body: datosTransformados,
        },
      );

      if (response?.data?.id) {
        familiar.id = response.data.id;
      }

      toast.success("✓ Familiar agregado");
    }

    // Recargar para sincronizar
    await cargarFamiliares();
  } catch (error: any) {
    console.error("Error al guardar:", error);
    toast.error(
      error.data?.detail || "Error al guardar la información del familiar",
    );
  } finally {
    familiar.guardando = false;
  }
};

// Eliminar familiar
const eliminarFamiliar = async (index: number) => {
  const familiar = familiares.value[index];

  // Solo permitir eliminar si hay más de 1 familiar Y existe en la base de datos
  if (familiares.value.length === 1) {
    toast.error("Debe haber al menos un familiar");
    return;
  }

  // Si no tiene ID, simplemente eliminar del frontend
  if (!familiar.id) {
    familiares.value.splice(index, 1);
    return;
  }

  if (
    !confirm(
      `¿Estás seguro que deseas eliminar a ${familiar.nombre} ${familiar.apellidoPaterno}?`,
    )
  ) {
    return;
  }

  try {
    await $fetch(`${apiBase}/auth/composicion-familiar/${familiar.id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token.value}`,
      },
    });

    toast.success("✓ Familiar eliminado");
    familiares.value.splice(index, 1);
  } catch (error: any) {
    console.error("Error al eliminar:", error);
    toast.error(error.data?.detail || "Error al eliminar el familiar");
  }
};

// Agregar formulario vacío
const agregarFamiliar = () => {
  familiares.value.push(crearFamiliarVacio());
};

// Grabar todos (mejor guardado individual)
const grabarTodos = async () => {
  try {
    guardandoGlobal.value = true;

    // Guardar todos los familiares que no tengan ID (nuevos)
    for (let i = 0; i < familiares.value.length; i++) {
      const familiar = familiares.value[i];
      if (!familiar.id) {
        await guardarFamiliar(i);
      }
    }

    toast.success("✓ Todos los familiares guardados");
  } catch (error: any) {
    console.error("Error general:", error);
    toast.error("Error al guardar los familiares");
  } finally {
    guardandoGlobal.value = false;
  }
};

onMounted(() => {
  cargarFamiliares();
});
</script>
