const form = document.querySelector("#arrow-form");
const numbersInput = document.querySelector("#numbers");
const inputArray = document.querySelector("#input-array");
const outputArray = document.querySelector("#output-array");
const sumResult = document.querySelector("#sum-result");
const operationButtons = document.querySelectorAll("[data-operation]");

const parseNumbers = text => text.split(",").map(value => Number(value.trim())).filter(value => Number.isFinite(value));
const double = number => number * 2;
const square = number => number ** 2;
const isPositive = number => number > 0;
const sum = numbers => numbers.reduce((total, number) => total + number, 0);

const render = (result, label) => {
  const original = parseNumbers(numbersInput.value);
  inputArray.textContent = JSON.stringify(original);
  outputArray.textContent = JSON.stringify(result);
  sumResult.textContent = label;
};

operationButtons.forEach(button => {
  button.addEventListener("click", () => {
    const numbers = parseNumbers(numbersInput.value);
    const operation = button.dataset.operation;
    if (operation === "double") render(numbers.map(double), "Función: number => number * 2");
    if (operation === "square") render(numbers.map(square), "Función: number => number ** 2");
    if (operation === "positive") render(numbers.filter(isPositive), "Función: number => number > 0");
  });
});

form.addEventListener("submit", event => {
  event.preventDefault();
  const numbers = parseNumbers(numbersInput.value);
  render(numbers, "Suma: " + sum(numbers));
});

render(parseNumbers(numbersInput.value), "Lista preparada");
