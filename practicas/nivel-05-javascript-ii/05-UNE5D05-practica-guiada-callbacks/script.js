const textInput = document.querySelector("#source-text");
const buttons = document.querySelectorAll("[data-transform]");
const nameOutput = document.querySelector("#transformation-name");
const resultOutput = document.querySelector("#transformation-result");

function transformText(text, callback) {
  return callback(text);
}

const transformations = {
  uppercase:text => text.toUpperCase(),
  reverse:text => [...text].reverse().join(""),
  words:text => String(text.trim() === "" ? 0 : text.trim().split(/\s+/).length) + " palabras",
  slug:text => text.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().trim().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")
};

const labels = {
  uppercase:"Conversión a mayúsculas",
  reverse:"Inversión de caracteres",
  words:"Conteo de palabras",
  slug:"Slug para URL"
};

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const type = button.dataset.transform;
    nameOutput.textContent = labels[type];
    resultOutput.textContent = transformText(textInput.value, transformations[type]);
  });
});

resultOutput.textContent = textInput.value;
