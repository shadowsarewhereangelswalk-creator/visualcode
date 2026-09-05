const fruits = ["Manzana", "Banana", "Naranja", "Mango", "Fresa"];
const previousButton = document.querySelector("#previous");
const nextButton = document.querySelector("#next");
const fruitIndex = document.querySelector("#fruit-index");
const fruitName = document.querySelector("#fruit-name");
const arrayItems = document.querySelector("#array-items");
const arrayLength = document.querySelector("#array-length");
const arrayCode = document.querySelector("#array-code");
let currentIndex = 0;

function renderArray() {
  fruitIndex.textContent = "Índice " + currentIndex;
  fruitName.textContent = fruits[currentIndex];
  arrayLength.textContent = String(fruits.length);
  arrayCode.textContent = JSON.stringify(fruits);
  arrayItems.replaceChildren();
  for (let index = 0; index < fruits.length; index += 1) {
    const item = document.createElement("span");
    item.textContent = index + ": " + fruits[index];
    item.classList.toggle("active", index === currentIndex);
    arrayItems.append(item);
  }
}

previousButton.addEventListener("click", () => {
  currentIndex = currentIndex === 0 ? fruits.length - 1 : currentIndex - 1;
  renderArray();
});

nextButton.addEventListener("click", () => {
  currentIndex = currentIndex === fruits.length - 1 ? 0 : currentIndex + 1;
  renderArray();
});

renderArray();
