const form = document.querySelector("#operators-form");
const valueA = document.querySelector("#value-a");
const valueB = document.querySelector("#value-b");
const arithmetic = document.querySelector("#arithmetic");
const relational = document.querySelector("#relational");
const logical = document.querySelector("#logical");

function renderRows(container, rows) {
  container.replaceChildren();
  rows.forEach(([label, value]) => {
    const row = document.createElement("div");
    const term = document.createElement("dt");
    const description = document.createElement("dd");
    term.textContent = label;
    description.textContent = String(value);
    row.append(term, description);
    container.append(row);
  });
}

function evaluate() {
  const a = Number(valueA.value);
  const b = Number(valueB.value);
  renderRows(arithmetic, [
    ["A + B", a + b],
    ["A - B", a - b],
    ["A × B", a * b],
    ["A ÷ B", b === 0 ? "Indefinido" : (a / b).toFixed(2)],
    ["A % B", b === 0 ? "Indefinido" : a % b]
  ]);
  renderRows(relational, [
    ["A > B", a > b],
    ["A < B", a < b],
    ["A === B", a === b],
    ["A !== B", a !== b]
  ]);
  renderRows(logical, [
    ["A > 0 && B > 0", a > 0 && b > 0],
    ["A > 10 || B > 10", a > 10 || b > 10],
    ["!(A === B)", !(a === b)]
  ]);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  evaluate();
});

evaluate();
