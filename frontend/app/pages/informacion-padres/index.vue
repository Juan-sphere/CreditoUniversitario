<template>
    <div class="w-full">
        <Register :tabs="['Información del padre', 'Información de la madre']" :activeTab="activeTab"
            @tab-change="activeTab = $event">
            <template #register>
                <!-- DATOS DEL PADRE -->
                <div class="p-4 space-y-6" v-if="activeTab === 0">
                    <!-- Datos Generales -->
                    <div>
                        <h3 class="text-secondary font-bold mb-4">Datos Generales</h3>
                        <div class="grid grid-cols-4 gap-4">
                            <div>
                                <label class="font-semibold text-sm">Tipo de Documento <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosPadre.tipoDocumento"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="DNI">DNI</option>
                                    <option value="CE">CE</option>
                                    <option value="Otro">Otro</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Número de Documento <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.numeroDocumento"
                                    @input="validarNumeroDocumento('padre')" maxlength="8"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" placeholder="12345678"
                                    required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Apellido Paterno <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.apellidoPaterno"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Apellido Materno <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.apellidoMaterno"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Nombre <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.nombre"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Segundo Nombre <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.segundoNombre"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Fecha de Nacimiento <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.fechaNacimiento" placeholder="dd/mm/yyyy"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿El padre vive? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosPadre.vive"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Estado Civil <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosPadre.estadoCivil"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Soltero">Soltero</option>
                                    <option value="Casado">Casado</option>
                                    <option value="Viudo">Viudo</option>
                                    <option value="Divorciado">Divorciado</option>
                                </select>
                            </div>
                            <div class="col-span-2">
                                <label class="font-semibold text-sm">¿Es conviviente? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosPadre.conviviente"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si, con la madre">Sí, con la madre del postulante</option>
                                    <option value="Si, con otra">Sí, con otra persona que no es la madre</option>
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
                                <label class="font-semibold text-sm">Correo Personal <span
                                        class="text-red-500">(*)</span></label>
                                <input type="email" v-model="datosPadre.correoPersonal"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                                    placeholder="usuario@dominio.com" required />
                            </div>
                            <div class="col-span-2">
                                <label class="font-semibold text-sm">Correo de Trabajo <span
                                        class="text-red-500">(*)</span></label>
                                <input type="email" v-model="datosPadre.correoTrabajo"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                                    placeholder="usuario@dominio.com" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Teléfono Celular <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.celular"
                                    @input="validarTelefono('padre', 'celular')" maxlength="9"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" placeholder="9XXXXXXXX"
                                    required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Celular de Trabajo <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.celularTrabajo"
                                    @input="validarTelefono('padre', 'celularTrabajo')" maxlength="9"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" placeholder="9XXXXXXXX"
                                    required />
                            </div>
                        </div>
                    </div>

                    <!-- Datos Laborales -->
                    <div>
                        <h3 class="text-secondary font-bold mb-4">Datos Laborales</h3>
                        <div class="grid grid-cols-4 gap-4">
                            <div>
                                <label class="font-semibold text-sm">¿Vive con usted? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosPadre.viveConUsted"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Trabaja? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosPadre.trabaja"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Tipo de Trabajo <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosPadre.tipoTrabajo"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Independiente informal permanente">Independiente informal permanente
                                    </option>
                                    <option value="Independiente informal temporal">Independiente informal temporal
                                    </option>
                                    <option value="Dependiente formal permanente">Dependiente formal permanente</option>
                                    <option value="Dependiente formal temporal">Dependiente formal temporal</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Tiene Empresa/Negocio propio? </label>
                                <select v-model="datosPadre.tieneNegocio"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si, informal">Sí, Empresa/Negocio informal</option>
                                    <option value="Si, formal">Sí, Empresa/Negocio formal</option>
                                    <option value="No">No tiene</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Es responsable economía familiar? </label>
                                <select v-model="datosPadre.responsableEconomia"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Contribuye economía familiar? </label>
                                <select v-model="datosPadre.contribuyeEconomia"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div class="col-span-2">
                                <label class="font-semibold text-sm">Grado de Instrucción </label>
                                <select v-model="datosPadre.gradoInstruccion"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Sin instrucción">Sin instrucción</option>
                                    <option value="Primaria incompleta">Primaria incompleta</option>
                                    <option value="Primaria completa">Primaria completa</option>
                                    <option value="Secundaria incompleta">Secundaria incompleta</option>
                                    <option value="Secundaria completa">Secundaria completa</option>
                                    <option value="Técnica incompleta">Técnica incompleta</option>
                                    <option value="Técnica completa">Técnica completa</option>
                                    <option value="Superior incompleta">Superior incompleta</option>
                                    <option value="Superior completa">Superior completa</option>
                                    <option value="Postgrado maestría incompleta">Postgrado maestría incompleta</option>
                                    <option value="Postgrado maestría completa">Postgrado maestría completa</option>
                                    <option value="Postgrado doctorado incompleto">Postgrado doctorado incompleto
                                    </option>
                                    <option value="Postgrado doctorado completo">Postgrado doctorado completo</option>
                                </select>
                            </div>
                            <div class="col-span-2">
                                <label class="font-semibold text-sm">Profesión u Oficio <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosPadre.profesion"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Tiene problemas de salud? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosPadre.problemaSalud"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="w-full flex justify-between items-center mt-5">
                        <div>
                            <p class="text-white bg-red-500 px-2">Campos Obligatorios (*)</p>
                        </div>
                        <button type="submit" class="px-4 py-1 bg-terciary text-white">
                            Registrar
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
                                <label class="font-semibold text-sm">Tipo de Documento <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.tipoDocumento"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="DNI">DNI</option>
                                    <option value="CE">CE</option>
                                    <option value="Otro">Otro</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Número de Documento <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.numeroDocumento"
                                    @input="validarNumeroDocumento('madre')" maxlength="8"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" placeholder="12345678"
                                    required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Apellido Paterno <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.apellidoPaterno"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Apellido Materno <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.apellidoMaterno"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Nombre <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.nombre"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Segundo Nombre <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.segundoNombre"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Fecha de Nacimiento <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.fechaNacimiento" placeholder="dd/mm/yyyy"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿La madre vive? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.vive"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Estado Civil <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.estadoCivil"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Soltera">Soltera</option>
                                    <option value="Casada">Casada</option>
                                    <option value="Viuda">Viuda</option>
                                    <option value="Divorciada">Divorciada</option>
                                </select>
                            </div>
                            <div class="col-span-2">
                                <label class="font-semibold text-sm">¿Es conviviente? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.conviviente"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si, con el padre">Sí, con el padre del postulante</option>
                                    <option value="Si, con otra">Sí, con otra persona que no es el padre</option>
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
                                <label class="font-semibold text-sm">Correo Personal <span
                                        class="text-red-500">(*)</span></label>
                                <input type="email" v-model="datosMadre.correoPersonal"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                                    placeholder="usuario@dominio.com" required />
                            </div>
                            <div class="col-span-2">
                                <label class="font-semibold text-sm">Correo de Trabajo <span
                                        class="text-red-500">(*)</span></label>
                                <input type="email" v-model="datosMadre.correoTrabajo"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1"
                                    placeholder="usuario@dominio.com" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Teléfono Celular <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.celular"
                                    @input="validarTelefono('madre', 'celular')" maxlength="9"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" placeholder="9XXXXXXXX"
                                    required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Celular de Trabajo <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.celularTrabajo"
                                    @input="validarTelefono('madre', 'celularTrabajo')" maxlength="9"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" placeholder="9XXXXXXXX"
                                    required />
                            </div>
                        </div>
                    </div>

                    <!-- Datos Laborales -->
                    <div>
                        <h3 class="text-secondary font-bold mb-4">Datos Laborales</h3>
                        <div class="grid grid-cols-4 gap-4">
                            <div>
                                <label class="font-semibold text-sm">¿Vive con usted? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.viveConUsted"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Trabaja? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.trabaja"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">Tipo de Trabajo <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.tipoTrabajo"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Independiente informal permanente">Independiente informal permanente
                                    </option>
                                    <option value="Independiente informal temporal">Independiente informal temporal
                                    </option>
                                    <option value="Dependiente formal permanente">Dependiente formal permanente</option>
                                    <option value="Dependiente formal temporal">Dependiente formal temporal</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Tiene Empresa/Negocio propio?</label>
                                <select v-model="datosMadre.tieneNegocio"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si, informal">Sí, Empresa/Negocio informal</option>
                                    <option value="Si, formal">Sí, Empresa/Negocio formal</option>
                                    <option value="No">No tiene</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Es responsable economía familiar? </label>
                                <select v-model="datosMadre.responsableEconomia"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Contribuye economía familiar? </label>
                                <select v-model="datosMadre.contribuyeEconomia"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                            <div class="col-span-2">
                                <label class="font-semibold text-sm">Grado de Instrucción <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.gradoInstruccion"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Sin instrucción">Sin instrucción</option>
                                    <option value="Primaria incompleta">Primaria incompleta</option>
                                    <option value="Primaria completa">Primaria completa</option>
                                    <option value="Secundaria incompleta">Secundaria incompleta</option>
                                    <option value="Secundaria completa">Secundaria completa</option>
                                    <option value="Técnica incompleta">Técnica incompleta</option>
                                    <option value="Técnica completa">Técnica completa</option>
                                    <option value="Superior incompleta">Superior incompleta</option>
                                    <option value="Superior completa">Superior completa</option>
                                    <option value="Postgrado maestría incompleta">Postgrado maestría incompleta</option>
                                    <option value="Postgrado maestría completa">Postgrado maestría completa</option>
                                    <option value="Postgrado doctorado incompleto">Postgrado doctorado incompleto
                                    </option>
                                    <option value="Postgrado doctorado completo">Postgrado doctorado completo</option>
                                </select>
                            </div>
                            <div class="col-span-2">
                                <label class="font-semibold text-sm">Profesión u Oficio <span
                                        class="text-red-500">(*)</span></label>
                                <input type="text" v-model="datosMadre.profesion"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required />
                            </div>
                            <div>
                                <label class="font-semibold text-sm">¿Tiene problemas de salud? <span
                                        class="text-red-500">(*)</span></label>
                                <select v-model="datosMadre.problemaSalud"
                                    class="w-full px-3 py-1 border border-gray-300 rounded mt-1" required>
                                    <option value="">--Seleccione--</option>
                                    <option value="Si">Sí</option>
                                    <option value="No">No</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="w-full flex justify-between items-center mt-5">
                        <div>
                            <p class="text-white bg-red-500 px-2">Campos Obligatorios (*)</p>
                        </div>
                        <button type="submit" class="px-4 py-1 bg-terciary text-white">
                            Registrar
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
import { ref } from "vue";

