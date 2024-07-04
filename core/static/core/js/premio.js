$(document).ready(function() {
  fetch("https://fakestoreapi.com/products")
    .then(response => response.json())
    .then(data => {
      $("#tabla-Api").empty();
      data.forEach(producto => {
        var fila = $("<tr>");
        fila.append("<td>" + traducirAlEspañol(producto.category) + "</td>");
        fila.append("<td>" + `<img src=${producto.image} width=40% >` + "</td>");
        fila.append("<td>" + traducirAlEspañol(producto.title) + "</td>");
        fila.append("<td>$" + producto.price + "</td>"); 
        $("#tabla-Api").append(fila);
      });
    })
    .catch(error => {
      console.error("Error al obtener datos de la API:", error);
    });
});

function traducirAlEspañol(texto) {
  const traducciones = {
    "electronics": "Electrónicos",
    "jewelery": "Joyería",
    "men's clothing": "Ropa de Hombre",
    "women's clothing": "Ropa de Mujer",
  };
  if (traducciones.hasOwnProperty(texto)) {
    return traducciones[texto];
  } else {
    return texto;
  }
}
