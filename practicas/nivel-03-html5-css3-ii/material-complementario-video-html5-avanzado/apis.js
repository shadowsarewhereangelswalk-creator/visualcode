const geoButton = document.getElementById("geo-btn");
const geoStatus = document.getElementById("geo-status");

geoButton.addEventListener("click", () => {
  if (!("geolocation" in navigator)) {
    geoStatus.textContent = "Este navegador no ofrece la API de geolocalización.";
    return;
  }

  geoStatus.textContent = "Solicitando permiso y ubicación…";
  navigator.geolocation.getCurrentPosition(
    (position) => {
      const { latitude, longitude, accuracy } = position.coords;
      geoStatus.textContent =
        "Latitud: " + latitude.toFixed(6) +
        "\nLongitud: " + longitude.toFixed(6) +
        "\nPrecisión aproximada: " + Math.round(accuracy) + " m";
    },
    (error) => {
      geoStatus.textContent = "No se pudo obtener la ubicación: " + error.message;
    },
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
  );
});

const note = document.getElementById("nota");
const storageStatus = document.getElementById("storage-status");

document.getElementById("local-save").addEventListener("click", () => {
  localStorage.setItem("html5_nota", note.value);
  storageStatus.textContent = "Dato guardado en localStorage.";
});
document.getElementById("local-load").addEventListener("click", () => {
  note.value = localStorage.getItem("html5_nota") || "";
  storageStatus.textContent = "Dato leído desde localStorage.";
});
document.getElementById("session-save").addEventListener("click", () => {
  sessionStorage.setItem("html5_nota", note.value);
  storageStatus.textContent = "Dato guardado en sessionStorage.";
});
document.getElementById("session-load").addEventListener("click", () => {
  note.value = sessionStorage.getItem("html5_nota") || "";
  storageStatus.textContent = "Dato leído desde sessionStorage.";
});

const dragItem = document.getElementById("drag-item");
const dropZone = document.getElementById("drop-zone");
const dragStatus = document.getElementById("drag-status");

dragItem.addEventListener("dragstart", (event) => {
  event.dataTransfer.setData("text/plain", dragItem.id);
  event.dataTransfer.effectAllowed = "move";
  dragStatus.textContent = "Elemento en movimiento.";
});

dropZone.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropZone.classList.add("active");
  event.dataTransfer.dropEffect = "move";
});

dropZone.addEventListener("dragleave", () => {
  dropZone.classList.remove("active");
});

dropZone.addEventListener("drop", (event) => {
  event.preventDefault();
  dropZone.classList.remove("active");
  const id = event.dataTransfer.getData("text/plain");
  const element = document.getElementById(id);
  if (element) {
    dropZone.replaceChildren(element);
    dragStatus.textContent = "Elemento soltado correctamente.";
  }
});
