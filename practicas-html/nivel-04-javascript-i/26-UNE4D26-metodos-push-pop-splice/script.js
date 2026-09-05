const topics = ["Variables", "Condicionales", "Ciclos", "Arreglos"];
const form = document.querySelector("#array-form");
const newItemInput = document.querySelector("#new-item");
const popButton = document.querySelector("#pop-item");
const spliceButton = document.querySelector("#splice-item");
const indexInput = document.querySelector("#remove-index");
const message = document.querySelector("#method-message");
const list = document.querySelector("#array-list");
const state = document.querySelector("#array-state");

function renderArray() {
  list.replaceChildren();
  topics.forEach((topic, index) => {
    const item = document.createElement("span");
    item.textContent = index + ": " + topic;
    list.append(item);
  });
  state.textContent = JSON.stringify(topics);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  const value = newItemInput.value.trim();
  topics.push(value);
  message.textContent = "push agregó “" + value + "” al final.";
  newItemInput.value = "";
  renderArray();
});

popButton.addEventListener("click", () => {
  const removed = topics.pop();
  message.textContent = removed === undefined
    ? "pop no encontró elementos para eliminar."
    : "pop eliminó “" + removed + "”.";
  renderArray();
});

spliceButton.addEventListener("click", () => {
  const index = Number(indexInput.value);
  const removed = topics.splice(index, 1);
  message.textContent = removed.length === 0
    ? "splice no encontró ese índice."
    : "splice eliminó “" + removed[0] + "” del índice " + index + ".";
  renderArray();
});

renderArray();
