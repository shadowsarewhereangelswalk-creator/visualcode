const form = document.querySelector("#filter-form");
const valuesInput = document.querySelector("#filter-values");
const ruleSelect = document.querySelector("#filter-rule");
const limitInput = document.querySelector("#filter-limit");
const allOutput = document.querySelector("#all-numbers");
const filteredOutput = document.querySelector("#filtered-numbers");
const countOutput = document.querySelector("#filter-count");

function renderNumbers(container, numbers) {
  container.replaceChildren();
  numbers.forEach(number => {
    const item = document.createElement("span");
    item.textContent = String(number);
    container.append(item);
  });
}

function applyFilter() {
  const numbers = valuesInput.value.split(",").map(value => Number(value.trim())).filter(Number.isFinite);
  const rule = ruleSelect.value;
  const limit = Number(limitInput.value);
  const filtered = numbers.filter(number => {
    if (rule === "even") return number % 2 === 0;
    if (rule === "odd") return number % 2 !== 0;
    if (rule === "greater") return number > limit;
    return number < limit;
  });
  renderNumbers(allOutput, numbers);
  renderNumbers(filteredOutput, filtered);
  countOutput.textContent = "filter() conservó " + filtered.length + " de " + numbers.length + " elementos.";
}

form.addEventListener("submit", event => {
  event.preventDefault();
  applyFilter();
});

ruleSelect.addEventListener("change", applyFilter);
applyFilter();
