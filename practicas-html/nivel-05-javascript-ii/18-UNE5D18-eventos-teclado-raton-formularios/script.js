const clickTarget = document.querySelector("#click-target");
const hoverTarget = document.querySelector("#hover-target");
const typingTarget = document.querySelector("#typing-target");
const form = document.querySelector("#sample-form");
const emailInput = document.querySelector("#event-email");
const typeOutput = document.querySelector("#event-type");
const targetOutput = document.querySelector("#event-target");
const dataOutput = document.querySelector("#event-data");
const countOutput = document.querySelector("#event-count");
let count = 0;

function inspectEvent(type, target, data) {
  count += 1;
  typeOutput.textContent = type;
  targetOutput.textContent = target;
  dataOutput.textContent = data;
  countOutput.textContent = String(count);
}

clickTarget.addEventListener("click", event => inspectEvent(event.type, event.target.tagName, "Botón activado"));
hoverTarget.addEventListener("mouseenter", event => {
  hoverTarget.classList.add("active");
  inspectEvent(event.type, event.target.tagName, "Puntero dentro");
});
hoverTarget.addEventListener("mouseleave", event => {
  hoverTarget.classList.remove("active");
  inspectEvent(event.type, event.target.tagName, "Puntero fuera");
});
hoverTarget.addEventListener("keydown", event => inspectEvent(event.type, event.target.tagName, event.key));
typingTarget.addEventListener("input", event => inspectEvent(event.type, event.target.tagName, event.target.value));
form.addEventListener("submit", event => {
  event.preventDefault();
  inspectEvent(event.type, event.target.tagName, emailInput.value);
  form.reset();
});
