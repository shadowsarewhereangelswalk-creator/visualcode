const form = document.querySelector("#order-form");
const productInput = document.querySelector("#order-product");
const amountInput = document.querySelector("#order-amount");
const paymentInput = document.querySelector("#payment-approved");
const resultOutput = document.querySelector("#order-result");
const stepElements = [...document.querySelectorAll("[data-step]")];

function delayStep(name, message, valid = true) {
  return new Promise((resolve, reject) => {
    const element = document.querySelector('[data-step="' + name + '"]');
    element.className = "active";
    window.setTimeout(() => {
      if (valid) {
        element.className = "complete";
        resolve(message);
      } else {
        element.className = "failed";
        reject(new Error(message));
      }
    }, 550);
  });
}

form.addEventListener("submit", event => {
  event.preventDefault();
  stepElements.forEach(step => step.className = "");
  resultOutput.textContent = "Procesando...";
  delayStep("validate", "Datos válidos", productInput.value.trim() !== "" && Number(amountInput.value) > 0)
    .then(message => {
      resultOutput.textContent = message;
      return delayStep("payment", "Pago aprobado", paymentInput.checked);
    })
    .then(message => {
      resultOutput.textContent = message;
      return delayStep("prepare", "Pedido preparado");
    })
    .then(() => {
      resultOutput.textContent = "Pedido completado: " + productInput.value + ".";
    })
    .catch(error => {
      resultOutput.textContent = "Proceso detenido: " + error.message + ".";
    });
});
