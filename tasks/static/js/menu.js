
$(document).ready(function() {
    // Evento de clic para el botón "Producto"
    $("#sidebar button:contains('producto')").click(function() {
        window.location.href = '/producto/';
    });

    // Evento de clic para el botón "Proveedor"
    $("#sidebar button:contains('Proveedor')").click(function() {
        cargarContenido('proveedor.html');
    });

    // Evento de clic para el botón "Cliente"
    $("#sidebar button:contains('Cliente')").click(function() {
        cargarContenido('cliente.html');
    });

    // Evento de clic para el botón "Pedidos"
    $("#sidebar button:contains('Pedidos')").click(function() {
        cargarContenido('pedidos.html');
    });

    // Función para cargar contenido dinámico
    function cargarContenido(url) {
        console.log('Intentando cargar contenido desde ' + url);

        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'html',
            success: function(data) {
                console.log('Contenido cargado con éxito:', data);
                $('#contenidoDinamico').html(data);
            },
            error: function(error) {
                console.error('Error al cargar el contenido:', error);
            }
        });
    }
});
