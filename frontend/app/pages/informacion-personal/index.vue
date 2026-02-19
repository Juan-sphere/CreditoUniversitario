<template>
  <div class="w-full">
    <Information title="Información personal">
      <template #information>
        <div class="grid grid-cols-4 gap-4 p-4">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Apellido paterno</label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Apellido materno</label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Nombre</label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Segundo nombre</label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
          <div class="col-span-1 flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">DNI</label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
          <div class="col-span-2 flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Correo electrónico universidad</label>
            <input type="email" class="w-full px-3 py-1 border border-gray-300 rounded" required />
          </div>
        </div>
      </template>
    </Information>

    <!-- <div class="w-full flex justify-end mt-4">
      <button type="submit" class="px-4 py-1 bg-terciary text-white rounded">
        Editar
      </button>
    </div> -->

    <Register :tabs="[
      'Información adicional',
      'Correo electrónico',
      'Dirección',
      'Datos laborales',
    ]" :activeTab="activeTab" @tab-change="activeTab = $event">
      <template #register>
        <!-- Información adicional -->
        <div class="p-2" v-if="activeTab === 0">
          <div class="grid grid-cols-2 gap-4">
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Estado Civil <span class="text-red-500">(*)</span></label>
              <select class="w-full px-3 py-1 border border-gray-300 rounded">
                <option>--Seleccione--</option>
                <option>Soltero(a)</option>
                <option>Casado(a)</option>
                <option>Divorciado(a)</option>
                <option>Viudo(a)</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Es conviviente? <span class="text-red-500">(*)</span></label>
              <select class="w-full px-3 py-1 border border-gray-300 rounded">
                <option>--Seleccione--</option>
                <option>Sí</option>
                <option>No</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Fecha de nacimiento
                <span class="text-red-500">(*)</span></label>
              <input type="date" class="w-full px-3 py-1 border border-gray-300 rounded" />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Lugar de nacimiento
                <span class="text-red-500">(*)</span></label>
              <select class="w-full px-3 py-1 border border-gray-300 rounded">
                <option>--Seleccione--</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Sexo <span class="text-red-500">(*)</span></label>
              <select class="w-full px-3 py-1 border border-gray-300 rounded">
                <option>--Seleccione--</option>
                <option>Masculino</option>
                <option>Femenino</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Telefono celular <span class="text-red-500">(*)</span></label>
              <input type="number" class="w-full px-3 py-1 border border-gray-300 rounded" min="0" required />
            </div>
          </div>
          <div class="w-full flex justify-between items-center mt-5">
            <CampoObligatorio />
            <button type="submit" class="px-4 py-1 bg-terciary text-white">
              Registrar
            </button>
          </div>
        </div>
        <!-- Correo electrónico universidad -->
        <div class="p-2" v-if="activeTab === 1">
          <div class="grid grid-cols-2 gap-4">
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Correo electrónico personal
                <span class="text-red-500">(*)</span></label>
              <input type="email" class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="usuario@dominio.com" required />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Correo electrónico laboral
                <span class="text-red-500">(*)</span></label>
              <input type="email" class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="usuario@dominio.com" required />
            </div>
          </div>
          <div class="w-full flex justify-between items-center mt-5">
            <CampoObligatorio />
            <button type="submit" class="px-4 py-1 bg-terciary text-white">
              Registrar
            </button>
          </div>
        </div>
        <!-- Dirección -->
        <div class="p-2" v-if="activeTab === 2">
          <div class="grid grid-cols-2 gap-4">
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Tipo de vía <span class="text-red-500">(*)</span></label>
              <select class="w-full px-3 py-1 border border-gray-300 rounded" required>
                <option>--Seleccione--</option>
                <option>Calle</option>
                <option>Pasaje</option>
                <option>Jirón</option>
                <option>Avenida</option>
                <option>Sin nombre</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Nombre de la vía <span class="text-red-500">(*)</span></label>
              <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="Nombre de la calle o avenida" required />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Número de vivienda <span
                  class="text-red-500">(*)</span></label>
              <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="Número del domicilio" required />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Urbanización <span class="text-red-500">(*)</span></label>
              <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="Nombre de urbanización" required />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Distrito <span class="text-red-500">(*)</span></label>
              <select class="w-full px-3 py-1 border border-gray-300 rounded" required>
                <option>--Seleccione--</option>
                <option>Ancón</option>
                <option>Ate</option>
                <option>Barranco</option>
                <option>Breña</option>
                <option>Carabayllo</option>
                <option>Chaclacayo</option>
                <option>Chorrillos</option>
                <option>Comas</option>
                <option>Cono Este</option>
                <option>Cono Norte</option>
                <option>Cono Oeste</option>
                <option>El Agustino</option>
                <option>Huacho</option>
                <option>Junín</option>
                <option>La Caleta</option>
                <option>La Molina</option>
                <option>La Perla</option>
                <option>La Punta</option>
                <option>Lince</option>
                <option>Lurín</option>
                <option>Lima</option>
                <option>Los Olivos</option>
                <option>Magdalena</option>
                <option>Magdalena del Mar</option>
                <option>Miraflores</option>
                <option>Pachacamac</option>
                <option>Pucusana</option>
                <option>Puente Piedra</option>
                <option>Punta Hermosa</option>
                <option>Punta Negra</option>
                <option>Rímac</option>
                <option>San Bartolo</option>
                <option>San Isidro</option>
                <option>San Martín de Porres</option>
                <option>San Miguel</option>
                <option>Santa Anita</option>
                <option>Santa María del Mar</option>
                <option>Santa Rosa</option>
                <option>Santiago de Surco</option>
                <option>Surquillo</option>
                <option>Villa El Salvador</option>
                <option>Villa María del Triunfo</option>
                <option>Vitarte</option>
              </select>
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Referencia de dirección</label>
              <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded"
                placeholder="Ej: Cerca del parque, esquina con..." />
            </div>
          </div>
          <div class="w-full flex justify-between items-center mt-5">
            <CampoObligatorio />
            <button type="submit" class="px-4 py-1 bg-terciary text-white">
              Registrar
            </button>
          </div>
        </div>
        <!-- Datos laborales -->
        <div class="flex flex-col gap-4 p-2" v-if="activeTab === 3">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">¿El postulante trabaja?
              <span class="text-red-500">(*)</span></label>
            <select v-model="postulanteTrabaja" class="w-full px-3 py-1 border border-gray-300 rounded" required>
              <option value="">--Seleccione--</option>
              <option value="Si">Sí</option>
              <option value="No">No</option>
            </select>
          </div>

          <template v-if="postulanteTrabaja === 'Si'">
            <div>
              <label class="text-gray-700 font-semibold">Tipo de trabajo <span class="text-red-500">(*)</span></label>
              <div class="grid grid-cols-1 gap-2 mt-2 pl-2">
                <div class="flex items-center">
                  <input type="checkbox" id="trabajo1" value="Trabajo dependiente formal en planilla"
                    v-model="tiposTrabajo" class="w-4 h-4" />
                  <label for="trabajo1" class="ml-2 text-gray-700">Trabajo dependiente formal en planilla</label>
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="trabajo2" value="Trabajo dependiente formal en Recibo por Honorarios"
                    v-model="tiposTrabajo" class="w-4 h-4" />
                  <label for="trabajo2" class="ml-2 text-gray-700">Trabajo dependiente formal en Recibo por
                    Honorarios</label>
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="trabajo3" value="Trabajo dependiente informal" v-model="tiposTrabajo"
                    class="w-4 h-4" />
                  <label for="trabajo3" class="ml-2 text-gray-700">Trabajo dependiente informal</label>
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="trabajo4" value="Trabajo independiente informal" v-model="tiposTrabajo"
                    class="w-4 h-4" />
                  <label for="trabajo4" class="ml-2 text-gray-700">Trabajo independiente informal</label>
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="trabajo5" value="Empresa/Negocio propio formal" v-model="tiposTrabajo"
                    class="w-4 h-4" />
                  <label for="trabajo5" class="ml-2 text-gray-700">Empresa/Negocio propio formal</label>
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="trabajo6" value="Empresa/Negocio propio informal" v-model="tiposTrabajo"
                    class="w-4 h-4" />
                  <label for="trabajo6" class="ml-2 text-gray-700">Empresa/Negocio propio informal</label>
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="trabajo7" value="Practicante pre-profesional" v-model="tiposTrabajo"
                    class="w-4 h-4" />
                  <label for="trabajo7" class="ml-2 text-gray-700">Practicante pre-profesional</label>
                </div>
              </div>
            </div>

            <div class="flex flex-col gap-2">
              <label class="text-gray-700 font-semibold">Ingresos mensuales (S/.)
                <span class="text-red-500">(*)</span></label>
              <input type="number" class="w-full px-3 py-1 border border-gray-300 rounded" placeholder="Ej: 2500.00"
                min="0" step="0.01" required />
            </div>
          </template>

          <div class="w-full flex justify-between items-center mt-5 pl-2">
            <CampoObligatorio />
            <button type="submit" class="px-4 py-1 bg-terciary text-white">
              Registrar
            </button>
          </div>
        </div>
      </template>
    </Register>

    <div class="flex items-center justify-end mt-4">
      <button class="px-4 py-1 bg-terciary text-white rounded">Grabar</button>
    </div>

    <BackNext />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const activeTab = ref(0);
const postulanteTrabaja = ref("");
const tiposTrabajo = ref<string[]>([]);
</script>
