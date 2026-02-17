<template>
    <div class="w-full">
        <Information title="Dirección del alumno">
            <template #information>
                <div class="bg-[#FFF9E9] p-4">
                    <p class="text-yellow-500">
                        Aviso! No Existen registros para la consulta...
                    </p>
                </div>
            </template>
        </Information>
        <div class="w-full flex justify-start mt-5">
            <button type="button" class="px-4 py-1 bg-gray-200 text-gray-500">Nueva Dirección</button>
        </div>
        <BackNext />
    </div>
</template>
