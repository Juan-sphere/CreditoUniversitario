<template>
  <div class="w-full">
    <Register
      :tabs="[
        'Ingresos Familiares',
        'Egresos Familiares',
        'Balance Presupuestal',
      ]"
    />
    <NuevoRegistro
      :ifTabs="false"
      :tabs="[]"
      title="Ingresos Familiares Mensuales"
    >
      <template #nuevo-registro>
        <div class="grid grid-cols-2 gap-4 p-2">
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Concepto <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Monto en Soles(S/) <span class="text-red-500">(*)</span></label
            >
            <select class="w-full px-3 py-1 border border-gray-300 rounded">
              <option>--Seleccione--</option>
            </select>
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-gray-700 font-semibold"
              >Aportante <span class="text-red-500">(*)</span></label
            >
            <input
              type="text"
              class="w-full px-3 py-1 border border-gray-300 rounded"
            />
          </div>
        </div>
        <div class="w-full flex justify-between items-center mt-5 pl-2">
          <div>
            <p class="text-white bg-red-500">Campos Obligatorios (*)</p>
          </div>
          <button type="submit" class="px-4 py-1 bg-terciary text-white">
            Registrar
          </button>
        </div>
      </template>
    </NuevoRegistro>
  </div>
</template>
