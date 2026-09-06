const symbols = {add:"+", subtract:"−", multiply:"×", divide:"÷"};
const form = document.querySelector("#calculator-form");
const firstInput = document.querySelector("#number-one");
const secondInput = document.querySelector("#number-two");
const operationSelect = document.querySelector("#operation");
const resultBox = document.querySelector("#calculator-result");
const expressionOutput = document.querySelector("#expression");
const answerOutput = document.querySelector("#answer");
const classificationOutput = document.querySelector("#classification");

function calculate() {
  const first = Number(firstInput.value);
  const second = Number(secondInput.value);
  const operation = operationSelect.value;
  let result;
  let error = "";
  if (operation === "add") result = first + second;
  else if (operation === "subtract") result = first - second;
  else if (operation === "multiply") result = first * second;
  else if (operation === "divide" && second !== 0) result = first / second;
  else error = "No se puede dividir entre cero.";
  expressionOutput.textContent = first + " " + symbols[operation] + " " + second;
  resultBox.classList.toggle("error-state", Boolean(error));
  if (error) {
    answerOutput.textContent = "Error";
    classificationOutput.textContent = error;
    return;
  }
  answerOutput.textContent = Number.isInteger(result) ? String(result) : result.toFixed(2);
  classificationOutput.textContent = result > 0
    ? "El resultado es positivo."
    : result < 0
      ? "El resultado es negativo."
      : "El resultado es cero.";
}

form.addEventListener("submit", event => {
  event.preventDefault();
  calculate();
});

calculate();
