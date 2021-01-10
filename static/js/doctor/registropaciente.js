import * as constants from '../base/constants.js';
import * as csrf from '../base/crfstoken.js';

/**
 * Funcion encargada de registrar al paciente
 * FALTA AGREGAR EL ID DEL DOCTOR QUE LO REGISTRO!!!!!, MODELO Y FORMULARIO
 */
$('#RegistroPacienteForm').submit(function(e){
    e.preventDefault();
    var form = new FormData(document.getElementById('RegistroPacienteForm'));
    fetch(constants.REGISTRO_PACIENTE_URL,{
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": csrf.getCookie('csrftoken'),
        }
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        console.log(data)
    })
    .catch(err => {
        console.log("Error en el servidor: "+err)
    });
});