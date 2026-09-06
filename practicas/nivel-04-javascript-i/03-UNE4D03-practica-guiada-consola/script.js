const input = document.querySelector("#message");
const history = document.querySelector("#history");
const methodButtons = document.querySelectorAll("[data-method]");
const clearButton = document.querySelector("#clear");
let sequence = 0;

methodButtons.forEach(button => {
  button.addEventListener("click", () => {
    const method = button.dataset.method;
    const message = input.value.trim() || "Mensaje vacío";
    sequence += 1;
    console[method](message);
    const item = document.createElement("li");
    item.dataset.method = method;
    item.textContent = sequence + ". " + method.toUpperCase() + ": " + message;
    history.prepend(item);
  });
});

clearButton.addEventListener("click", () => {
  history.replaceChildren();
  sequence = 0;
  console.clear();
  input.focus();
});
