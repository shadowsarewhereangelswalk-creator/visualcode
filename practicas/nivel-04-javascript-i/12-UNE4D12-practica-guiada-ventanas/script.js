const unitPrice = 12.5;
const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const startButton = document.querySelector("#start-order");
const card = document.querySelector("#order-card");
const productOutput = document.querySelector("#order-product");
const quantityOutput = document.querySelector("#order-quantity");
const totalOutput = document.querySelector("#order-total");
const statusOutput = document.querySelector("#order-status");

startButton.addEventListener("click", () => {
  const product = window.prompt("¿Qué producto deseas pedir?", "Cuaderno digital");
  if (product === null || product.trim() === "") {
    statusOutput.textContent = "Pedido cancelado: no se indicó un producto.";
    return;
  }
  const quantityText = window.prompt("¿Cuántas unidades deseas?", "1");
  const quantity = Number(quantityText);
  if (!Number.isInteger(quantity) || quantity < 1) {
    window.alert("La cantidad debe ser un número entero mayor que cero.");
    statusOutput.textContent = "Pedido cancelado por una cantidad inválida.";
    return;
  }
  const total = unitPrice * quantity;
  const accepted = window.confirm("Total: " + currency.format(total) + ". ¿Confirmas el pedido?");
  if (!accepted) {
    statusOutput.textContent = "El pedido fue cancelado antes de enviarse.";
    return;
  }
  productOutput.textContent = product.trim();
  quantityOutput.textContent = String(quantity);
  totalOutput.textContent = currency.format(total);
  card.hidden = false;
  statusOutput.textContent = "El pedido quedó registrado correctamente.";
  window.alert("Pedido confirmado.");
});
