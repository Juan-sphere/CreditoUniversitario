<template>
  <div class="w-full">
    <!-- Loading Spinner -->
    <div v-if="loading" class="flex justify-center items-center h-96">
      <LoadingSpinner />
    </div>

    <!-- Form Content -->
    <div v-else>
      <Register
        :tabs="['Información del padre', 'Información de la madre']"
        :activeTab="activeTab"
        @tab-change="activeTab = $event"
      >
        <template #register>
          <!-- DATOS DEL PADRE -->
          <div class="p-4 space-y-6" v-if="activeTab === 0">
            <!-- Datos Generales -->
            <div>
              <h3 class="text-secondary font-bold mb-4">Datos Generales</h3>
              <div class="grid grid-cols-4 gap-4">
                <div>
                  <label class="font-semibold text-sm"
                    >Tipo de Documento
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosPadre.tipo_documento"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="DNI">DNI</option>
                    <option value="CE">CE</option>
                    <option value="PASAPORTE">Pasaporte</option>
                  </select>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Número de Documento
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosPadre.numero_documento"
                    @input="validarNumeroDocumento('padre')"
                    maxlength="8"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="12345678"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Apellidos <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosPadre.apellidos"
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
                    v-model="datosPadre.nombre"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Fecha de Nacimiento
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="date"
                    v-model="datosPadre.fecha_nacimiento"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >¿El padre vive?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosPadre.vive"
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
                    >Estado Civil <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosPadre.estado_civil"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Soltero">Soltero</option>
                    <option value="Casado">Casado</option>
                    <option value="Viudo">Viudo</option>
                    <option value="Divorciado">Divorciado</option>
                  </select>
                </div>
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >¿Es conviviente?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosPadre.es_conviviente"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si, con la madre">
                      Sí, con la madre del postulante
                    </option>
                    <option value="Si, con otra">
                      Sí, con otra persona que no es la madre
                    </option>
                    <option value="No">No</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- Datos de Contacto -->
            <div>
              <h3 class="text-secondary font-bold mb-4">Datos de Contacto</h3>
              <div class="grid grid-cols-4 gap-4">
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >Correo Personal
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="email"
                    v-model="datosPadre.correo_personal"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="usuario@dominio.com"
                    required
                  />
                </div>
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >Correo de Trabajo
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="email"
                    v-model="datosPadre.correo_trabajo"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="usuario@dominio.com"
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Teléfono Celular
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosPadre.celular"
                    @input="validarTelefono('padre', 'celular')"
                    maxlength="9"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="9XXXXXXXX"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Celular de Trabajo
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosPadre.celular_trabajo"
                    @input="validarTelefono('padre', 'celular_trabajo')"
                    maxlength="9"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="9XXXXXXXX"
                  />
                </div>
              </div>
            </div>

            <!-- Datos Laborales -->
            <div>
              <h3 class="text-secondary font-bold mb-4">Datos Laborales</h3>
              <div class="grid grid-cols-3 gap-4">
                <div>
                  <label class="font-semibold text-sm"
                    >¿Vive con usted?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosPadre.vive_con_usuario"
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
                    >¿Trabaja? <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosPadre.trabaja"
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
                    >Tipo de Trabajo
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosPadre.tipo_trabajo"
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
                <div>
                  <label class="font-semibold text-sm"
                    >¿Tiene Empresa/Negocio propio?</label
                  >
                  <select
                    v-model="datosPadre.tiene_negocio"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si, informal">
                      Sí, Empresa/Negocio informal
                    </option>
                    <option value="Si, formal">
                      Sí, Empresa/Negocio formal
                    </option>
                    <option value="No">No tiene</option>
                  </select>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >¿Es responsable economía familiar?</label
                  >
                  <select
                    v-model="datosPadre.responsable_economia"
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
                    >¿Contribuye economía familiar?</label
                  >
                  <select
                    v-model="datosPadre.contribuye_economia"
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
                    >Grado de Instrucción</label
                  >
                  <select
                    v-model="datosPadre.grado_instruccion"
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
                    <option value="Técnica incompleta">
                      Técnica incompleta
                    </option>
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
                <div>
                  <label class="font-semibold text-sm"
                    >¿Tiene problemas de salud?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosPadre.problemas_salud"
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
                    >Profesión u Oficio
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosPadre.profesion"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
              </div>
            </div>

            <div class="w-full flex justify-between items-center mt-5">
              <div>
                <p class="text-white bg-red-500 px-2">
                  Campos Obligatorios (*)
                </p>
              </div>
              <button
                @click="guardarTodo"
                :disabled="guardando"
                class="px-4 py-1 bg-terciary text-white disabled:opacity-50"
              >
                {{
                  guardando
                    ? "Guardando..."
                    : existePadreGuardado
                      ? "Actualizar"
                      : "Guardar"
                }}
              </button>
            </div>
          </div>

          <!-- DATOS DE LA MADRE -->
          <div class="p-4 space-y-6" v-if="activeTab === 1">
            <!-- Datos Generales -->
            <div>
              <h3 class="text-secondary font-bold mb-4">Datos Generales</h3>
              <div class="grid grid-cols-4 gap-4">
                <div>
                  <label class="font-semibold text-sm"
                    >Tipo de Documento
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosMadre.tipo_documento"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="DNI">DNI</option>
                    <option value="CE">CE</option>
                    <option value="PASAPORTE">Pasaporte</option>
                  </select>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Número de Documento
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosMadre.numero_documento"
                    @input="validarNumeroDocumento('madre')"
                    maxlength="8"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="12345678"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Apellidos <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosMadre.apellidos"
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
                    v-model="datosMadre.nombre"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Fecha de Nacimiento
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="date"
                    v-model="datosMadre.fecha_nacimiento"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >¿La madre vive?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosMadre.vive"
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
                    >Estado Civil <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosMadre.estado_civil"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Soltera">Soltera</option>
                    <option value="Casada">Casada</option>
                    <option value="Viuda">Viuda</option>
                    <option value="Divorciada">Divorciada</option>
                  </select>
                </div>
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >¿Es conviviente?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosMadre.es_conviviente"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si, con el padre">
                      Sí, con el padre del postulante
                    </option>
                    <option value="Si, con otra">
                      Sí, con otra persona que no es el padre
                    </option>
                    <option value="No">No</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- Datos de Contacto (Madre) -->
            <div>
              <h3 class="text-secondary font-bold mb-4">Datos de Contacto</h3>
              <div class="grid grid-cols-4 gap-4">
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >Correo Personal
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="email"
                    v-model="datosMadre.correo_personal"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="usuario@dominio.com"
                    required
                  />
                </div>
                <div class="col-span-2">
                  <label class="font-semibold text-sm"
                    >Correo de Trabajo
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="email"
                    v-model="datosMadre.correo_trabajo"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="usuario@dominio.com"
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Teléfono Celular
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosMadre.celular"
                    @input="validarTelefono('madre', 'celular')"
                    maxlength="9"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="9XXXXXXXX"
                    required
                  />
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >Celular de Trabajo
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosMadre.celular_trabajo"
                    @input="validarTelefono('madre', 'celular_trabajo')"
                    maxlength="9"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    placeholder="9XXXXXXXX"
                  />
                </div>
              </div>
            </div>

            <!-- Datos Laborales (Madre) -->
            <div>
              <h3 class="text-secondary font-bold mb-4">Datos Laborales</h3>
              <div class="grid grid-cols-3 gap-4">
                <div>
                  <label class="font-semibold text-sm"
                    >¿Vive con usted?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosMadre.vive_con_usuario"
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
                    >¿Trabaja? <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosMadre.trabaja"
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
                    >Tipo de Trabajo
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosMadre.tipo_trabajo"
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
                <div>
                  <label class="font-semibold text-sm"
                    >¿Tiene Empresa/Negocio propio?</label
                  >
                  <select
                    v-model="datosMadre.tiene_negocio"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  >
                    <option value="">--Seleccione--</option>
                    <option value="Si, informal">
                      Sí, Empresa/Negocio informal
                    </option>
                    <option value="Si, formal">
                      Sí, Empresa/Negocio formal
                    </option>
                    <option value="No">No tiene</option>
                  </select>
                </div>
                <div>
                  <label class="font-semibold text-sm"
                    >¿Es responsable economía familiar?</label
                  >
                  <select
                    v-model="datosMadre.responsable_economia"
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
                    >¿Contribuye economía familiar?</label
                  >
                  <select
                    v-model="datosMadre.contribuye_economia"
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
                    >Grado de Instrucción</label
                  >
                  <select
                    v-model="datosMadre.grado_instruccion"
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
                    <option value="Técnica incompleta">
                      Técnica incompleta
                    </option>
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
                <div>
                  <label class="font-semibold text-sm"
                    >¿Tiene problemas de salud?
                    <span class="text-red-500">(*)</span></label
                  >
                  <select
                    v-model="datosMadre.problemas_salud"
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
                    >Profesión u Oficio
                    <span class="text-red-500">(*)</span></label
                  >
                  <input
                    type="text"
                    v-model="datosMadre.profesion"
                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                    required
                  />
                </div>
              </div>
            </div>

            <div class="w-full flex justify-between items-center mt-5">
              <div>
                <p class="text-white bg-red-500 px-2">
                  Campos Obligatorios (*)
                </p>
              </div>
              <button
                @click="guardarTodo"
                :disabled="guardando"
                class="px-4 py-1 bg-terciary text-white disabled:opacity-50"
              >
                {{
                  guardando
                    ? "Guardando..."
                    : existeMadreGuardada
                      ? "Actualizar"
                      : "Guardar"
                }}
              </button>
            </div>
          </div>
        </template>
      </Register>

      <div class="flex justify-center items-center">
        <BackNext />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { toast } from "vue3-toastify";
