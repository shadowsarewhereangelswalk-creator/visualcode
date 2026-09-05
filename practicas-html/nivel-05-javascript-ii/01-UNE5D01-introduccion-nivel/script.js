const activateButton = document.querySelector("#activate-roadmap");
const items = [...document.querySelectorAll(".roadmap-item")];
const countOutput = document.querySelector("#roadmap-count");
const messageOutput = document.querySelector("#roadmap-message");

const updateRoadmap = () => {
  const explored = items.filter(item => item.getAttribute("aria-pressed") === "true").length;
  countOutput.textContent = explored + " de " + items.length + " exploradas";
  messageOutput.textContent = explored === items.length
    ? "Ruta completa: ya conoces todas las competencias del Nivel 5."
    : "Has explorado " + explored + " competencias.";
};

activateButton.addEventListener("click", () => {
  document.querySelector(".panel").scrollIntoView({behavior:"smooth"});
  messageOutput.textContent = "Ruta activada. Explora las seis competencias.";
});

items.forEach(item => {
  item.addEventListener("click", () => {
    const active = item.getAttribute("aria-pressed") === "true";
    item.setAttribute("aria-pressed", String(!active));
    updateRoadmap();
  });
});
