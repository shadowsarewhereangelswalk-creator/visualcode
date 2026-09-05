const storageKey = "une5-preferences";
const defaults = {name:"Karen", theme:"light", accent:"#2563eb"};
const form = document.querySelector("#settings-form");
const nameInput = document.querySelector("#saved-name");
const themeSelect = document.querySelector("#saved-theme");
const accentInput = document.querySelector("#saved-accent");
const clearButton = document.querySelector("#clear-settings");
const preview = document.querySelector("#settings-preview");
const initialOutput = document.querySelector("#saved-initial");
const greetingOutput = document.querySelector("#saved-greeting");
const storagePreview = document.querySelector("#storage-preview");
const statusOutput = document.querySelector("#storage-status");

function readPreferences() {
  try {
    const saved = localStorage.getItem(storageKey);
    return saved ? JSON.parse(saved) : defaults;
  } catch (error) {
    statusOutput.textContent = "El navegador no permitió leer LocalStorage: " + error.message;
    return defaults;
  }
}

function renderPreferences(preferences) {
  nameInput.value = preferences.name;
  themeSelect.value = preferences.theme;
  accentInput.value = preferences.accent;
  preview.className = "settings-preview " + preferences.theme;
  preview.style.setProperty("--accent", preferences.accent);
  initialOutput.textContent = preferences.name.charAt(0).toUpperCase();
  greetingOutput.textContent = "Hola, " + preferences.name;
  storagePreview.textContent = JSON.stringify(preferences);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  const preferences = {
    name:nameInput.value.trim(),
    theme:themeSelect.value,
    accent:accentInput.value
  };
  try {
    localStorage.setItem(storageKey, JSON.stringify(preferences));
    renderPreferences(preferences);
    statusOutput.textContent = "Preferencias guardadas. Puedes recargar la página.";
  } catch (error) {
    statusOutput.textContent = "No fue posible guardar: " + error.message;
  }
});

clearButton.addEventListener("click", () => {
  try {
    localStorage.removeItem(storageKey);
    renderPreferences(defaults);
    statusOutput.textContent = "Las preferencias guardadas fueron eliminadas.";
  } catch (error) {
    statusOutput.textContent = "No fue posible borrar los datos: " + error.message;
  }
});

renderPreferences(readPreferences());
