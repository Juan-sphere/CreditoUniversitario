<template>
  <div class="flex flex-col gap-2">
    <label class="text-gray-700 font-semibold">
      {{ label }}
      <span v-if="required" class="text-red-500">(*)</span>
    </label>
    <select
      :value="modelValue"
      @input="
        $emit('update:modelValue', ($event.target as HTMLSelectElement).value)
      "
      :required="required"
      class="w-full px-3 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
    >
      <option value="">--Seleccione--</option>
      <option
        v-for="department in departments"
        :key="department"
        :value="department"
      >
        {{ department }}
      </option>
    </select>
  </div>
</template>

<script setup lang="ts">
import { peruDepartments } from "@/utils/peru-provinces";

defineProps({
  modelValue: {
    type: String,
    default: "",
  },
  label: {
    type: String,
    default: "Departamento",
  },
  required: {
    type: Boolean,
    default: false,
  },
});

defineEmits(["update:modelValue"]);

const departments = peruDepartments;
</script>

<style scoped></style>
