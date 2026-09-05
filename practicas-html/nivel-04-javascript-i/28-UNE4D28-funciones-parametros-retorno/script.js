const form = document.querySelector("#unit-form");
const valueInput = document.querySelector("#unit-value");
const operationSelect = document.querySelector("#unit-operation");
const callOutput = document.querySelector("#function-call");
const resultOutput = document.querySelector("#unit-result");
const descriptionOutput = document.querySelector("#unit-description");

function kilometersToMiles(kilometers) {
  return kilometers * 0.621371;
}

function milesToKilometers(miles) {
  return miles / 0.621371;
}

function kilogramsToPounds(kilograms) {
  return kilograms * 2.20462;
}

function poundsToKilograms(pounds) {
  return pounds / 2.20462;
}

function convertValue(value, operation) {
  if (operation === "km-miles") return {result:kilometersToMiles(value), unit:"mi", call:"kilometersToMiles(" + value + ")"};
  if (operation === "miles-km") return {result:milesToKilometers(value), unit:"km", call:"milesToKilometers(" + value + ")"};
  if (operation === "kg-pounds") return {result:kilogramsToPounds(value), unit:"lb", call:"kilogramsToPounds(" + value + ")"};
  return {result:poundsToKilograms(value), unit:"kg", call:"poundsToKilograms(" + value + ")"};
}

function renderConversion() {
  const value = Number(valueInput.value);
  const conversion = convertValue(value, operationSelect.value);
  callOutput.textContent = conversion.call;
  resultOutput.textContent = conversion.result.toFixed(2) + " " + conversion.unit;
  descriptionOutput.textContent = "La función recibió " + value + " como argumento y devolvió " + conversion.result.toFixed(4) + ".";
}

form.addEventListener("submit", event => {
  event.preventDefault();
  renderConversion();
});

operationSelect.addEventListener("change", renderConversion);
renderConversion();
