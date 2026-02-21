<template>
  <div class="w-full">
    <!-- Loading Spinner mientras carga datos -->
    <div v-if="cargando" class="flex justify-center items-center h-96">
      <LoadingSpinner />
    </div>

    <!-- Contenido principal -->
    <div v-else>
      <Information
        title="Personas que contribuyen externamente a la economía familiar"
      >
        <template #information>
          <div class="p-4 space-y-6 text-gray-700 overflow-hidden">
            <!-- Foreach para cada persona externa -->
            <div
              v-for="(persona, index) in personasExternas"
              :key="index"
              class="border border-gray-300 rounded p-4 space-y-4"
            >
              <div class="flex justify-between items-center mb-4">
                <h3 class="text-secondary font-bold">
                  Persona Externa {{ index + 1 }}
                </h3>
                <button
                  v-if="personasExternas.length > 1"
                  @click="eliminarPersona(index)"
                  type="button"
                  class="px-2 py-1 bg-red-500 text-white rounded text-sm hover:bg-red-600"
                  :disabled="persona.guardando"
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
                    v-model="persona.apellidoPaterno"
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
                    v-model="persona.apellidoMaterno"
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
                    v-model="persona.nombre"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm">Segundo Nombre</label>
                  <input
                    type="text"
                    v-model="persona.segundoNombre"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Parentesco o Relación
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="persona.parentesco"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Amigo del postulante">
                      Amigo del postulante
                    </option>
                    <option value="Amigo de la familia">
                      Amigo de la familia
                    </option>
                    <option value="Hermano">Hermano</option>
                    <option value="Hermana">Hermana</option>
                    <option value="Cuñado">Cuñado</option>
                    <option value="Cuñada">Cuñada</option>
                    <option value="Medio hermano">Medio hermano</option>
                    <option value="Media hermana">Media hermana</option>
                    <option value="Pareja de mi madre">
                      Pareja de mi madre
                    </option>
                    <option value="Pareja de mi padre">
                      Pareja de mi padre
                    </option>
                    <option value="Abuelo">Abuelo</option>
                    <option value="Abuela">Abuela</option>
                    <option value="Bisabuelo">Bisabuelo</option>
                    <option value="Bisabuela">Bisabuela</option>
                    <option value="Tío">Tío</option>
                    <option value="Tía">Tía</option>
                    <option value="Primo">Primo</option>
                    <option value="Prima">Prima</option>
                    <option value="Tío abuelo">Tío abuelo</option>
                    <option value="Tía abuela">Tía abuela</option>
                    <option value="Otro">Otro</option>
                  </select>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Edad <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="number"
                    v-model="persona.edad"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    min="0"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >¿Trabaja? <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="persona.trabaja"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si">Sí</option>
                    <option value="No">No</option>
                  </select>
                </div>
                <div v-if="persona.trabaja === 'Si'">
                  <label class="font-semibold text-sm"
                    >Tipo de Trabajo
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="persona.tipoTrabajo"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Independiente permanente">
                      Independiente permanente
                    </option>
                    <option value="Independiente temporal">
                      Independiente temporal
                    </option>
                    <option value="Dependiente permanente">
                      Dependiente permanente
                    </option>
                    <option value="Dependiente temporal">
                      Dependiente temporal
                    </option>
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
                <div class="col-span-3">
                  <label class="font-semibold text-sm"
                    >Grado de Instrucción
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="persona.gradoInstruccion"
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
                <div class="col-span-1"></div>
                <div class="col-span-4">
                  <label class="font-semibold text-sm"
                    >Profesión u Oficio</label
                  >
                  <input
                    type="text"
                    v-model="persona.profesion"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                  />
                </div>
              </div>

              <!-- Botones de Acción -->
              <div class="flex justify-end gap-2 pt-4">
                <button
                  v-if="personasExternas.length > 1"
                  @click="eliminarPersona(index)"
                  type="button"
                  class="px-2 py-1 bg-red-500 text-white rounded text-sm hover:bg-red-600"
                  :disabled="persona.guardando"
                >
                  Eliminar
                </button>
                <button
                  @click="guardarPersona(index)"
                  type="button"
                  class="px-3 py-1 bg-blue-500 text-white rounded text-sm font-semibold hover:bg-blue-600 disabled:opacity-50"
                  :disabled="persona.guardando"
                >
                  {{
                    persona.guardando
                      ? "Guardando..."
                      : persona.id
                        ? "Actualizar"
                        : "Guardar"
                  }}
                </button>
              </div>
            </div>

            <!-- Botón para agregar persona -->
            <button
              @click="agregarPersona"
              type="button"
              class="px-4 py-2 bg-primary text-white rounded"
            >
              + Agregar otra persona externa
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

interface PersonaExterna {
  id?: number;
  apellidoPaterno: string;
  apellidoMaterno: string;
  nombre: string;
  segundoNombre: string;
  parentesco: string;
  edad: number | string;
  trabaja: string;
  tipoTrabajo: string;
  gradoInstruccion: string;
  profesion: string;
  guardando?: boolean;
}

const personasExternas = ref<PersonaExterna[]>([]);
const cargando = ref(false);

// Crear persona externa vacía
const crearPersonaVacia = (): PersonaExterna => ({
  apellidoPaterno: "",
  apellidoMaterno: "",
  nombre: "",
  segundoNombre: "",
  parentesco: "",
  edad: "",
  trabaja: "",
  tipoTrabajo: "",
  gradoInstruccion: "",
  profesion: "",
  guardando: false,
});

