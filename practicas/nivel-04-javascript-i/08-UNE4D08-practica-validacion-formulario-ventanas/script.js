const form = document.querySelector("#registration-form");
const nameInput = document.querySelector("#student-name");
const emailInput = document.querySelector("#student-email");
const courseSelect = document.querySelector("#course");
const personalizeButton = document.querySelector("#personalize");
const receipt = document.querySelector("#receipt");
const receiptText = document.querySelector("#receipt-text");

personalizeButton.addEventListener("click", () => {
  const answer = window.prompt("¿Cuál es tu nombre?", nameInput.value);
  if (answer !== null && answer.trim() !== "") {
    nameInput.value = answer.trim();
    window.alert("Nombre agregado al formulario.");
  }
});

form.addEventListener("submit", event => {
  event.preventDefault();
  if (!form.checkValidity()) {
    window.alert("Completa correctamente todos los campos.");
    form.reportValidity();
    return;
  }
  const summary = nameInput.value + " se registrará en " + courseSelect.value + " con el correo " + emailInput.value + ".";
  const accepted = window.confirm(summary + " ¿Confirmas el registro?");
  if (!accepted) {
    window.alert("El registro fue cancelado. Puedes revisar los datos.");
    return;
  }
  receiptText.textContent = summary;
  receipt.hidden = false;
  window.alert("Registro enviado correctamente.");
});
