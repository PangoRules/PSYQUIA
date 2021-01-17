/**
 * Url para registrarse
 * @type {string}  
 */
export const REGISTRO_URL = "/registrarse/";
export const REGISTRO_PACIENTE_URL = "/doc/registrarpaciente";
export const REGISTRO_BECK = "/doc/becktest";



/**
 * Funcion encargada de convertir un objeto FormData a JSon
 * @param {FormData} formdata - Objeto tipo form data 
 */
export function convertFormDatatoJson(formdata){
    if(formdata){
        var object = {};
        formdata.forEach((value, key) => object[key] = value);
        var json = JSON.stringify(object);
        return json;
    }else{
        return 'Formulario Vacio';
    }
    
}