const activeTab = ref(0);

const datosPadre = ref({
    tipoDocumento: "",
    numeroDocumento: "",
    apellidoPaterno: "",
    apellidoMaterno: "",
    nombre: "",
    segundoNombre: "",
    fechaNacimiento: "",
    vive: "",
    estadoCivil: "",
    conviviente: "",
    correoPersonal: "",
    correoTrabajo: "",
    celular: "",
    celularTrabajo: "",
    viveConUsted: "",
    trabaja: "",
    tipoTrabajo: "",
    tieneNegocio: "",
    responsableEconomia: "",
    contribuyeEconomia: "",
    gradoInstruccion: "",
    profesion: "",
    problemaSalud: ""
});

const datosMadre = ref({
    tipoDocumento: "",
    numeroDocumento: "",
    apellidoPaterno: "",
    apellidoMaterno: "",
    nombre: "",
    segundoNombre: "",
    fechaNacimiento: "",
    vive: "",
    estadoCivil: "",
    conviviente: "",
    correoPersonal: "",
    correoTrabajo: "",
    celular: "",
    celularTrabajo: "",
    viveConUsted: "",
    trabaja: "",
    tipoTrabajo: "",
    tieneNegocio: "",
    responsableEconomia: "",
    contribuyeEconomia: "",
    gradoInstruccion: "",
    profesion: "",
    problemaSalud: ""
});

const validarNumeroDocumento = (tipo: string) => {
    const datos = tipo === "padre" ? datosPadre.value : datosMadre.value;
    if (datos.numeroDocumento.length > 8) {
        datos.numeroDocumento = datos.numeroDocumento.slice(0, 8);
    }
};

const validarTelefono = (tipo: string, campo: string) => {
    const datos = tipo === "padre" ? datosPadre.value : datosMadre.value;
    const valor = datos[campo as keyof typeof datos];

    if (typeof valor === "string") {
        let soloNumeros = valor.replace(/\D/g, "");
        if (soloNumeros.length > 9) {
            soloNumeros = soloNumeros.slice(0, 9);
        }

        if (soloNumeros && !soloNumeros.startsWith("9")) {
            soloNumeros = "";
        }

        datos[campo as keyof typeof datos] = soloNumeros;
    }
};
</script>
