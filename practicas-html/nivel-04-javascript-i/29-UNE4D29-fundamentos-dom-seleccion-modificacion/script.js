const form = document.querySelector("#editor-form");
const titleInput = document.querySelector("#card-title");
const textInput = document.querySelector("#card-text");
const colorInput = document.querySelector("#card-color");
const styleSelect = document.querySelector("#card-style");
const preview = document.querySelector("#preview-card");
const previewTitle = document.querySelector("#preview-title");
const previewText = document.querySelector("#preview-text");
const previewAction = document.querySelector("#preview-action");
const status = document.querySelector("#dom-status");
let updates = 0;

function updatePreview() {
  updates += 1;
  previewTitle.textContent = titleInput.value.trim() || "Título sin contenido";
  previewText.textContent = textInput.value.trim() || "Descripción sin contenido";
  preview.style.setProperty("--accent", colorInput.value);
  preview.className = "preview-card " + styleSelect.value;
  status.textContent = "DOM actualizado " + updates + (updates === 1 ? " vez." : " veces.");
}

form.addEventListener("submit", event => {
  event.preventDefault();
  updatePreview();
});

previewAction.addEventListener("click", () => {
  previewAction.textContent = previewAction.textContent === "Interacción lista" ? "Elemento modificado" : "Interacción lista";
});

colorInput.addEventListener("input", updatePreview);
