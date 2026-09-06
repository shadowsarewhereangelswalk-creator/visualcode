const products = [
  {id:1, name:"JavaScript Inicial", category:"curso", price:80},
  {id:2, name:"CSS Responsive", category:"curso", price:65},
  {id:3, name:"Plantilla Portfolio", category:"recurso", price:28},
  {id:4, name:"Kit de Componentes", category:"recurso", price:45},
  {id:5, name:"JavaScript Avanzado", category:"curso", price:120}
];
const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const form = document.querySelector("#catalog-form");
const categorySelect = document.querySelector("#category");
const maxPriceInput = document.querySelector("#max-price");
const discountInput = document.querySelector("#catalog-discount");
const grid = document.querySelector("#product-grid");
const filteredCount = document.querySelector("#filtered-count");
const mappedCount = document.querySelector("#mapped-count");
const reducedTotal = document.querySelector("#reduced-total");

function processCatalog() {
  const category = categorySelect.value;
  const maximum = Number(maxPriceInput.value);
  const discount = Number(discountInput.value);
  const filtered = products.filter(product => (category === "all" || product.category === category) && product.price <= maximum);
  const discounted = filtered.map(product => ({
    ...product,
    finalPrice:product.price * (1 - discount / 100)
  }));
  const total = discounted.reduce((sum, product) => sum + product.finalPrice, 0);
  grid.replaceChildren();
  discounted.forEach(product => {
    const card = document.createElement("article");
    card.className = "product-card";
    card.innerHTML = "<p class=\"eyebrow\">" + product.category + "</p><h3>" + product.name + "</h3><span class=\"old-price\">" + currency.format(product.price) + "</span><br><span class=\"new-price\">" + currency.format(product.finalPrice) + "</span>";
    grid.append(card);
  });
  filteredCount.textContent = filtered.length + " productos";
  mappedCount.textContent = discounted.length + " precios";
  reducedTotal.textContent = currency.format(total);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  processCatalog();
});

processCatalog();
