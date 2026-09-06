const form = document.querySelector("#cards-form");
const countInput = document.querySelector("#card-count");
const grid = document.querySelector("#generated-cards");
const totalOutput = document.querySelector("#total-cards");
const evenOutput = document.querySelector("#even-cards");
const sumOutput = document.querySelector("#card-sum");

function generateCards() {
  const count = Number(countInput.value);
  let evenCount = 0;
  let sum = 0;
  grid.replaceChildren();
  for (let number = 1; number <= count; number += 1) {
    const card = document.createElement("article");
    card.className = "generated-card";
    card.textContent = String(number);
    if (number % 2 === 0) {
      card.classList.add("even");
      evenCount += 1;
    }
    sum += number;
    grid.append(card);
  }
  totalOutput.textContent = String(count);
  evenOutput.textContent = String(evenCount);
  sumOutput.textContent = String(sum);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  generateCards();
});

generateCards();
