const form = document.querySelector("#map-form");
const valuesInput = document.querySelector("#map-values");
const operationSelect = document.querySelector("#map-operation");
const originalOutput = document.querySelector("#original-values");
const mappedOutput = document.querySelector("#mapped-values");
const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});

function renderValues(container, values) {
  container.replaceChildren();
  values.forEach(value => {
    const item = document.createElement("span");
    item.textContent = String(value);
    container.append(item);
  });
}

function applyMap() {
  const original = valuesInput.value.split(",").map(value => Number(value.trim())).filter(Number.isFinite);
  const operation = operationSelect.value;
  const mapped = original.map(value => {
    if (operation === "double") return value * 2;
    if (operation === "square") return value ** 2;
    return currency.format(value);
  });
  renderValues(originalOutput, original);
  renderValues(mappedOutput, mapped);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  applyMap();
});

applyMap();
