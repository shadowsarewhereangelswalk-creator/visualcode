const product = {
  code:"JS-205",
  name:"Curso JavaScript II",
  category:"Formación",
  stock:12,
  available:true
};
const form = document.querySelector("#inventory-form");
const movementSelect = document.querySelector("#movement");
const valueInput = document.querySelector("#movement-value");
const codeOutput = document.querySelector("#product-code");
const nameOutput = document.querySelector("#product-name");
const categoryOutput = document.querySelector("#product-category");
const stockOutput = document.querySelector("#product-stock");
const statusOutput = document.querySelector("#product-status");
const jsonOutput = document.querySelector("#inventory-json");
const messageOutput = document.querySelector("#inventory-message");

function renderProduct(message = "") {
  product.available = product.stock > 0;
  codeOutput.textContent = product.code;
  nameOutput.textContent = product.name;
  categoryOutput.textContent = product.category;
  stockOutput.textContent = product.stock + " unidades";
  statusOutput.textContent = product.available ? "Disponible" : "Agotado";
  jsonOutput.textContent = JSON.stringify(product);
  messageOutput.textContent = message;
}

movementSelect.addEventListener("change", () => {
  valueInput.value = movementSelect.value === "rename" ? product.name : "1";
  valueInput.type = movementSelect.value === "rename" ? "text" : "number";
});

form.addEventListener("submit", event => {
  event.preventDefault();
  const movement = movementSelect.value;
  if (movement === "rename") {
    product.name = valueInput.value.trim();
    renderProduct("La propiedad name fue actualizada.");
    return;
  }
  const quantity = Number(valueInput.value);
  if (!Number.isInteger(quantity) || quantity < 1) {
    renderProduct("Introduce una cantidad entera mayor que cero.");
    return;
  }
  if (movement === "add") {
    product.stock += quantity;
    renderProduct("Se agregaron " + quantity + " unidades.");
  } else if (quantity <= product.stock) {
    product.stock -= quantity;
    renderProduct("Se vendieron " + quantity + " unidades.");
  } else {
    renderProduct("No existe suficiente inventario para esa venta.");
  }
});

renderProduct("Objeto preparado para recibir cambios.");
