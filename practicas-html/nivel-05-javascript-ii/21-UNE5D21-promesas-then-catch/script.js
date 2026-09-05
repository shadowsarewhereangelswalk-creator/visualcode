const form = document.querySelector("#promise-form");
const delayInput = document.querySelector("#promise-delay");
const resultSelect = document.querySelector("#promise-result");
const messageOutput = document.querySelector("#promise-message");
const pendingState = document.querySelector("#state-pending");
const resolvedState = document.querySelector("#state-resolved");
const rejectedState = document.querySelector("#state-rejected");

function resetStates() {
  pendingState.className = "";
  resolvedState.className = "";
  rejectedState.className = "";
}

function createPromise(delay, shouldResolve) {
  return new Promise((resolve, reject) => {
    window.setTimeout(() => {
      if (shouldResolve) resolve("La promesa entregó sus datos.");
      else reject(new Error("La promesa simuló un error."));
    }, delay);
  });
}

form.addEventListener("submit", event => {
  event.preventDefault();
  resetStates();
  pendingState.className = "active";
  messageOutput.textContent = "Estado pendiente...";
  createPromise(Number(delayInput.value), resultSelect.value === "success")
    .then(message => {
      pendingState.className = "";
      resolvedState.className = "success";
      messageOutput.textContent = "then(): " + message;
    })
    .catch(error => {
      pendingState.className = "";
      rejectedState.className = "error-state";
      messageOutput.textContent = "catch(): " + error.message;
    });
});
