const preview = document.querySelector("#color-preview");
const picker = document.querySelector("#color-picker");
const nameInput = document.querySelector("#color-name");
const codeOutput = document.querySelector("#color-code");
const form = document.querySelector("#color-form");
const savedColors = document.querySelector("#saved-colors");
const eventOutput = document.querySelector("#color-event");
let hue = 217;

function updateColor(color, eventName) {
  preview.style.backgroundColor = color;
  picker.value = color;
  codeOutput.textContent = color.toUpperCase();
  eventOutput.textContent = "Evento " + eventName + ": color actualizado.";
}

picker.addEventListener("input", event => updateColor(event.target.value, event.type));
preview.addEventListener("click", event => {
  eventOutput.textContent = "Evento " + event.type + ": vista previa seleccionada.";
});
preview.addEventListener("keydown", event => {
  if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
  event.preventDefault();
  hue += event.key === "ArrowRight" ? 5 : -5;
  if (hue > 360) hue = 0;
  if (hue < 0) hue = 360;
  const temporary = document.createElement("span");
  temporary.style.color = "hsl(" + hue + " 80% 52%)";
  document.body.append(temporary);
  const color = getComputedStyle(temporary).color;
  temporary.remove();
  preview.style.backgroundColor = color;
  codeOutput.textContent = "hsl(" + hue + " 80% 52%)";
  eventOutput.textContent = "Evento keydown: tono " + hue + ".";
});
form.addEventListener("submit", event => {
  event.preventDefault();
  const chip = document.createElement("article");
  const sample = document.createElement("span");
  const label = document.createElement("strong");
  chip.className = "color-chip";
  sample.style.backgroundColor = getComputedStyle(preview).backgroundColor;
  label.textContent = nameInput.value.trim();
  chip.append(sample, label);
  savedColors.append(chip);
  eventOutput.textContent = "Evento submit: muestra guardada.";
});
