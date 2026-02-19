<template>
  <div class="w-full space-y-4">
    <!-- Encabezado -->
    <Information title="Instrucciones generales">
      <template #information>
        <div class="p-4 text-gray-700 text-sm space-y-3">
          <p>
            Bienvenido al sistema de solicitud de <strong>Crédito Universitario</strong>. Para completar tu solicitud
            deberás llenar cada sección del menú lateral en orden. Lee atentamente las indicaciones antes de empezar.
          </p>
          <ul class="list-disc list-inside space-y-1 pl-2">
            <li>Todos los campos marcados con <span class="text-red-500 font-bold">(*)</span> son <strong>obligatorios</strong>.</li>
            <li>Haz clic en <strong>Registrar</strong> al finalizar cada sección para guardar los datos ingresados.</li>
            <li>Usa los botones <strong>Anterior</strong> y <strong>Siguiente</strong> para navegar entre secciones.</li>
            <li>Al terminar todas las secciones, dirígete a <strong>Enviar Solicitud</strong> para finalizar el proceso.</li>
          </ul>
          <p class="text-yellow-600 font-medium">
            Asegúrate de tener a la mano los documentos de sustentación antes de comenzar.
          </p>
        </div>
      </template>
    </Information>

    <!-- Pasos -->
    <Information title="Pasos a seguir">
      <template #information>
        <div class="p-4 text-sm text-gray-700 space-y-3">
          <ol class="space-y-4">
            <li class="flex gap-3">
              <span class="bg-secondary text-white font-bold rounded-full w-6 h-6 flex items-center justify-center shrink-0">1</span>
              <div>
                <p class="font-semibold">Información Personal</p>
                <p class="text-gray-500">Completa tus datos personales, correo electrónico, dirección y datos laborales. Registra cada pestaña por separado.</p>
              </div>
            </li>
            <li class="flex gap-3">
              <span class="bg-secondary text-white font-bold rounded-full w-6 h-6 flex items-center justify-center shrink-0">2</span>
              <div>
                <p class="font-semibold">Información de los Padres</p>
                <p class="text-gray-500">Ingresa los datos del padre y la madre: nombres, DNI, situación laboral e ingresos mensuales.</p>
              </div>
            </li>
            <li class="flex gap-3">
              <span class="bg-secondary text-white font-bold rounded-full w-6 h-6 flex items-center justify-center shrink-0">3</span>
              <div>
                <p class="font-semibold">Composición del núcleo familiar</p>
                <p class="text-gray-500">Registra a todas las personas que viven contigo: parentesco, edad, ocupación e ingresos.</p>
              </div>
            </li>
            <li class="flex gap-3">
              <span class="bg-secondary text-white font-bold rounded-full w-6 h-6 flex items-center justify-center shrink-0">4</span>
              <div>
                <p class="font-semibold">Personas que contribuyen externamente</p>
                <p class="text-gray-500">Indica si hay personas fuera del núcleo familiar que aporten económicamente a tu hogar.</p>
              </div>
            </li>
            <li class="flex gap-3">
              <span class="bg-secondary text-white font-bold rounded-full w-6 h-6 flex items-center justify-center shrink-0">5</span>
              <div>
                <p class="font-semibold">Información económica del núcleo familiar</p>
                <p class="text-gray-500">Registra los ingresos y egresos mensuales familiares. Verifica el balance presupuestal y agrega una observación si es necesario.</p>
              </div>
            </li>
            <li class="flex gap-3">
              <span class="bg-secondary text-white font-bold rounded-full w-6 h-6 flex items-center justify-center shrink-0">6</span>
              <div>
                <p class="font-semibold">Patrimonio del núcleo familiar</p>
                <p class="text-gray-500">Declara los bienes del grupo familiar: inmuebles, vehículos u otros activos relevantes.</p>
              </div>
            </li>
            <li class="flex gap-3">
              <span class="bg-secondary text-white font-bold rounded-full w-6 h-6 flex items-center justify-center shrink-0">7</span>
              <div>
                <p class="font-semibold">Documentos de sustentación</p>
                <p class="text-gray-500">Adjunta los documentos requeridos en formato PDF o imagen. Verifica que sean legibles antes de subirlos.</p>
              </div>
            </li>
            <li class="flex gap-3">
              <span class="bg-secondary text-white font-bold rounded-full w-6 h-6 flex items-center justify-center shrink-0">8</span>
              <div>
                <p class="font-semibold">Enviar Solicitud</p>
                <p class="text-gray-500">Revisa el resumen de tu solicitud y envíala. Recibirás una confirmación una vez procesada.</p>
              </div>
            </li>
          </ol>
        </div>
      </template>
    </Information>
  </div>
</template>
