const form = document.querySelector("#type-form");
const rawInput = document.querySelector("#raw-value");
const conversionSelect = document.querySelector("#conversion");
const originalValue = document.querySelector("#original-value");
const originalType = document.querySelector("#original-type");
const convertedValue = document.querySelector("#converted-value");
const convertedType = document.querySelector("#converted-type");
const errorOutput = document.querySelector("#type-error");

function convertValue(value, target) {
  if (target === "string") return String(value);
  if (target === "number") return Number(value);
  if (target === "boolean") return value.trim().toLowerCase() === "true" || value === "1";
  if (target === "json") return JSON.parse(value);
  return value;
}

function inspect() {
  const raw = rawInput.value;
  errorOutput.textContent = "";
  originalValue.textContent = JSON.stringify(raw);
  originalType.textContent = typeof raw;
  try {
    const converted = convertValue(raw, conversionSelect.value);
    convertedValue.textContent = JSON.stringify(converted);
    convertedType.textContent = typeof converted;
  } catch (error) {
    convertedValue.textContent = "Conversión no disponible";
    convertedType.textContent = "error";
    errorOutput.textContent = "Para un objeto JSON usa un valor como {\"curso\":\"JavaScript\"}.";
  }
}

form.addEventListener("submit", event => {
  event.preventDefault();
  inspect();
});

inspect();
