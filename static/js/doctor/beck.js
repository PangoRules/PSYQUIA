import * as constants from '../base/constants.js';
import * as csrf from '../base/crfstoken.js';

/**
 * Funcion encargada de registrar el formulario submitido por el doctor
 */
$('#BeckForm').submit(function(e){
    e.preventDefault();
    var form = new FormData(document.getElementById('BeckForm'));
    console.log(constants.convertFormDatatoJson(form));
    fetch(constants.REGISTRO_BECK,{
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
            $('#modalExitoBeck').modal('toggle');
            $('.alert-danger').remove();
            //window.location.href=""
        }else if(data.errores){
            topFunction();
            $('.alert-danger').remove();
            for(var error in data.errores){
                console.log(data.errores[error]);
                switch(error){
                    case "id_paciente":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_paciente').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                }
            }
        }else{
            $('#modalError').modal('toggle');
        }
    })
    .catch(err => {
        $('#modalError').modal('toggle');
        console.log(err);
    });
});

function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  }