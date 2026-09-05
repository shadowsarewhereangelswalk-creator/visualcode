const taxRate = 0.16;
const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const form = document.querySelector("#product-form");
const productInput = document.querySelector("#product");
const priceInput = document.querySelector("#price");
const quantityInput = document.querySelector("#quantity");
const productOutput = document.querySelector("#receipt-product");
const subtotalOutput = document.querySelector("#subtotal");
const taxOutput = document.querySelector("#tax");
const totalOutput = document.querySelector("#total");
let subtotal = 0;
let tax = 0;
let total = 0;

function calculate() {
  const price = Number(priceInput.value);
  const quantity = Number(quantityInput.value);
  subtotal = price * quantity;
  tax = subtotal * taxRate;
  total = subtotal + tax;
  productOutput.textContent = productInput.value;
  subtotalOutput.textContent = currency.format(subtotal);
  taxOutput.textContent = currency.format(tax);
  totalOutput.textContent = currency.format(total);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  calculate();
});

calculate();
