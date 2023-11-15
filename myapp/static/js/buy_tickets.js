function toggleBox(boxNumber) {
    var box = document.getElementById('box' + boxNumber);
    if (box.style.display === 'none') {
        box.style.display = 'block';
    } else {
        box.style.display = 'none';
    }
}

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