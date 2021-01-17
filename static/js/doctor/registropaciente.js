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
        if(data.respuesta==true){
            $('.alert-danger').remove();
            $('#modalExitoPaciente').modal('toggle');
            $('#RegistroPacienteForm')[0].reset();
        }else if(data.errores){
            $('.alert-danger').remove();
            for(var error in data.errores){
                switch(error){
                    case "email":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_email').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                    case "birth_date":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_birth_date').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                    case "name":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_name').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                }
            }
        }
    })
    .catch(err => {
        console.log("Error en el servidor: "+err)
    });
});