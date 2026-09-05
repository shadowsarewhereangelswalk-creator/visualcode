const startButton = document.querySelector("#start");
const roadmap = document.querySelector("#roadmap");
const topicButtons = [...document.querySelectorAll(".topic-card")];
const progressBar = document.querySelector("#progress-bar");
const progressLabel = document.querySelector("#progress-label");
const welcome = document.querySelector("#welcome");

function updateProgress() {
  const completed = topicButtons.filter(button => button.getAttribute("aria-pressed") === "true").length;
  const percentage = completed / topicButtons.length * 100;
  progressBar.style.width = percentage + "%";
  progressLabel.textContent = completed + " de " + topicButtons.length + " temas";
  welcome.textContent = completed === topicButtons.length
    ? "Recorrido preparado. Ya conoces todos los temas del nivel."
    : "Has seleccionado " + completed + " temas.";
}

startButton.addEventListener("click", () => {
  roadmap.scrollIntoView({behavior:"smooth"});
  welcome.textContent = "Selecciona cada tema para explorar la ruta.";
});

topicButtons.forEach(button => {
  button.addEventListener("click", () => {
    const selected = button.getAttribute("aria-pressed") === "true";
    button.setAttribute("aria-pressed", String(!selected));
    updateProgress();
  });
});
