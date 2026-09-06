const form = document.querySelector("#access-form");
const ageInput = document.querySelector("#age");
const lessonsInput = document.querySelector("#lessons");
const rulesInput = document.querySelector("#rules");
const result = document.querySelector("#access-result");
const requirements = document.querySelector("#requirements");

function addRequirement(text, passed) {
  const item = document.createElement("li");
  item.textContent = (passed ? "✓ " : "✕ ") + text;
  requirements.append(item);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  const age = Number(ageInput.value);
  const lessons = Number(lessonsInput.value);
  const adult = age >= 18;
  const prepared = lessons >= 10;
  const accepted = rulesInput.checked;
  const approved = adult && prepared && accepted;
  requirements.replaceChildren();
  addRequirement("Tener al menos 18 años", adult);
  addRequirement("Completar 10 clases o más", prepared);
  addRequirement("Aceptar las normas", accepted);
  result.className = "decision " + (approved ? "approved" : "denied");
  result.querySelector("strong").textContent = approved
    ? "Acceso aprobado"
    : "Acceso pendiente: revisa los requisitos";
});
