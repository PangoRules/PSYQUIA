// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    search: false,
    dom: 'Bfrtip',
    ordering: true,
    order : [[0,"desc"]],
    oLanguage: {
      sInfo: "Total de _TOTAL_ entradas a mostrar (_START_ to _END_)"
    },
    buttons: [
      'copyHtml5',
      'excelHtml5',
      'csvHtml5',
      'pdfHtml5'
    ],
    language: {
    zeroRecords: "No se encontraron resultados",
    //info: "Ver pagina _PAGE_ de _PAGES_",
    lengthMenu: "Ver _MENU_ elementos por pagina",
    infoEmpty: "Sin elementos disponibles",
    infoFiltered: "(filtro de un total de _MAX_ cédulas)",
    search: "Buscar",
    
    paginate: {
      previous: "Anterior",
        next : "Siguiente"
    }
    }
  });
});
