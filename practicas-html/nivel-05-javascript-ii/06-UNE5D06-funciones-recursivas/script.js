const form = document.querySelector("#recursion-form");
const numberInput = document.querySelector("#recursive-number");
const countdownOutput = document.querySelector("#countdown");
const factorialOutput = document.querySelector("#factorial-result");
const expressionOutput = document.querySelector("#factorial-expression");

function factorial(number) {
  if (number <= 1) return 1;
  return number * factorial(number - 1);
}

function buildCountdown(number, values = []) {
  values.push(number);
  if (number === 0) return values;
  return buildCountdown(number - 1, values);
}

function buildExpression(number) {
  if (number <= 1) return "1";
  return number + " × " + buildExpression(number - 1);
}

function renderRecursion() {
  const number = Number(numberInput.value);
  countdownOutput.replaceChildren();
  buildCountdown(number).forEach(value => {
    const badge = document.createElement("span");
    badge.textContent = String(value);
    countdownOutput.append(badge);
  });
  factorialOutput.textContent = String(factorial(number));
  expressionOutput.textContent = buildExpression(number);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  renderRecursion();
});

renderRecursion();
