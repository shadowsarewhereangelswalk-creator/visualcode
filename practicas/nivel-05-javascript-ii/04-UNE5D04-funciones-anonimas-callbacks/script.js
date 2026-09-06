const form = document.querySelector("#callback-form");
const valueInput = document.querySelector("#callback-value");
const operationSelect = document.querySelector("#callback-operation");
const inputOutput = document.querySelector("#callback-input");
const nameOutput = document.querySelector("#callback-name");
const resultOutput = document.querySelector("#callback-result");
const statusOutput = document.querySelector("#callback-status");

function processValue(value, callback) {
  statusOutput.textContent = "Procesando la operación...";
  window.setTimeout(function () {
    const result = callback(value);
    resultOutput.textContent = String(result);
    statusOutput.textContent = "El callback se ejecutó correctamente.";
  }, 500);
}

form.addEventListener("submit", function (event) {
  event.preventDefault();
  const value = Number(valueInput.value);
  const operation = operationSelect.value;
  const callbacks = {
    double:function (number) { return number * 2; },
    square:function (number) { return number ** 2; },
    half:function (number) { return number / 2; }
  };
  const labels = {double:"Duplicar", square:"Cuadrado", half:"Mitad"};
  inputOutput.textContent = String(value);
  nameOutput.textContent = labels[operation];
  processValue(value, callbacks[operation]);
});