import { useRouter } from "vue-router";
import LoadingSpinner from "~/components/LoadingSpinner.vue";
import Register from "~/components/Register.vue";
import BackNext from "~/components/BackNext.vue";
import { useAuth } from "~/composables/useAuth";

const router = useRouter();
const config = useRuntimeConfig();
const apiBase = config.public.apiBase as string;
const { token } = useAuth();

const activeTab = ref(0);
const loading = ref(true);
const guardando = ref(false);
const existePadreGuardado = ref(false);
const existeMadreGuardada = ref(false);

type ParentData = {
  tipo_documento?: string;
  numero_documento?: string;
  apellidos?: string;
  nombre?: string;
  fecha_nacimiento?: string;
  vive?: string;
  estado_civil?: string;
  es_conviviente?: string;
  correo_personal?: string;
  correo_trabajo?: string;
  celular?: string;
  celular_trabajo?: string;
  vive_con_usuario?: string;
  trabaja?: string;
  tipo_trabajo?: string;
  tiene_negocio?: string;
  responsable_economia?: string;
  contribuye_economia?: string;
  grado_instruccion?: string;
  profesion?: string;
  problemas_salud?: string;
};

const datosPadre = ref<ParentData>({
  tipo_documento: "",
  numero_documento: "",
  apellidos: "",
  nombre: "",
  fecha_nacimiento: "",
  vive: "",
  estado_civil: "",
  es_conviviente: "",
  correo_personal: "",
  correo_trabajo: "",
  celular: "",
  celular_trabajo: "",
  vive_con_usuario: "",
  trabaja: "",
  tipo_trabajo: "",
  tiene_negocio: "",
  responsable_economia: "",
  contribuye_economia: "",
  grado_instruccion: "",
  profesion: "",
  problemas_salud: "",
});

