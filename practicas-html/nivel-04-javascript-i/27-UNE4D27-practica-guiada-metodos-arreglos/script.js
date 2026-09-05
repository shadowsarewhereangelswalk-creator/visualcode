const tracks = [
  {title:"Inicio", artist:"Estudio Uno"},
  {title:"Código Azul", artist:"Nave Digital"},
  {title:"Nueva Ruta", artist:"Horizonte"}
];
const form = document.querySelector("#track-form");
const titleInput = document.querySelector("#track-title");
const artistInput = document.querySelector("#track-artist");
const removeLastButton = document.querySelector("#remove-last");
const insertButton = document.querySelector("#insert-demo");
const playlist = document.querySelector("#playlist");
const status = document.querySelector("#playlist-status");

function renderPlaylist() {
  playlist.replaceChildren();
  tracks.forEach((track, index) => {
    const item = document.createElement("li");
    const info = document.createElement("div");
    const title = document.createElement("strong");
    const artist = document.createElement("span");
    const remove = document.createElement("button");
    info.className = "track-info";
    title.textContent = track.title;
    artist.textContent = track.artist;
    remove.className = "remove-track";
    remove.type = "button";
    remove.textContent = "Eliminar";
    remove.addEventListener("click", () => {
      const removed = tracks.splice(index, 1)[0];
      status.textContent = "splice eliminó “" + removed.title + "”.";
      renderPlaylist();
    });
    info.append(title, artist);
    item.append(info, remove);
    playlist.append(item);
  });
  if (tracks.length === 0) status.textContent = "La lista de reproducción está vacía.";
}

form.addEventListener("submit", event => {
  event.preventDefault();
  tracks.push({title:titleInput.value.trim(), artist:artistInput.value.trim()});
  status.textContent = "push agregó una canción al final.";
  form.reset();
  renderPlaylist();
});

removeLastButton.addEventListener("click", () => {
  const removed = tracks.pop();
  status.textContent = removed ? "pop quitó “" + removed.title + "”." : "No hay canciones para quitar.";
  renderPlaylist();
});

insertButton.addEventListener("click", () => {
  tracks.splice(1, 0, {title:"Pista insertada", artist:"Demo JavaScript"});
  status.textContent = "splice insertó una canción en el índice 1.";
  renderPlaylist();
});

renderPlaylist();
