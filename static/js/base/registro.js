import * as constants from './constants.js';

$(function(){

});

/**
 * Funcion para obtener el token CSRF con javascript
 * @param {string} name - Parametro donde se le coloca el tipo de valor que se desea obtener, en este caso el token CSRF 
 * @returns {string} Token CSRF a insertar al metodo fetch
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Funcion encargada de prevenir que el formulario sea submitido
 * para poder crear un objeto con los datos de este y luego mandarlo
 * por post con fetch
 */
$('#RegistroForm').on('submit', function(e){
    e.preventDefault();
    var form = new FormData(document.getElementById('RegistroForm'));
    fetch(constants.REGISTRO_URL,{
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        }
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        if(data.respuesta==true){
            //console.log("Exito: "+data.respuesta);
            $('#modalExito').modal('toggle');
            $('#RegistroForm')[0].reset();
        }else{
            $('.alert-danger').remove();
            //console.log("Fracaso: "+data.respuesta);
            for(var error in data.errores){
                switch(error){
                    case "email":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_email').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                    case "nombres":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_nombres').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                    case "apellidos":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_apellidos').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                    case "cedula":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_cedula').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                    case "password1":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_password1').after('<div class="alert alert-danger mb-1 mt-3" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                    case "password2":
                        for(var temp=0;temp<data.errores[error].length;temp++){
                            $('#id_password2').after('<div class="alert alert-danger mb-1" role="alert"><small>'+data.errores[error][temp]+'</small></div>');
                        }
                    break;
                }
            }
        }
    })
    .catch(err => {
        console.log("Error en el servidor: "+err);
    });
});