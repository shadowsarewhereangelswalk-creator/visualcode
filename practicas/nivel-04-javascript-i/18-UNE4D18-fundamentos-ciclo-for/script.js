const form = document.querySelector("#table-form");
const baseInput = document.querySelector("#base-number");
const limitInput = document.querySelector("#limit");
const table = document.querySelector("#multiplication-table");
const iterationCount = document.querySelector("#iteration-count");
const lastResult = document.querySelector("#last-result");

function generateTable() {
  const base = Number(baseInput.value);
  const limit = Number(limitInput.value);
  table.replaceChildren();
  let finalValue = 0;
  for (let i = 1; i <= limit; i += 1) {
    const result = base * i;
    const item = document.createElement("li");
    item.textContent = base + " × " + i + " = " + result;
    table.append(item);
    finalValue = result;
  }
  iterationCount.textContent = String(limit);
  lastResult.textContent = String(finalValue);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  generateTable();
});

generateTable();
