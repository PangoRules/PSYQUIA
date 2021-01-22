
function diagnosticosRealizados(){
    $('#pacientesRegistrados').hide();
    $('#diagnosticosDepresivoDistimico').hide();
    $('#diagnosticosRealizados').show();
    resetdiagnosticosRealizadosDT();
    location.href = "#diagnosticosDataTable";
}

function pacientesRegistrados(){
    $('#diagnosticosRealizados').hide();
    $('#diagnosticosDepresivoDistimico').hide();
    $('#pacientesRegistrados').show();
    resetPacientesDT();
    location.href = "#pacientesDataTable";
}

function diagnosticosDepresivoDistimico(){
    $('#diagnosticosRealizados').hide();
    $('#pacientesRegistrados').hide();
    $('#diagnosticosDepresivoDistimico').show();
    resetdiagnosticosDepresivoDistimicoDT();
    location.href = "#pacientesDataTable";
}

function ver_edit_paciente(id_paciente){
    fetch("/doc/get_datos_paciente",{
        method: "POST",
        body: id_paciente,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        }
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        $('#modalEditarPaciente #id_sex').val(data.data[0]['sex']);
        $('#modalEditarPaciente #id_birth_date').val(data.data[0]['birth_date']);
        $('#modalEditarPaciente #id_name').val(data.data[0]['name']);
        $('#modalEditarPaciente #id_email').val(data.data[0]['email']);
        $('#modalEditarPaciente #id_study').val(data.data[0]['study']);
        $('#modalEditarPaciente #id_job').val(data.data[0]['job']);
        $('#modalEditarPaciente #id_civil_state').val(data.data[0]['civil_state']);
        $('#modalEditarPaciente #id_religion').val(data.data[0]['religion']);
        $('#modalEditarPaciente #id_economical_situation').val(data.data[0]['economical_situation']);
        $('#modalEditarPaciente').modal('toggle');
    })
    .catch(err => {
        $('#modalError').modal('toggle');
    });
}

$('#EditPacienteForm').submit(function(e){
    e.preventDefault();
    var form = new FormData(document.getElementById('EditPacienteForm'));
    fetch("/doc/editar_paciente",{
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
        if(data.data){
            $('#modalEditarPaciente').modal('toggle');
            $('#modalExitoEditarPaciente').modal('toggle');
        }
    })
    .catch(err => {
        $('#modalError').modal('toggle');
    });
});

$('#acceptExitoEditarPaciente').click(function(e){
    window.location.reload();
});

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