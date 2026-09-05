const status = document.querySelector("#connection-status");
const detail = document.querySelector("#connection-detail");
const runButton = document.querySelector("#run");
const countButton = document.querySelector("#count");
const messages = document.querySelector("#messages");
let executions = 0;

status.textContent = "JavaScript conectado";
detail.textContent = "El archivo script.js se ejecutó correctamente.";
console.log("JavaScript está vinculado con el documento HTML");

function addMessage(text) {
  const item = document.createElement("li");
  item.textContent = text;
  messages.prepend(item);
}

runButton.addEventListener("click", () => {
  executions += 1;
  const message = "Mensaje ejecutado correctamente";
  console.log(message, executions);
  addMessage(message + " · ejecución " + executions);
});

countButton.addEventListener("click", () => {
  console.info("Total de ejecuciones:", executions);
  addMessage("La consola registra " + executions + " ejecuciones.");
});
