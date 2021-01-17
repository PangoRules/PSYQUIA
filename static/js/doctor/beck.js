import * as constants from '../base/constants.js';
import * as csrf from '../base/crfstoken.js';

/**
 * Funcion encargada de registrar el formulario submitido por el doctor
 */
$('#BeckForm').submit(function(e){
    e.preventDefault();
    var form = new FormData(document.getElementById('BeckForm'));
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
            $("#modalExitoBeck .modal-body .res").empty();
            for(var res in data.resultados){
                if(data.resultados[res]){
                    switch(res){
                        case 'Suicidio':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>El paciente <strong>presenta</strong> riesgo de <strong>Pensamientos Suicidas</strong></p>');
                        break;
                        case 'Depresion':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>El paciente <strong>presenta</strong> riesgo de <strong>Trastorno Depresivo Mayor</strong></p>');
                        break;
                        case 'Distimia':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>El paciente <strong>presenta</strong> riesgo de <strong>Trastorno Distimico</strong></p>');
                        break;
                        case 'Melancolico':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>Trastorno Depresivo del Tipo: <strong>Melancólico</strong></p>');
                        break;
                        case 'Atipico':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>Trastorno Depresivo del Tipo: <strong>Atípico</strong></p>');
                        break;
                        case 'Catatonico':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>Trastorno Depresivo del Tipo: <strong>Catatónico</strong></p>');
                        break;
                    }
                }else{
                    switch(res){
                        case 'Suicidio':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>El paciente <strong>no presenta</strong> riesgo de <strong>Pensamientos Suicidas</strong></p>');
                        break;
                        case 'Depresion':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>El paciente <strong>no presenta</strong> riesgo de <strong>Trastorno Depresivo Mayor</strong></p>');
                        break;
                        case 'Distimia':
                            $("#modalExitoBeck").find(".modal-body .res").append('<p>El paciente <strong>no presenta</strong> riesgo de <strong>Trastorno Distimico</strong></p>');
                        break;
                    }
                }
                console.log(res)
                console.log(data.resultados[res])
            }
            $('#modalExitoBeck').modal('toggle');
            $('.alert-danger').remove();
            //$('#BeckForm')[0].reset();
            //window.location.href="/doc/dashboard";
        }else if(data.errores){
            topFunction();
            $('.alert-danger').remove();
            for(var error in data.errores){
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
    });
});

function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  }