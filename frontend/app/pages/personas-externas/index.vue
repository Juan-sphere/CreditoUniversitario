<template>
  <div class="w-full">
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
                class="px-2 py-1 bg-red-500 text-white rounded text-sm"
              >
                Eliminar
              </button>
            </div>

            <!-- Datos Generales -->
            <div class="grid grid-cols-4 gap-4">
              <div class="col-span-4 text-secondary font-bold text-shadow-2xs">
                <h4>Datos Generales</h4>
              </div>
              <div>
                <label class="font-semibold text-sm"
                  >Apellido Paterno <span class="text-red-500">(*)</span></label
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
                  >Apellido Materno <span class="text-red-500">(*)</span></label
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
                  <option value="Pareja de mi madre">Pareja de mi madre</option>
                  <option value="Pareja de mi padre">Pareja de mi padre</option>
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
                  >Tipo de Trabajo <span class="text-red-500">(*)</span></label
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
              <div class="col-span-4 text-secondary font-bold text-shadow-2xs">
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
                  <option value="Técnica incompleta">Técnica incompleta</option>
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
                <label class="font-semibold text-sm">Profesión u Oficio</label>
                <input
                  type="text"
                  v-model="persona.profesion"
                  class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                />
              </div>
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

          <div class="w-full flex justify-between items-center mt-5">
            <CampoObligatorio />
            <button type="submit" class="px-4 py-1 bg-terciary text-white">
              Grabar
            </button>
          </div>
        </div>
      </template>
    </Information>
    <div class="flex justify-center items-center">
      <BackNext />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

interface PersonaExterna {
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
}

const personasExternas = ref<PersonaExterna[]>([
  {
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
  },
]);

const agregarPersona = () => {
  personasExternas.value.push({
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
  });
};

const eliminarPersona = (index: number) => {
  if (personasExternas.value.length > 1) {
    personasExternas.value.splice(index, 1);
  }
};
</script>
