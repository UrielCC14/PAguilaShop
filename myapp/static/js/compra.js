function toggleBox(boxNumber) {
    var box = document.getElementById('box' + boxNumber);
    if (box.style.display === 'none') {
        box.style.display = 'block';
    } else {
        box.style.display = 'none';
    }
}

//Extraer ID de la direccion
document.addEventListener("DOMContentLoaded", function () {
    var botonesElegir = document.querySelectorAll(".elegir-direccion");

    botonesElegir.forEach(function (boton) {
        boton.addEventListener("click", function () {
            var id_address = boton.getAttribute("data-id");
            seleccionarDireccion(id_address);
        });
    });

    function seleccionarDireccion(id) {
        // Aquí puedes usar el ID para realizar acciones en JavaScript
        console.log("ID de dirección seleccionada: " + id);

        // Obtén el campo por nombre
        var campoDireccion = document.querySelector('input[name="delivery_address"]');

        // Asigna el valor al campo
        if (campoDireccion) {
            console.log("Prueba de dirección seleccionada: " + id);
            campoDireccion.value = id;
        } else {
            console.log("Campo no encontrado");
        }

    }
});


//Extraer ID de la Targeta
document.addEventListener("DOMContentLoaded", function () {
    var botonesElegirT = document.querySelectorAll(".elegir-targeta");

    botonesElegirT.forEach(function (boton) {
        boton.addEventListener("click", function () {
            var id_target = boton.getAttribute("dataT-id");
            seleccionarTargeta(id_target);
        });
    });

    function seleccionarTargeta(id) {
        // Aquí puedes usar el ID para realizar acciones en JavaScript
        console.log("ID de dirección seleccionada: " + id);

        // Obtén el campo por nombre
        var campoTargeta = document.querySelector('input[name="payment_method"]');

        // Asigna el valor al campo
        if (campoTargeta) {
            console.log("Prueba de targeta seleccionada: " + id);
            campoTargeta.value = id;
        } else {
            console.log("Campo no encontrado");
        }

    }
});

//Obteniendo el precio total de la compra.
// Obtén referencias a los campos del formulario
const unidadesInput = document.getElementById("amount");
const precioInput = document.getElementById("price");
const totalInput = document.getElementById("total");

// Escucha el evento 'input' en el campo de unidades
unidadesInput.addEventListener("input", function() {
    const unidades = parseInt(unidadesInput.value, 10); // Obtén el valor de unidades como entero
    const precio = parseFloat(precioInput.value); // Obtén el valor de precio como número decimal

    // Calcula el total y lo asigna al campo "total"
    const total = unidades * precio;
    totalInput.value = total.toFixed(2); // Asegura que el total tenga dos decimales
});