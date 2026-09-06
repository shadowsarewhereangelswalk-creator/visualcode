const storageKey = "une5-persistent-notes";
const form = document.querySelector("#note-form");
const titleInput = document.querySelector("#note-title");
const categorySelect = document.querySelector("#note-category");
const contentInput = document.querySelector("#note-content");
const searchInput = document.querySelector("#note-search");
const pinnedInput = document.querySelector("#pinned-only");
const clearButton = document.querySelector("#clear-notes");
const grid = document.querySelector("#notes-grid");
const countOutput = document.querySelector("#notes-count");
const statusOutput = document.querySelector("#notes-status");
const emptyOutput = document.querySelector("#empty-notes");
let notes = [];

function loadNotes() {
  try {
    const saved = localStorage.getItem(storageKey);
    notes = saved ? JSON.parse(saved) : [];
    statusOutput.textContent = saved ? "Notas recuperadas desde LocalStorage." : "Aún no hay datos guardados.";
  } catch (error) {
    notes = [];
    statusOutput.textContent = "No fue posible leer LocalStorage: " + error.message;
  }
}

function saveNotes(message) {
  try {
    localStorage.setItem(storageKey, JSON.stringify(notes));
    statusOutput.textContent = message;
  } catch (error) {
    statusOutput.textContent = "No fue posible guardar: " + error.message;
  }
}

function filteredNotes() {
  const query = searchInput.value.trim().toLowerCase();
  return notes.filter(note => {
    const matchesText = note.title.toLowerCase().includes(query) || note.content.toLowerCase().includes(query);
    const matchesPinned = !pinnedInput.checked || note.pinned;
    return matchesText && matchesPinned;
  });
}

function renderNotes() {
  const visible = filteredNotes();
  grid.replaceChildren();
  visible.forEach(note => {
    const card = document.createElement("article");
    const category = document.createElement("span");
    const title = document.createElement("h3");
    const content = document.createElement("p");
    const actions = document.createElement("div");
    const pin = document.createElement("button");
    const remove = document.createElement("button");
    card.className = "note-card" + (note.pinned ? " pinned" : "");
    category.className = "category";
    category.textContent = note.category;
    title.textContent = note.title;
    content.textContent = note.content;
    actions.className = "note-actions";
    pin.type = "button";
    pin.textContent = note.pinned ? "Desfijar" : "Fijar";
    remove.type = "button";
    remove.className = "delete-note";
    remove.textContent = "Eliminar";
    pin.addEventListener("click", () => {
      note.pinned = !note.pinned;
      saveNotes(note.pinned ? "Nota fijada." : "Nota desfijada.");
      renderNotes();
    });
    remove.addEventListener("click", () => {
      notes = notes.filter(item => item.id !== note.id);
      saveNotes("Nota eliminada.");
      renderNotes();
    });
    actions.append(pin, remove);
    card.append(category, title, content, actions);
    grid.append(card);
  });
  countOutput.textContent = notes.length + (notes.length === 1 ? " nota" : " notas");
  emptyOutput.hidden = visible.length !== 0;
}

form.addEventListener("submit", event => {
  event.preventDefault();
  notes.unshift({
    id:Date.now(),
    title:titleInput.value.trim(),
    category:categorySelect.value,
    content:contentInput.value.trim(),
    pinned:false
  });
  saveNotes("Nota guardada en LocalStorage.");
  form.reset();
  renderNotes();
});

searchInput.addEventListener("input", renderNotes);
pinnedInput.addEventListener("change", renderNotes);
clearButton.addEventListener("click", () => {
  const accepted = window.confirm("¿Deseas eliminar todas las notas guardadas?");
  if (!accepted) return;
  notes = [];
  saveNotes("Todas las notas fueron eliminadas.");
  renderNotes();
});

loadNotes();
renderNotes();
