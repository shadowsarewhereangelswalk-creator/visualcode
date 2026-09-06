const form = document.querySelector("#converter-form");
const temperatureInput = document.querySelector("#temperature");
const directionSelect = document.querySelector("#direction");
const sourceOutput = document.querySelector("#source-value");
const resultOutput = document.querySelector("#result-value");
const inputType = document.querySelector("#input-type");
const numberType = document.querySelector("#number-type");

function convert() {
  const rawValue = temperatureInput.value;
  const numericValue = Number(rawValue);
  const toFahrenheit = directionSelect.value === "c-to-f";
  const result = toFahrenheit
    ? numericValue * 9 / 5 + 32
    : (numericValue - 32) * 5 / 9;
  const sourceUnit = toFahrenheit ? "°C" : "°F";
  const resultUnit = toFahrenheit ? "°F" : "°C";
  sourceOutput.textContent = numericValue.toFixed(1) + " " + sourceUnit;
  resultOutput.textContent = result.toFixed(1) + " " + resultUnit;
  inputType.textContent = typeof rawValue;
  numberType.textContent = typeof numericValue;
}

form.addEventListener("submit", event => {
  event.preventDefault();
  convert();
});

directionSelect.addEventListener("change", convert);
convert();
