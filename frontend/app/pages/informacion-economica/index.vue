<template>
  <div class="w-full">
    <Register :tabs="['Ingresos Familiares', 'Gastos Familiares', 'Balance Presupuesto']" :activeTab="activeTab"
      @tab-change="activeTab = $event">
      <template #register>
        <!-- INGRESOS FAMILIARES -->
        <div class="p-4 space-y-6" v-if="activeTab === 0">
          <h3 class="text-secondary font-bold mb-4">Ingresos Familiares</h3>

          <div v-for="(ingreso, index) in ingresos" :key="index" class="border border-gray-300 rounded p-4 space-y-4">
            <div class="flex justify-between items-center mb-4">
              <span class="font-semibold">Ingreso {{ index + 1 }}</span>
              <button v-if="ingresos.length > 1" @click="eliminarIngreso(index)" type="button"
                class="px-2 py-1 bg-red-500 text-white rounded text-sm">
                Eliminar
              </button>
            </div>

            <div class="grid grid-cols-3 gap-4">
              <div>
                <label class="font-semibold text-sm">Tipo de Ingreso <span class="text-red-500">(*)</span></label>
                <select v-model="ingreso.tipo" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                  <option value="">--Seleccione--</option>
                  <option value="Sueldo mensual en planilla formal">Sueldo mensual en planilla formal de empresa
                  </option>
                  <option value="Sueldo mensual informal dependiente">Sueldo mensual informal dependiente en empresa
                  </option>
                  <option value="Recibo por Honorarios dependiente">Recibo por Honorarios mensual dependiente en empresa
                  </option>
                  <option value="Bonificación formal">Bonificaciones/comisión variable formal (promedio mensualizado)
                  </option>
                  <option value="Bonificación informal">Bonificaciones/comisión variable informal (promedio
                    mensualizado)</option>
                  <option value="Honorarios independiente">Recibo por Honorarios servicios varios independientes
                    (promedio mensualizado)</option>
                  <option value="Ingresos formales negocio">Ingresos formales por negocio/empresa propia (promedio
                    mensualizado)</option>
                  <option value="Ingresos informales negocio">Ingresos informales por negocio/empresa propia (promedio
                    mensualizado)</option>
                  <option value="Ingresos informales servicios">Ingresos mensuales informales por servicios u oficio
                    independiente</option>
                  <option value="Sueldo practicante">Sueldo mensual de practicante pre-profesional o profesional
                  </option>
                  <option value="Bonificación movilidad">Bonificación por movilidad</option>
                  <option value="Pensión jubilación">Pensión/Jubilación</option>
                  <option value="Renta inmuebles">Renta de inmuebles</option>
                  <option value="Renta vehículos">Renta de vehículos/Taxis a terceros</option>
                  <option value="Remesas extranjero">Remesas del extranjero</option>
                  <option value="Pensión alimentos">Pensión de alimentos/separación/divorcio</option>
                  <option value="Sentencia judicial">Sentencia judicial (pensión por alimentos/separación/divorcio)
                  </option>
                  <option value="Vales consumo">Vales de consumo</option>
                  <option value="Vales combustible">Vales de combustible</option>
                  <option value="Apoyo externo">Apoyo económico externo al núcleo familiar</option>
                </select>
              </div>

              <div>
                <label class="font-semibold text-sm">Vinculado a <span class="text-red-500">(*)</span></label>
                <select v-model="ingreso.personaVinculada" class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                  required>
                  <option value="">--Seleccione--</option>
                  <option value="Postulante">Postulante</option>
                  <option value="Familiar familia">Familiar del núcleo familiar</option>
                  <option value="Persona externa">Persona externa de apoyo</option>
                </select>
              </div>

              <div>
                <label class="font-semibold text-sm">Monto en S/. <span class="text-red-500">(*)</span></label>
                <input type="number" v-model="ingreso.monto"
                  class="w-full px-3 py-1 border border-gray-300 rounded mt-1" min="0" step="0.01" required />
              </div>
            </div>
          </div>

          <button @click="agregarIngreso" type="button" class="px-4 py-2 bg-primary text-white rounded">
            + Agregar otro ingreso
          </button>

          <div class="w-full flex justify-end items-center mt-5">
            <button type="submit" class="px-4 py-1 bg-terciary text-white rounded">
              Continuar
            </button>
          </div>
        </div>

        <!-- GASTOS FAMILIARES -->
        <div class="p-4 space-y-6" v-if="activeTab === 1">
          <h3 class="text-secondary font-bold mb-4">Gastos Familiares</h3>

          <div v-for="(gasto, index) in gastos" :key="index" class="border border-gray-300 rounded p-4 space-y-4">
            <div class="flex justify-between items-center mb-4">
              <span class="font-semibold">Gasto {{ index + 1 }}</span>
              <button v-if="gastos.length > 1" @click="eliminarGasto(index)" type="button"
                class="px-2 py-1 bg-red-500 text-white rounded text-sm">
                Eliminar
              </button>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="font-semibold text-sm">Tipo de Gasto <span class="text-red-500">(*)</span></label>
                <select v-model="gasto.tipo" class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                  <option value="">--Seleccione--</option>
                  <option value="Alquiler vivienda">Alquiler de vivienda</option>
                  <option value="Agua">Agua</option>
                  <option value="Luz">Luz</option>
                  <option value="Internet/Cable">Internet/Cable</option>
                  <option value="Teléfonos celulares">Teléfonos celulares</option>
                  <option value="Gas">Gas</option>
                  <option value="Mantenimiento edificio">Mantenimiento en edificio</option>
                  <option value="Alimentación">Alimentación</option>
                  <option value="Útiles limpieza">Útiles de limpieza e higiene</option>
                  <option value="Vestido/Calzado">Vestido/Calzado (monto mensualizado)</option>
                  <option value="Arbitrios/Predial">Arbitrios/Predial (monto mensualizado)</option>
                  <option value="Pensión colegio">Pensión de colegios</option>
                  <option value="Pensión universidad postulante">Pensión de universidad del postulante</option>
                  <option value="Pensión otras universidades">Pensión de otras universidades del núcleo familiar
                  </option>
                  <option value="Pensión academias">Pensión de academias – institutos</option>
                  <option value="Materiales estudio">Materiales de estudio/útiles/separatas (monto mensualizado)
                  </option>
                  <option value="Empleada hogar">Empleada del hogar</option>
                  <option value="Vigilancia/seguridad">Vigilancia/seguridad</option>
                  <option value="Movilidad">Movilidad (combustible, pasajes)</option>
                  <option value="Hipoteca vivienda">Pago de préstamo de hipoteca de la vivienda</option>
                  <option value="Crédito vehicular">Pago de préstamo de crédito vehicular</option>
                  <option value="Otros préstamos formales">Pago de otros préstamos personales o comerciales formales
                  </option>
                  <option value="Tarjetas crédito">Pago de cuotas de tarjetas de crédito</option>
                  <option value="Préstamos informales">Pago de préstamos informales</option>
                  <option value="Salud">Salud (consultas, medicinas, pruebas de laboratorio)</option>
                  <option value="Seguros médicos">Seguros médicos de salud</option>
                  <option value="Seguros vida">Seguros de vida</option>
                  <option value="Entretenimiento">Entretenimiento/Vida social/Vacaciones (monto mensualizado)</option>
                </select>
              </div>

              <div>
                <label class="font-semibold text-sm">Monto en S/. <span class="text-red-500">(*)</span></label>
                <input type="number" v-model="gasto.monto" class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                  min="0" step="0.01" required />
              </div>
            </div>
          </div>

          <button @click="agregarGasto" type="button" class="px-4 py-2 bg-primary text-white rounded">
            + Agregar otro gasto
          </button>

          <div class="w-full flex justify-end items-center mt-5">
            <button type="submit" class="px-4 py-1 bg-terciary text-white rounded">
              Continuar
            </button>
          </div>
        </div>

        <!-- BALANCE PRESUPUESTO -->
        <div class="p-4 space-y-6" v-if="activeTab === 2">
          <h3 class="text-secondary font-bold mb-4">Balance de Presupuesto Familiar</h3>

          <div class="grid grid-cols-3 gap-4 mb-6">
            <div class="border border-gray-300 rounded p-4">
              <label class="font-semibold text-sm text-gray-700">Total de Ingresos (S/.)</label>
              <p class="text-2xl font-bold text-primary mt-2">{{ totalIngresos.toFixed(2) }}</p>
            </div>

            <div class="border border-gray-300 rounded p-4">
              <label class="font-semibold text-sm text-gray-700">Total de Gastos (S/.)</label>
              <p class="text-2xl font-bold text-primary mt-2">{{ totalGastos.toFixed(2) }}</p>
            </div>

            <div class="border border-gray-300 rounded p-4">
              <label class="font-semibold text-sm text-gray-700">Saldo (S/.)</label>
              <p :class="['text-2xl font-bold mt-2', saldo < 0 ? 'text-red-500' : 'text-green-600']">
                {{ saldo < 0 ? '-' : '' }}{{ Math.abs(saldo).toFixed(2) }} </p>
            </div>
          </div>

          <!-- Campo obligatorio si es negativo -->
          <div v-if="saldo < 0" class="border border-red-300 rounded p-4 bg-red-50 space-y-4">
            <label class="font-semibold text-sm text-red-700">
              ¿Cómo se cierra mensualmente el déficit económico familiar? <span class="text-red-500">(*)</span>
            </label>
            <textarea v-model="cierrDeficit" class="w-full px-3 py-2 border border-red-300 rounded" rows="4"
              placeholder="Describa cómo la familia cubre el déficit económico mensual..." required></textarea>
          </div>

          <!-- Observaciones -->
          <div class="space-y-4">
            <label class="font-semibold text-sm">Observaciones y/o comentarios sobre la economía familiar</label>
            <textarea v-model="observaciones" class="w-full px-3 py-2 border border-gray-300 rounded" rows="4"
              placeholder="Comparta observaciones sobre la situación económica familiar..."></textarea>
          </div>

          <div class="w-full flex justify-end items-center mt-5">
            <button type="submit" class="px-4 py-1 bg-terciary text-white rounded">
              Grabar
            </button>
          </div>
        </div>
      </template>
    </Register>

    <div class="flex justify-center items-center">
      <BackNext />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";

