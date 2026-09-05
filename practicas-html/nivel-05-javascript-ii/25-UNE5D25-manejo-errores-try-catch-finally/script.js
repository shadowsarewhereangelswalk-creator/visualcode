const form = document.querySelector("#json-form");
const input = document.querySelector("#json-input");
const result = document.querySelector("#json-result");
const title = document.querySelector("#json-title");
const output = document.querySelector("#json-output");
const finallyMessage = document.querySelector("#finally-message");
const attemptsOutput = document.querySelector("#attempts");
const successesOutput = document.querySelector("#successes");
const failuresOutput = document.querySelector("#failures");
const invalidButton = document.querySelector("#invalid-sample");
let attempts = 0;
let successes = 0;
let failures = 0;

function updateStats() {
  attemptsOutput.textContent = String(attempts);
  successesOutput.textContent = String(successes);
  failuresOutput.textContent = String(failures);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  attempts += 1;
  result.className = "json-result";
  finallyMessage.textContent = "";
  try {
    const data = JSON.parse(input.value);
    if (data === null || typeof data !== "object") throw new Error("El JSON debe representar un objeto o arreglo.");
    successes += 1;
    result.classList.add("success");
    title.textContent = "JSON válido";
    output.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    failures += 1;
    result.classList.add("failure");
    title.textContent = "Error capturado";
    output.textContent = error.message;
  } finally {
    finallyMessage.textContent = "finally: el intento terminó y las estadísticas fueron actualizadas.";
    updateStats();
  }
});

invalidButton.addEventListener("click", () => {
  input.value = '{"curso":"JavaScript", nivel:5}';
  form.requestSubmit();
});
