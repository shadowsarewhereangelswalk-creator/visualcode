const tasks = [
  {id:1, name:"Repasar variables", priority:"alta", completed:true},
  {id:2, name:"Practicar ciclos", priority:"media", completed:false},
  {id:3, name:"Construir la interfaz", priority:"alta", completed:false}
];
const form = document.querySelector("#task-form");
const taskInput = document.querySelector("#task-input");
const prioritySelect = document.querySelector("#priority");
const list = document.querySelector("#task-list");
const pendingCount = document.querySelector("#pending-count");
const totalCount = document.querySelector("#total-count");
const emptyState = document.querySelector("#empty-state");
const filters = document.querySelectorAll("[data-filter]");
const clearButton = document.querySelector("#clear-completed");
let activeFilter = "all";
let nextId = 4;

function visibleTasks() {
  if (activeFilter === "pending") return tasks.filter(task => !task.completed);
  if (activeFilter === "completed") return tasks.filter(task => task.completed);
  return tasks;
}

function renderTasks() {
  list.replaceChildren();
  const selectedTasks = visibleTasks();
  selectedTasks.forEach(task => {
    const item = document.createElement("li");
    const toggle = document.createElement("button");
    const info = document.createElement("div");
    const name = document.createElement("strong");
    const priority = document.createElement("span");
    const remove = document.createElement("button");
    item.className = "task-item" + (task.completed ? " completed" : "");
    toggle.className = "task-toggle";
    toggle.type = "button";
    toggle.textContent = task.completed ? "↺" : "✓";
    toggle.setAttribute("aria-label", task.completed ? "Marcar como pendiente" : "Marcar como completada");
    name.className = "task-name";
    name.textContent = task.name;
    priority.className = "task-priority";
    priority.textContent = "Prioridad " + task.priority;
    remove.className = "task-delete";
    remove.type = "button";
    remove.textContent = "Eliminar";
    toggle.addEventListener("click", () => {
      task.completed = !task.completed;
      renderTasks();
    });
    remove.addEventListener("click", () => {
      const index = tasks.findIndex(itemTask => itemTask.id === task.id);
      tasks.splice(index, 1);
      renderTasks();
    });
    info.append(name, priority);
    item.append(toggle, info, remove);
    list.append(item);
  });
  const pending = tasks.filter(task => !task.completed).length;
  pendingCount.textContent = String(pending);
  totalCount.textContent = tasks.length + (tasks.length === 1 ? " tarea" : " tareas");
  emptyState.hidden = selectedTasks.length !== 0;
}

form.addEventListener("submit", event => {
  event.preventDefault();
  tasks.push({
    id:nextId,
    name:taskInput.value.trim(),
    priority:prioritySelect.value,
    completed:false
  });
  nextId += 1;
  form.reset();
  activeFilter = "all";
  filters.forEach(button => button.setAttribute("aria-pressed", String(button.dataset.filter === "all")));
  renderTasks();
});

filters.forEach(button => {
  button.addEventListener("click", () => {
    activeFilter = button.dataset.filter;
    filters.forEach(filter => filter.setAttribute("aria-pressed", String(filter === button)));
    renderTasks();
  });
});

clearButton.addEventListener("click", () => {
  for (let index = tasks.length - 1; index >= 0; index -= 1) {
    if (tasks[index].completed) tasks.splice(index, 1);
  }
  renderTasks();
});

renderTasks();
