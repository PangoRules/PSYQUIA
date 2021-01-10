import * as constants from '../base/constants.js';
import * as csrf from '../base/crfstoken.js';

/**
 * Funcion encargada de registrar el formulario submitido por el doctor
 */
$('#RegistroPacienteForm').submit(function(e){
    e.preventDefault();
});