const amounts = [24.5, 18, 32.75, 15.25, 40];
const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const list = document.querySelector("#amount-list");
const labelOutput = document.querySelector("#reduce-label");
const valueOutput = document.querySelector("#reduce-value");
const stepsOutput = document.querySelector("#reduce-steps");
const totalButton = document.querySelector("#calculate-total");
const averageButton = document.querySelector("#calculate-average");

amounts.forEach(amount => {
  const item = document.createElement("span");
  item.textContent = currency.format(amount);
  list.append(item);
});

function totalAmounts() {
  return amounts.reduce((accumulator, amount) => accumulator + amount, 0);
}

totalButton.addEventListener("click", () => {
  const total = totalAmounts();
  labelOutput.textContent = "Total acumulado";
  valueOutput.textContent = currency.format(total);
  stepsOutput.textContent = amounts.join(" + ") + " = " + total;
});

averageButton.addEventListener("click", () => {
  const average = amounts.reduce((accumulator, amount) => accumulator + amount, 0) / amounts.length;
  labelOutput.textContent = "Promedio";
  valueOutput.textContent = currency.format(average);
  stepsOutput.textContent = "Suma ÷ " + amounts.length + " elementos";
});

totalButton.click();
