<template>
  <div class="w-full">
    <Register :tabs="[
      'Ingresos Familiares',
      'Egresos Familiares',
      'Balance Presupuestal',
    ]" :activeTab="activeTab" @tab-change="activeTab = $event">
      <!-- Slot para Balance Presupuestal -->
      <template v-if="activeTab === 2" #register>
        <div class="flex flex-col w-fit">
          <button class="bg-[#5EC7DC] text-white px-8 py-1 mb-2">
            Ver Resumen de Ingresos
          </button>
          <button class="bg-[#5EC7DC] text-white px-8 py-1">
            Ver Resumen de Egresos
          </button>
        </div>
        <div>
          <h3 class="text-secondary font-semibold my-2">Resumen:</h3>
          <div class="flex justify-between">
            <div class="w-1/3">
              <div class="bg-light p-2 border-b border-gray-300">
                <p class="font-semibold">TOTAL DE INGRESOS</p>
              </div>
              <p class="p-2">S/0.00</p>
            </div>
            <div class="w-1/3 font-semibold">
              <div class="bg-light p-2 border-b border-gray-300">
                <p class="font-semibold">TOTAL DE EGRESOS</p>
              </div>
              <p class="p-2">S/0.00</p>
            </div>
            <div class="w-1/3 text-center">
              <div class="bg-light p-2 border-b border-gray-300">
                <p class="font-semibold">SALDO</p>
              </div>
              <p class="p-2">S/0.00</p>
            </div>
          </div>
        </div>
      </template>
    </Register>

    <!-- Tab 1: Ingresos Familiares -->
    <NuevoRegistro v-if="activeTab === 0" :ifTabs="false" :tabs="[]" title="Ingresos Familiares Mensuales">
      <template #nuevo-registro>
        <div class="grid grid-cols-2 gap-4 p-2">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Concepto <span class="text-red-500">(*)</span></label>
            <select class="w-full px-3 py-1 border border-gray-300 rounded">
              <option>--Seleccione--</option>
              <option>ACCIONES / UTILIDADES</option>
              <option>BONIFICACION POR MOVILIDAD</option>
              <option>BONIFICACIONES</option>
              <option>CONSULTORIAS TECNICAS</option>
              <option>EMPRESAS O NEGOCIOS</option>
              <option>HONORARIOS PROFESIONALES</option>
              <option>INGRESO NO FORMAL</option>
              <option>INGRESO POR EMPRESA/NEGOCIO FORMAL</option>
              <option>INGRESOS POR RECIBOS POR HONORARIOS</option>
              <option>INTERESES DEPOSITOS BANCARIOS</option>
              <option>OTROS</option>
              <option>PENSION / JUBILACION</option>
              <option>PENSION DE ALIMENTOS/SEPARACION/DIVORCIO</option>
              <option>REMESAS DEL EXTRANJERO</option>
              <option>RENTA DE INMUEBLES</option>
              <option>RENTA DE VEHICULOS / TAXI</option>
              <option>SENTENCIA JUDICIAL (PENSION POR ALIMENTOS/SEPARACION/DIVORCIO)</option>
              <option>SUELDOS Y/O SALARIOS</option>
              <option>VALES</option>
              <option>VALES DE COMBUSTIBLE</option>
            </select>
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Monto en Soles(S/) <span class="text-red-500">(*)</span></label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Aportante <span class="text-red-500">(*)</span></label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
        </div>
        <div class="w-full flex justify-between items-center mt-5 pl-2">
          <div>
            <p class="text-white bg-red-500 px-2">Campos Obligatorios (*)</p>
          </div>
          <button type="submit" class="px-4 py-1 bg-terciary text-white">
            Registrar
          </button>
        </div>
      </template>
    </NuevoRegistro>

    <!-- Tab 2: Egresos Familiares -->
    <NuevoRegistro v-if="activeTab === 1" :ifTabs="false" :tabs="[]" title="Egresos Familiares Mensuales">
      <template #nuevo-registro>
        <div class="grid grid-cols-1 gap-4 p-2 overflow-visible">
          <div class="flex flex-col w-1/2 gap-2">
            <label class="text-gray-700 font-semibold">Concepto <span class="text-red-500">(*)</span></label>
            <select class="w-full px-3 py-1 border border-gray-300 rounded relative z-50">
              <option>--Seleccione--</option>
              <option>AGUA Y LUZ</option>
              <option>ALIMENTACION Y VIVIENDA (FORANEOS) N° DE PERSONAS</option>
              <option>ALIMENTACION, GAS, UTILES DE LIMPIEZA - N° DE PERSONAS</option>
              <option>ALQUILER DE VIVIENDA (DE LA FAMILIA)</option>
              <option>ARBITRIOS / PREDIAL (PROMEDIO MENSUAL)</option>
              <option>COLEGIOS</option>
              <option>CUOTAS DE CLUBES</option>
              <option>EMPLEADA DEL HOGAR / VIGILANCIA</option>
              <option>HIPOTECA DE VIVIENDA</option>
              <option>MANTENIMIENTO</option>
              <option>MOVILIDAD (COMBUSTIBLE-MANTENIMIENTO-PASAJES)</option>
              <option>OTROS EGRESOS</option>
              <option>PRESTAMOS BANCARIOS Y COMERCIALES</option>
              <option>SALUD (CONSULTAS - MEDICINAS)</option>
              <option>SEGURO DE VIDA Y/O SEGURO MEDICO</option>
              <option>TARJETA DE CREDITO</option>
              <option>TELEFONOS (FIJO-CELULARES) / CABLE / INTERNET</option>
              <option>TRANSPORTE (TAXI-COLECTIVO-MOTO) / OTROS</option>
              <option>UNIVERSIDADES Y/O INSTITUTOS</option>
              <option>UTILES / SEPARATAS / LIBROS</option>
              <option>VESTIDO / CALZADO</option>
              <option>VIAJES NACIONALES O AL EXTRANJERO; REALIZADOS POR LA PERSONA O FAMILIAR DESDE EL AÑO PASADO
              </option>
            </select>
          </div>
          <div class="flex flex-col w-1/2 gap-2">
            <label class="text-gray-700 font-semibold">Monto en Soles(S/) <span class="text-red-500">(*)</span></label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
        </div>
        <div class="w-full flex justify-between items-center mt-5 pl-2">
          <div>
            <p class="text-white bg-red-500 px-2">Campos Obligatorios (*)</p>
          </div>
          <button type="submit" class="px-4 py-1 bg-terciary text-white">
            Registrar
          </button>
        </div>
      </template>
    </NuevoRegistro>

    <!-- Tab 3: Balance Presupuestal -->
    <NuevoRegistro v-if="activeTab === 2" :ifTabs="false" :tabs="[]" title="Observación:">
      <template #nuevo-registro>
        <div class="grid grid-cols-1 gap-4 p-2">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold">Observaciones sobre Balance Presupuestal (Máximo 500 caracteres)
              (*)</label>
            <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
          </div>
        </div>
        <div class="w-full flex justify-between items-center mt-5 pl-2">
          <div>
            <p class="text-white bg-red-500 px-2">Campos Obligatorios (*)</p>
          </div>
          <button type="submit" class="px-4 py-1 bg-terciary text-white">
            Registrar
          </button>
        </div>
      </template>
    </NuevoRegistro>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const activeTab = ref(0);
</script>
