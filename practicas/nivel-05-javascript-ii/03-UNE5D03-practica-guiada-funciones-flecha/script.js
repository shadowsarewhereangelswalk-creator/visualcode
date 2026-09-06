const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const form = document.querySelector("#price-form");
const priceInput = document.querySelector("#base-price");
const discountInput = document.querySelector("#discount");
const taxInput = document.querySelector("#tax");
const baseOutput = document.querySelector("#base-output");
const discountOutput = document.querySelector("#discount-output");
const taxOutput = document.querySelector("#tax-output");
const finalOutput = document.querySelector("#final-output");
const formulaOutput = document.querySelector("#formula-output");

const percentage = (amount, rate) => amount * rate / 100;
const subtractDiscount = (amount, rate) => amount - percentage(amount, rate);
const addTax = (amount, rate) => amount + percentage(amount, rate);
const money = amount => currency.format(amount);

const calculate = () => {
  const base = Number(priceInput.value);
  const discountRate = Number(discountInput.value);
  const taxRate = Number(taxInput.value);
  const discounted = subtractDiscount(base, discountRate);
  const finalPrice = addTax(discounted, taxRate);
  baseOutput.textContent = money(base);
  discountOutput.textContent = "−" + money(percentage(base, discountRate));
  taxOutput.textContent = money(percentage(discounted, taxRate));
  finalOutput.textContent = money(finalPrice);
  formulaOutput.textContent = "addTax(subtractDiscount(" + base + ", " + discountRate + "), " + taxRate + ")";
};

form.addEventListener("submit", event => {
  event.preventDefault();
  calculate();
});

calculate();
