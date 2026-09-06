const buttons = document.querySelectorAll("[data-window]");
const history = document.querySelector("#window-history");

function record(text) {
  const item = document.createElement("li");
  item.textContent = text;
  history.prepend(item);
}

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const type = button.dataset.window;
    if (type === "alert") {
      window.alert("Este mensaje fue creado con alert().");
      record("alert: la persona cerró el mensaje.");
    }
    if (type === "confirm") {
      const answer = window.confirm("¿Deseas continuar con la práctica?");
      record("confirm: respuesta " + (answer ? "Aceptar" : "Cancelar") + ".");
    }
    if (type === "prompt") {
      const answer = window.prompt("Escribe tu lenguaje favorito:", "JavaScript");
      record("prompt: " + (answer === null ? "respuesta cancelada" : "respuesta " + answer) + ".");
    }
  });
});
