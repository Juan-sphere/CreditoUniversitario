<template>
  <div class="w-full">
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
              <h3 class="text-secondary font-bold">Familiar {{ index + 1 }}</h3>
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
              <div class="col-span-4 text-secondary font-bold text-shadow-2xs">
                <h4>Datos Generales</h4>
              </div>
              <div>
                <label class="font-semibold text-sm"
                  >Apellido Paterno <span class="text-red-500">(*)</span></label
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
                  >Apellido Materno <span class="text-red-500">(*)</span></label
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
                  <option value="Pareja de mi madre">Pareja de mi madre</option>
                  <option value="Pareja de mi padre">Pareja de mi padre</option>
                  <option value="Hijo">Hijo</option>
                  <option value="Hija">Hija</option>
                  <option value="Pareja conviviente">Pareja conviviente</option>
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
                  >Tipo de Trabajo <span class="text-red-500">(*)</span></label
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
                  <option value="Si, formal">Sí, Empresa/Negocio formal</option>
                  <option value="No">No tiene</option>
                </select>
              </div>
            </div>

            <!-- Datos Laborales -->
            <div class="grid grid-cols-4 gap-4">
              <div class="col-span-4 text-secondary font-bold text-shadow-2xs">
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
              <div class="col-span-2">
                <label class="font-semibold text-sm">Profesión u Oficio</label>
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
          </div>

          <!-- Botón para agregar familiar -->
          <button
            @click="agregarFamiliar"
            type="button"
            class="px-4 py-2 bg-primary text-white rounded"
          >
            + Agregar otro familiar
          </button>

          <div class="w-full flex justify-end items-center mt-5">
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

interface Familiar {
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
}

const familiares = ref<Familiar[]>([
  {
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
  },
]);

const agregarFamiliar = () => {
  familiares.value.push({
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
  });
};

const eliminarFamiliar = (index: number) => {
  if (familiares.value.length > 1) {
    familiares.value.splice(index, 1);
  }
};
</script>
