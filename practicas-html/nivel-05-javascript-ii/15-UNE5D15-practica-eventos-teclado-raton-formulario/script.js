const pointerArea = document.querySelector("#pointer-area");
const pointerDot = document.querySelector("#pointer-dot");
const coordinates = document.querySelector("#pointer-coordinates");
const pointerButton = document.querySelector("#pointer-click");
const keyDisplay = document.querySelector("#key-display");
const pressedKey = document.querySelector("#pressed-key");
const form = document.querySelector("#event-form");
const nameInput = document.querySelector("#event-name");
const log = document.querySelector("#event-log");
const totalOutput = document.querySelector("#event-total");
let eventCount = 0;

function recordEvent(message) {
  eventCount += 1;
  const item = document.createElement("li");
  item.textContent = eventCount + ". " + message;
  log.prepend(item);
  while (log.children.length > 12) log.lastElementChild.remove();
  totalOutput.textContent = eventCount + (eventCount === 1 ? " evento" : " eventos");
}

pointerArea.addEventListener("pointermove", event => {
  const bounds = pointerArea.getBoundingClientRect();
  const x = Math.round(event.clientX - bounds.left);
  const y = Math.round(event.clientY - bounds.top);
  pointerDot.style.left = x + "px";
  pointerDot.style.top = y + "px";
  coordinates.textContent = "x: " + x + " · y: " + y;
});

pointerButton.addEventListener("click", () => recordEvent("Clic registrado en el botón."));
pointerArea.addEventListener("pointerdown", () => recordEvent("pointerdown dentro del área."));
keyDisplay.addEventListener("keydown", event => {
  pressedKey.textContent = event.key === " " ? "Espacio" : event.key;
  recordEvent("keydown: " + event.key);
});
form.addEventListener("submit", event => {
  event.preventDefault();
  recordEvent("submit: " + nameInput.value.trim());
  form.reset();
});
