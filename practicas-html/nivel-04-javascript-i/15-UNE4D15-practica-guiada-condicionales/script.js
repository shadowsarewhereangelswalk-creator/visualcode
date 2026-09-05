const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const form = document.querySelector("#shipping-form");
const destination = document.querySelector("#destination");
const orderValue = document.querySelector("#order-value");
const weight = document.querySelector("#weight");
const methodOutput = document.querySelector("#shipping-method");
const messageOutput = document.querySelector("#shipping-message");
const costOutput = document.querySelector("#shipping-cost");

function calculateShipping() {
  const zone = destination.value;
  const order = Number(orderValue.value);
  const kilograms = Number(weight.value);
  let baseCost;
  let method;
  if (zone === "local") {
    baseCost = 4;
    method = "Entrega local";
  } else if (zone === "national") {
    baseCost = 8 + kilograms * 1.5;
    method = "Paquetería nacional";
  } else {
    baseCost = 20 + kilograms * 4;
    method = "Envío internacional";
  }
  if (order >= 100 && zone !== "international") {
    baseCost = 0;
    messageOutput.textContent = "Envío gratuito por superar $100.";
  } else if (kilograms > 10) {
    baseCost += 12;
    messageOutput.textContent = "Incluye recargo por peso mayor de 10 kg.";
  } else {
    messageOutput.textContent = "Tarifa estándar aplicada.";
  }
  methodOutput.textContent = method;
  costOutput.textContent = currency.format(baseCost);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  calculateShipping();
});

calculateShipping();