interface Ingreso {
  tipo: string;
  personaVinculada: string;
  monto: number | string;
}

interface Gasto {
  tipo: string;
  monto: number | string;
}

const activeTab = ref(0);

const ingresos = ref<Ingreso[]>([
  {
    tipo: "",
    personaVinculada: "",
    monto: ""
  }
]);

const gastos = ref<Gasto[]>([
  {
    tipo: "",
    monto: ""
  }
]);

const cierrDeficit = ref("");
const observaciones = ref("");

const agregarIngreso = () => {
  ingresos.value.push({
    tipo: "",
    personaVinculada: "",
    monto: ""
  });
};

const eliminarIngreso = (index: number) => {
  if (ingresos.value.length > 1) {
    ingresos.value.splice(index, 1);
  }
};

const agregarGasto = () => {
  gastos.value.push({
    tipo: "",
    monto: ""
  });
};

const eliminarGasto = (index: number) => {
  if (gastos.value.length > 1) {
    gastos.value.splice(index, 1);
  }
};

const totalIngresos = computed(() => {
  return ingresos.value.reduce((total, ingreso) => {
    return total + (parseFloat(String(ingreso.monto)) || 0);
  }, 0);
});

const totalGastos = computed(() => {
  return gastos.value.reduce((total, gasto) => {
    return total + (parseFloat(String(gasto.monto)) || 0);
  }, 0);
});

const saldo = computed(() => {
  return totalIngresos.value - totalGastos.value;
});
</script>