const datosMadre = ref<ParentData>({
  tipo_documento: "",
  numero_documento: "",
  apellidos: "",
  nombre: "",
  fecha_nacimiento: "",
  vive: "",
  estado_civil: "",
  es_conviviente: "",
  correo_personal: "",
  correo_trabajo: "",
  celular: "",
  celular_trabajo: "",
  vive_con_usuario: "",
  trabaja: "",
  tipo_trabajo: "",
  tiene_negocio: "",
  responsable_economia: "",
  contribuye_economia: "",
  grado_instruccion: "",
  profesion: "",
  problemas_salud: "",
});

// Cargar datos existentes
const cargarDatos = async () => {
  try {
    loading.value = true;
    const response = await $fetch<any>(`${apiBase}/auth/informacion-padres`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token.value}`,
      },
    });

    if (response?.data?.padre) {
      datosPadre.value = transformarDatosDelBackend(response.data.padre);
      existePadreGuardado.value = true;
    }
    if (response?.data?.madre) {
      datosMadre.value = transformarDatosDelBackend(response.data.madre);
      existeMadreGuardada.value = true;
    }
  } catch (error: any) {
    console.log("No hay datos previos o error al cargar:", error.message);
  } finally {
    loading.value = false;
  }
};

// Transformar datos del backend al formato del frontend
const transformarDatosDelBackend = (datosBackend: any): ParentData => {
  return {
    tipo_documento: datosBackend.tipo_documento || "",
    numero_documento: datosBackend.numero_documento || "",
    apellidos: `${datosBackend.apellido_paterno || ""} ${datosBackend.apellido_materno || ""}`.trim(),
    nombre: datosBackend.nombre || "",
    fecha_nacimiento: datosBackend.fecha_nacimiento || "",
    vive: datosBackend.vive ? "Si" : "No",
    estado_civil: datosBackend.estado_civil || "",
    es_conviviente: datosBackend.es_conviviente ? "Si, con la madre" : "No",
    correo_personal: datosBackend.correo_personal || "",
    correo_trabajo: datosBackend.correo_trabajo || "",
    celular: datosBackend.telefono_celular || "",
    celular_trabajo: datosBackend.celular_trabajo || "",
    vive_con_usuario: datosBackend.vive_con_usuario ? "Si" : "No",
    trabaja: datosBackend.trabaja ? "Si" : "No",
    tipo_trabajo: datosBackend.tipo_trabajo || "",
    tiene_negocio: datosBackend.tiene_empresa ? "Si, informal" : "No",
    responsable_economia: datosBackend.responsable_economia ? "Si" : "No",
    contribuye_economia: datosBackend.contribuye_economia ? "Si" : "No",
    grado_instruccion: datosBackend.grado_instruccion || "",
    profesion: datosBackend.profesion_oficio || "",
    problemas_salud: datosBackend.problemas_salud ? "Si" : "No",
  };
};

// Validar campos requeridos
const validarDatos = (datos: ParentData, tipo: string): boolean => {
  const camposRequeridos = [
    "tipo_documento",
    "numero_documento",
    "apellidos",
    "nombre",
    "fecha_nacimiento",
    "vive",
    "estado_civil",
    "es_conviviente",
    "correo_personal",
    "vive_con_usuario",
    "trabaja",
    "tipo_trabajo",
    "profesion",
    "problemas_salud",
  ];

  for (const campo of camposRequeridos) {
    const valor = datos[campo as keyof ParentData];
    if (!valor || valor === "") {
      toast.error(`${tipo}: Por favor completa el campo "${campo}"`);
      return false;
    }
  }
  return true;
};

// Transformar datos del frontend al formato del backend
const transformarDatos = (datos: ParentData, parentType: string) => {
  // Separar apellidos si vienen como un solo campo
  const apellidosParts = (datos.apellidos || "").split(" ");
  const apellido_paterno = apellidosParts[0] || "";
  const apellido_materno = apellidosParts.slice(1).join(" ") || "";

  return {
    parent_type: parentType,

    // Datos generales
    tipo_documento: datos.tipo_documento || "",
    numero_documento: datos.numero_documento || "",
    apellido_paterno,
    apellido_materno,
    nombre: datos.nombre || "",
    segundo_nombre: datos.nombre || "",
    fecha_nacimiento: datos.fecha_nacimiento || "1900-01-01",
    vive: datos.vive === "Si",
    estado_civil: datos.estado_civil || "",
    es_conviviente:
      datos.es_conviviente && datos.es_conviviente.startsWith("Si"),

    // Datos de contacto
    correo_personal: datos.correo_personal || "",
    correo_trabajo: datos.correo_trabajo || "",
    telefono_celular: datos.celular || "",
    celular_trabajo: datos.celular_trabajo || "",

    // Datos laborales
    vive_con_usuario: datos.vive_con_usuario === "Si",
    trabaja: datos.trabaja === "Si",
    tipo_trabajo: datos.tipo_trabajo || "",
    tiene_empresa: datos.tiene_negocio && datos.tiene_negocio.includes("Si"),
    responsable_economia: datos.responsable_economia === "Si",
    contribuye_economia: datos.contribuye_economia === "Si",
    grado_instruccion: datos.grado_instruccion || "",
    profesion_oficio: datos.profesion || "",
    problemas_salud: datos.problemas_salud === "Si",
  };
};

// Guardar todos los datos
const guardarTodo = async () => {
  try {
    guardando.value = true;

    // Validar que al menos tenga datos de padre o madre
    const tieneDataPadre =
      datosPadre.value.numero_documento || datosPadre.value.nombre;
    const tieneDataMadre =
      datosMadre.value.numero_documento || datosMadre.value.nombre;

    if (!tieneDataPadre && !tieneDataMadre) {
      toast.error("Por favor ingresa datos de al menos uno de los padres");
      guardando.value = false;
      return;
    }

    // Guardar padre
    if (tieneDataPadre) {
      // Validar padre si tiene datos
      if (!validarDatos(datosPadre.value, "Padre")) {
        guardando.value = false;
        return;
      }

      const metodo = existePadreGuardado.value ? "PUT" : "POST";
      await $fetch(`${apiBase}/auth/informacion-padres`, {
        method: metodo,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
        body: transformarDatos(datosPadre.value, "PADRE"),
      });

      existePadreGuardado.value = true;
      toast.success("✓ Información del padre guardada");

      // Cambiar a pestaña de madre
      if (tieneDataMadre) {
        activeTab.value = 1;
      }
    }

    // Guardar madre
    if (tieneDataMadre) {
      // Validar madre si tiene datos
      if (!validarDatos(datosMadre.value, "Madre")) {
        guardando.value = false;
        return;
      }

      const metodo = existeMadreGuardada.value ? "PUT" : "POST";
      await $fetch(`${apiBase}/auth/informacion-padres`, {
        method: metodo,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
        body: transformarDatos(datosMadre.value, "MADRE"),
      });

      existeMadreGuardada.value = true;
      toast.success("✓ Información de la madre guardada");
    }

    // Toast final y recargar datos
    toast.success("✓ Información de padres guardada correctamente");
    await cargarDatos();
  } catch (error: any) {
    console.error("Error al guardar:", error);
    toast.error(
      error.data?.detail || "Error al guardar la información de padres",
    );
  } finally {
    guardando.value = false;
  }
};

const validarNumeroDocumento = (tipo: string) => {
  const datos = tipo === "padre" ? datosPadre.value : datosMadre.value;
  if (datos.numero_documento && datos.numero_documento.length > 8) {
    datos.numero_documento = datos.numero_documento.slice(0, 8);
  }
};

const validarTelefono = (
  tipo: string,
  campo: "celular" | "celular_trabajo",
) => {
  const datos = tipo === "padre" ? datosPadre.value : datosMadre.value;
  const valor = datos[campo];

  if (typeof valor === "string") {
    let soloNumeros = valor.replace(/\D/g, "");
    if (soloNumeros.length > 9) {
      soloNumeros = soloNumeros.slice(0, 9);
    }

    if (soloNumeros && !soloNumeros.startsWith("9")) {
      soloNumeros = "";
    }

    datos[campo] = soloNumeros;
  }
};

onMounted(() => {
  cargarDatos();
});
</script>
