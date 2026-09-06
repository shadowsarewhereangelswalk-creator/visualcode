const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const form = document.querySelector("#savings-form");
const initialInput = document.querySelector("#initial");
const targetInput = document.querySelector("#target");
const contributionInput = document.querySelector("#contribution");
const steps = document.querySelector("#savings-steps");
const monthsOutput = document.querySelector("#months");
const balanceOutput = document.querySelector("#final-balance");
const messageOutput = document.querySelector("#loop-message");

function simulateSavings() {
  let balance = Number(initialInput.value);
  const target = Number(targetInput.value);
  const contribution = Number(contributionInput.value);
  let month = 0;
  steps.replaceChildren();
  while (balance < target && month < 1200) {
    month += 1;
    balance += contribution;
    const item = document.createElement("li");
    item.textContent = "Mes " + month + ": " + currency.format(balance);
    steps.append(item);
  }
  monthsOutput.textContent = month + (month === 1 ? " mes" : " meses");
  balanceOutput.textContent = currency.format(balance) + " acumulados";
  messageOutput.textContent = month === 0
    ? "La meta ya estaba alcanzada antes de iniciar el ciclo."
    : "El ciclo terminó cuando el saldo alcanzó la meta.";
}

form.addEventListener("submit", event => {
  event.preventDefault();
  simulateSavings();
});

simulateSavings();
