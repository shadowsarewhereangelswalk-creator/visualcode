const resources = [
  {name:"Introducción a map", type:"video", tags:["arreglos","map"], free:true},
  {name:"Guía de callbacks", type:"guia", tags:["funciones","callbacks"], free:true},
  {name:"Dashboard con API", type:"proyecto", tags:["api","async"], free:false},
  {name:"Promesas paso a paso", type:"video", tags:["promesas","asincronía"], free:true},
  {name:"Aplicación persistente", type:"proyecto", tags:["dom","localstorage"], free:false},
  {name:"Referencia de objetos", type:"guia", tags:["objetos","clases"], free:true}
];
const searchInput = document.querySelector("#resource-search");
const typeSelect = document.querySelector("#resource-type");
const freeInput = document.querySelector("#free-only");
const grid = document.querySelector("#resource-grid");
const countOutput = document.querySelector("#resource-count");

function filterResources() {
  const query = searchInput.value.trim().toLowerCase();
  const type = typeSelect.value;
  const freeOnly = freeInput.checked;
  const filtered = resources.filter(resource => {
    const matchesText = resource.name.toLowerCase().includes(query) || resource.tags.some(tag => tag.includes(query));
    const matchesType = type === "all" || resource.type === type;
    const matchesPrice = !freeOnly || resource.free;
    return matchesText && matchesType && matchesPrice;
  });
  grid.replaceChildren();
  filtered.forEach(resource => {
    const card = document.createElement("article");
    card.className = "resource-card";
    card.innerHTML = "<span>" + resource.type + "</span><h3>" + resource.name + "</h3><p>" + resource.tags.join(" · ") + "</p><strong>" + (resource.free ? "Gratuito" : "Premium") + "</strong>";
    grid.append(card);
  });
  countOutput.textContent = filtered.length + (filtered.length === 1 ? " recurso encontrado" : " recursos encontrados");
}

searchInput.addEventListener("input", filterResources);
typeSelect.addEventListener("change", filterResources);
freeInput.addEventListener("change", filterResources);
filterResources();
