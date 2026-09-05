const apiBase = "https://jsonplaceholder.typicode.com/posts/";
const form = document.querySelector("#post-form");
const idInput = document.querySelector("#post-id");
const randomButton = document.querySelector("#random-post");
const numberOutput = document.querySelector("#post-number");
const titleOutput = document.querySelector("#post-title");
const bodyOutput = document.querySelector("#post-body");
const statusOutput = document.querySelector("#post-status");

async function fetchPost(id) {
  statusOutput.textContent = "Consultando la publicación " + id + "...";
  try {
    const response = await fetch(apiBase + id);
    if (!response.ok) throw new Error("Respuesta HTTP " + response.status);
    const post = await response.json();
    numberOutput.textContent = "Publicación " + post.id;
    titleOutput.textContent = post.title;
    bodyOutput.textContent = post.body;
    statusOutput.textContent = "Consulta completada.";
  } catch (error) {
    numberOutput.textContent = "Error";
    titleOutput.textContent = "No se pudo cargar la publicación";
    bodyOutput.textContent = error.message;
    statusOutput.textContent = "Revisa la conexión e inténtalo de nuevo.";
  }
}

form.addEventListener("submit", event => {
  event.preventDefault();
  fetchPost(Number(idInput.value));
});

randomButton.addEventListener("click", () => {
  const id = Math.floor(Math.random() * 100) + 1;
  idInput.value = String(id);
  fetchPost(id);
});

fetchPost(1);
