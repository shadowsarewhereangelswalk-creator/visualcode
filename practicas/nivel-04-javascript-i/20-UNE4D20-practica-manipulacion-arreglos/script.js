const technologies = ["HTML", "CSS", "JavaScript", "Git"];
const form = document.querySelector("#technology-form");
const technologyInput = document.querySelector("#technology");
const searchInput = document.querySelector("#search");
const list = document.querySelector("#technology-list");
const countOutput = document.querySelector("#technology-count");
const previewOutput = document.querySelector("#array-preview");
const messageOutput = document.querySelector("#array-message");
const removeButton = document.querySelector("#remove-last");
const sortButton = document.querySelector("#sort-list");
const reverseButton = document.querySelector("#reverse-list");

function renderTechnologies(operationMessage = "") {
  const query = searchInput.value.trim().toLowerCase();
  list.replaceChildren();
  let matches = 0;
  for (let index = 0; index < technologies.length; index += 1) {
    const technology = technologies[index];
    if (technology.toLowerCase().includes(query)) {
      const item = document.createElement("li");
      const position = document.createElement("span");
      position.textContent = String(index);
      item.append(position, technology);
      list.append(item);
      matches += 1;
    }
  }
  countOutput.textContent = String(technologies.length);
  previewOutput.textContent = JSON.stringify(technologies);
  messageOutput.textContent = operationMessage || (query ? matches + " coincidencias encontradas." : "Se muestran todos los elementos.");
}

form.addEventListener("submit", event => {
  event.preventDefault();
  const value = technologyInput.value.trim();
  if (value !== "") {
    technologies.push(value);
    technologyInput.value = "";
    renderTechnologies("push agregó “" + value + "”.");
  }
});

removeButton.addEventListener("click", () => {
  const removed = technologies.pop();
  renderTechnologies(removed ? "pop eliminó “" + removed + "”." : "El arreglo ya está vacío.");
});

sortButton.addEventListener("click", () => {
  technologies.sort((a, b) => a.localeCompare(b));
  renderTechnologies("El arreglo quedó ordenado alfabéticamente.");
});

reverseButton.addEventListener("click", () => {
  technologies.reverse();
  renderTechnologies("El orden del arreglo fue invertido.");
});

searchInput.addEventListener("input", () => renderTechnologies());
renderTechnologies();
