const runButton = document.querySelector("#run-sequence");
const resetButton = document.querySelector("#reset-sequence");
const messageOutput = document.querySelector("#async-message");
const phases = [...document.querySelectorAll("[data-phase]")];

const wait = milliseconds => new Promise(resolve => window.setTimeout(resolve, milliseconds));

async function executePhase(name, message) {
  const phase = document.querySelector('[data-phase="' + name + '"]');
  phase.className = "active";
  messageOutput.textContent = message;
  await wait(650);
  phase.className = "complete";
}

async function runSequence() {
  runButton.disabled = true;
  phases.forEach(phase => phase.className = "");
  await executePhase("connect", "Conectando...");
  await executePhase("receive", "Esperando los datos...");
  await executePhase("render", "Actualizando la interfaz...");
  messageOutput.textContent = "Secuencia completada con async/await.";
  runButton.disabled = false;
}

runButton.addEventListener("click", runSequence);
resetButton.addEventListener("click", () => {
  phases.forEach(phase => phase.className = "");
  messageOutput.textContent = "Secuencia lista.";
  runButton.disabled = false;
});
