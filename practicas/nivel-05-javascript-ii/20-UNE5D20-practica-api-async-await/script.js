const apiUrl = "https://jsonplaceholder.typicode.com/users";
const loadButton = document.querySelector("#load-users");
const retryButton = document.querySelector("#retry-users");
const searchInput = document.querySelector("#user-search");
const statusOutput = document.querySelector("#api-status");
const grid = document.querySelector("#user-grid");
let users = [];

function renderUsers() {
  const query = searchInput.value.trim().toLowerCase();
  const filtered = users.filter(user => user.name.toLowerCase().includes(query) || user.address.city.toLowerCase().includes(query));
  grid.replaceChildren();
  filtered.forEach(user => {
    const card = document.createElement("article");
    card.className = "user-card";
    const title = document.createElement("h3");
    const company = document.createElement("strong");
    const city = document.createElement("p");
    const email = document.createElement("a");
    title.textContent = user.name;
    company.textContent = user.company.name;
    city.textContent = user.address.city;
    email.href = "mailto:" + user.email;
    email.textContent = user.email;
    card.append(title, company, city, email);
    grid.append(card);
  });
  statusOutput.textContent = filtered.length + " usuarios visibles de " + users.length + ".";
}

async function loadUsers() {
  loadButton.disabled = true;
  retryButton.hidden = true;
  searchInput.disabled = true;
  statusOutput.textContent = "Consultando la API...";
  grid.replaceChildren();
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) throw new Error("Respuesta HTTP " + response.status);
    users = await response.json();
    searchInput.disabled = false;
    renderUsers();
  } catch (error) {
    statusOutput.textContent = "No fue posible cargar los usuarios: " + error.message;
    retryButton.hidden = false;
  } finally {
    loadButton.disabled = false;
  }
}

loadButton.addEventListener("click", loadUsers);
retryButton.addEventListener("click", loadUsers);
searchInput.addEventListener("input", renderUsers);