// Transformar datos del frontend (camelCase) al backend (snake_case)
const transformarDatos = (persona: PersonaExterna) => {
  return {
    apellido_paterno: persona.apellidoPaterno,
    apellido_materno: persona.apellidoMaterno,
    nombre: persona.nombre,
    segundo_nombre: persona.segundoNombre,
    parentesco_relacion: persona.parentesco,
    edad: Number(persona.edad),
    trabaja: persona.trabaja === "Si",
    tipo_trabajo: persona.trabaja === "Si" ? persona.tipoTrabajo : null,
    grado_instruccion: persona.gradoInstruccion,
    profesion_oficio: persona.profesion,
  };
};

// Transformar datos del backend (snake_case) al frontend (camelCase)
const transformarDelBackend = (data: any): PersonaExterna => {
  const persona: PersonaExterna = {
    id: data.id,
    apellidoPaterno: data.apellido_paterno || "",
    apellidoMaterno: data.apellido_materno || "",
    nombre: data.nombre || "",
    segundoNombre: data.segundo_nombre || "",
    parentesco: data.parentesco_relacion || "",
    edad: data.edad || "",
    trabaja: data.trabaja ? "Si" : "No",
    tipoTrabajo: data.tipo_trabajo || "",
    gradoInstruccion: data.grado_instruccion || "",
    profesion: data.profesion_oficio || "",
    guardando: false,
  };
  return persona;
};

// Cargar personas externas del backend
const cargarPersonas = async () => {
  try {
    cargando.value = true;
    const response = await $fetch<any>(`${apiBase}/auth/personas-externas`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token.value}`,
      },
    });

    if (response?.data && Array.isArray(response.data)) {
      const personasTransformadas: PersonaExterna[] = response.data.map(
        (item: any): PersonaExterna => transformarDelBackend(item),
      );
      personasExternas.value = personasTransformadas;
    }

    // Siempre asegurar que hay al menos un formulario vacío para agregar
    if (personasExternas.value.length === 0) {
      personasExternas.value = [crearPersonaVacia()];
    }
  } catch (error: any) {
    console.log("Error al cargar personas externas:", error.message);
    personasExternas.value = [crearPersonaVacia()];
  } finally {
    cargando.value = false;
  }
};

// Validar campos requeridos
const validarPersona = (persona: PersonaExterna): boolean => {
  const camposRequeridos = [
    { campo: "apellidoPaterno", nombre: "Apellido Paterno" },
    { campo: "apellidoMaterno", nombre: "Apellido Materno" },
    { campo: "nombre", nombre: "Nombre" },
    { campo: "parentesco", nombre: "Parentesco o Relación" },
    { campo: "edad", nombre: "Edad" },
    { campo: "gradoInstruccion", nombre: "Grado de Instrucción" },
  ];

  for (const { campo, nombre } of camposRequeridos) {
    const valor = persona[campo as keyof PersonaExterna];
    if (!valor || valor === "") {
      toast.error(`Por favor completa ${nombre}`);
      return false;
    }
  }

  if (persona.trabaja === "Si" && !persona.tipoTrabajo) {
    toast.error("Por favor indica el tipo de trabajo");
    return false;
  }

  return true;
};

// Guardar individual
const guardarPersona = async (index: number) => {
  const persona = personasExternas.value[index];

  if (!validarPersona(persona)) {
    return;
  }

  try {
    persona.guardando = true;
    const datosTransformados = transformarDatos(persona);

    if (persona.id) {
      // Actualizar
      await $fetch(`${apiBase}/auth/personas-externas/${persona.id}`, {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
        body: datosTransformados,
      });
      toast.success("✓ Persona externa actualizada");
    } else {
      // Crear
      const response = await $fetch<any>(`${apiBase}/auth/personas-externas`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
        body: datosTransformados,
      });

      if (response?.data?.id) {
        persona.id = response.data.id;
      }

      toast.success("✓ Persona externa agregada");
    }

    // Recargar para sincronizar
    await cargarPersonas();
  } catch (error: any) {
    console.error("Error al guardar:", error);
    toast.error(
      error.data?.detail || "Error al guardar la información de la persona",
    );
  } finally {
    persona.guardando = false;
  }
};

// Eliminar persona
const eliminarPersona = async (index: number) => {
  const persona = personasExternas.value[index];

  // Solo permitir eliminar si hay más de 1 persona Y existe en la base de datos
  if (personasExternas.value.length === 1) {
    toast.error("Debe haber al menos una persona");
    return;
  }

  // Si no tiene ID, simplemente eliminar del frontend
  if (!persona.id) {
    personasExternas.value.splice(index, 1);
    return;
  }

  if (
    !confirm(
      `¿Estás seguro que deseas eliminar a ${persona.nombre} ${persona.apellidoPaterno}?`,
    )
  ) {
    return;
  }

  try {
    await $fetch(`${apiBase}/auth/personas-externas/${persona.id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token.value}`,
      },
    });

    toast.success("✓ Persona externa eliminada");
    personasExternas.value.splice(index, 1);
  } catch (error: any) {
    console.error("Error al eliminar:", error);
    toast.error(error.data?.detail || "Error al eliminar la persona");
  }
};

// Agregar formulario vacío
const agregarPersona = () => {
  personasExternas.value.push(crearPersonaVacia());
};

onMounted(() => {
  cargarPersonas();
});
</script>
