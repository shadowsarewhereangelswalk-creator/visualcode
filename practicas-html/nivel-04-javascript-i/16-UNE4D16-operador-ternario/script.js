const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const form = document.querySelector("#ticket-form");
const ageInput = document.querySelector("#visitor-age");
const memberInput = document.querySelector("#member");
const typeOutput = document.querySelector("#ticket-type");
const discountOutput = document.querySelector("#discount-text");
const priceOutput = document.querySelector("#ticket-price");

function calculateTicket() {
  const age = Number(ageInput.value);
  const basePrice = age < 18 ? 8 : age >= 65 ? 7 : 15;
  const type = age < 18 ? "Entrada juvenil" : age >= 65 ? "Entrada sénior" : "Entrada general";
  const finalPrice = memberInput.checked ? basePrice * 0.8 : basePrice;
  typeOutput.textContent = type;
  discountOutput.textContent = memberInput.checked ? "20% de descuento por membresía" : "Precio regular";
  priceOutput.textContent = currency.format(finalPrice);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  calculateTicket();
});

memberInput.addEventListener("change", calculateTicket);
calculateTicket();
