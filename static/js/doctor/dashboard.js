
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

function ver_testbeck(id_paciente){
    fetch("/doc/get_test_beck",{
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
        console.log(data.data);
        for(var res in data.data){
            console.log(data.data[res]);
            $('#id_paciente').val(data.data[res].paciente_id);
            $('#id_tristeza').val(data.data[res].tristeza);
            $('#id_pesimismo').val(data.data[res].pesimismo);
            $('#id_fracaso').val(data.data[res].fracaso);
            $('#id_placer').val(data.data[res].placer);
            $('#id_culpa').val(data.data[res].culpa);
            $('#id_castigo').val(data.data[res].castigo);
            $('#id_disconformidad').val(data.data[res].disconformidad);
            $('#id_autocritica').val(data.data[res].autocritica);
            $('#id_llanto').val(data.data[res].llanto);
            $('#id_agitacion').val(data.data[res].agitacion);
            $('#id_interes').val(data.data[res].interes);
            $('#id_indecision').val(data.data[res].indecision);
            $('#id_desvalorizacion').val(data.data[res].desvalorizacion);
            $('#id_energia').val(data.data[res].energia);
            $('#id_sueño').val(data.data[res].sueño);
            $('#id_irritabilidad').val(data.data[res].irritabilidad);
            $('#id_apetito').val(data.data[res].apetito);
            $('#id_concentracion').val(data.data[res].concentracion);
            $('#id_fatiga').val(data.data[res].fatiga);
            $('#id_sexo').val(data.data[res].sexo);
            $('#id_vivir_solo').prop('checked',data.data[res].vivir_solo);
            $('#id_conflicto_familiar').prop('checked',data.data[res].conflicto_familiar);
            $('#id_muerte_ser_querido').prop('checked',data.data[res].muerte_ser_querido);
            $('#id_presion_redes_sociales').prop('checked',data.data[res].presion_redes_sociales);
            $('#id_dias_festivos').prop('checked',data.data[res].dias_festivos);
            $('#id_divorcio_padres').prop('checked',data.data[res].divorcio_padres);
            $('#id_perdida_trabajo').prop('checked',data.data[res].perdida_trabajo);
            $('#id_conflicto_laboral').prop('checked',data.data[res].conflicto_laboral);
            $('#id_separacion_conyugal').prop('checked',data.data[res].separacion_conyugal);
            $('#id_abuso_sexual').prop('checked',data.data[res].abuso_sexual);
            $('#id_conflicto_amoroso').prop('checked',data.data[res].conflicto_amoroso);
        }
        $('#modalVerTest').modal('toggle');
    })
    .catch(err => {
        $('#modalError').modal('toggle');
    });
}

$('#modalVerTest').on('show.bs.modal', function (event) {
    $("#verTestBeckForm :input").prop("disabled", true);
});

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
$('#modalEditarPaciente').on('show.bs.modal', function (event) {
    $('#id_birth_date').prop( "disabled", true );
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