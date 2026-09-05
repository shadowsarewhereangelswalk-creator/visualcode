const taxRate = 0.16;
const form = document.querySelector("#quote-form");
const serviceInput = document.querySelector("#service");
const hoursInput = document.querySelector("#hours");
const rateInput = document.querySelector("#rate");
const discountInput = document.querySelector("#discount");
const serviceOutput = document.querySelector("#quote-service");
const subtotalOutput = document.querySelector("#quote-subtotal");
const discountOutput = document.querySelector("#quote-discount");
const taxOutput = document.querySelector("#quote-tax");
const totalOutput = document.querySelector("#quote-total");

function calculateSubtotal(hours, rate) {
  return hours * rate;
}

function calculatePercentage(amount, percentage) {
  return amount * percentage / 100;
}

function formatMoney(amount) {
  return new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"}).format(amount);
}

function buildQuote(hours, rate, discountPercentage) {
  const subtotal = calculateSubtotal(hours, rate);
  const discount = calculatePercentage(subtotal, discountPercentage);
  const taxableAmount = subtotal - discount;
  const tax = taxableAmount * taxRate;
  return {subtotal, discount, tax, total:taxableAmount + tax};
}

function renderQuote() {
  const quote = buildQuote(
    Number(hoursInput.value),
    Number(rateInput.value),
    Number(discountInput.value)
  );
  serviceOutput.textContent = serviceInput.value;
  subtotalOutput.textContent = formatMoney(quote.subtotal);
  discountOutput.textContent = "−" + formatMoney(quote.discount);
  taxOutput.textContent = formatMoney(quote.tax);
  totalOutput.textContent = formatMoney(quote.total);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  renderQuote();
});

renderQuote();
