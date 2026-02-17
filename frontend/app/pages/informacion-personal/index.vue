<template>
    <div class="w-full">
        <Information title="Información personal">
            <template #information>
                <div class="grid grid-cols-2 gap-4">
                    <div class="grid grid-cols-[auto_1fr] gap-x-4 gap-y-2 items-center">
                        <label class="text-gray-700 font-semibold">Nombre</label>
                        <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        <label class="text-gray-700 font-semibold">DNI</label>
                        <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        <label class="text-gray-700 font-semibold">Fecha de nacimiento</label>
                        <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                    </div>
                    <div class="grid grid-cols-[auto_1fr] gap-x-4 gap-y-2 items-center self-start">
                        <label class="text-gray-700 font-semibold">Género</label>
                        <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                        <label class="text-gray-700 font-semibold">Lugar de Nacimiento</label>
                        <input type="text" class="w-full px-3 py-1 border border-gray-300 rounded" />
                    </div>
                </div>
            </template>
        </Information>
        <div class="w-full flex justify-end mt-4">
            <button type="submit" class="px-4 py-1 bg-terciary text-white rounded">Editar</button>
        </div>
        <Register/>

        <div>
            <select name="grabar" id="grabar" class="px-3 py-1 border border-gray-300 rounded mt-5 mr-5 text-left w-1/2">
                <option value="grabar">--Seleccione--</option>
                <option value="grabar">Grabar</option>
            </select>
            <button class="px-4 py-1 bg-terciary text-white rounded">Grabar</button>
        </div>
        
        <BackNext/>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>