/**
 * Funcion para obtener el token CSRF con javascript
 * @param {string} name - Parametro donde se le coloca el tipo de valor que se desea obtener, en este caso el token CSRF 
 * @returns {string} Token CSRF a insertar al metodo fetch
 */

export function getCookie(name) {
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