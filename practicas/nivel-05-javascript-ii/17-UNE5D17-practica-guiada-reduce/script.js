const transactions = [
  {description:"Proyecto web", category:"Ingresos", amount:650},
  {description:"Suscripción", category:"Herramientas", amount:-24},
  {description:"Curso", category:"Formación", amount:-80},
  {description:"Consultoría", category:"Ingresos", amount:300},
  {description:"Internet", category:"Servicios", amount:-45},
  {description:"Plantilla", category:"Herramientas", amount:-18}
];
const currency = new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"});
const list = document.querySelector("#transaction-list");
const incomeOutput = document.querySelector("#income-total");
const expenseOutput = document.querySelector("#expense-total");
const balanceOutput = document.querySelector("#balance-total");
const categoryOutput = document.querySelector("#category-summary");
const summarizeButton = document.querySelector("#summarize");
const groupButton = document.querySelector("#group");

function renderTransactions() {
  transactions.forEach(transaction => {
    const row = document.createElement("article");
    const description = document.createElement("strong");
    const category = document.createElement("span");
    const amount = document.createElement("strong");
    row.className = "transaction";
    description.textContent = transaction.description;
    category.textContent = transaction.category;
    amount.className = transaction.amount >= 0 ? "income" : "expense";
    amount.textContent = currency.format(transaction.amount);
    row.append(description, category, amount);
    list.append(row);
  });
}

function renderTotals() {
  const totals = transactions.reduce((summary, transaction) => {
    if (transaction.amount >= 0) summary.income += transaction.amount;
    else summary.expenses += Math.abs(transaction.amount);
    summary.balance += transaction.amount;
    return summary;
  }, {income:0, expenses:0, balance:0});
  incomeOutput.textContent = currency.format(totals.income);
  expenseOutput.textContent = currency.format(totals.expenses);
  balanceOutput.textContent = currency.format(totals.balance);
}

function renderCategories() {
  const categories = transactions.reduce((summary, transaction) => {
    summary[transaction.category] = (summary[transaction.category] || 0) + transaction.amount;
    return summary;
  }, {});
  categoryOutput.replaceChildren();
  Object.entries(categories).forEach(([category, total]) => {
    const card = document.createElement("article");
    const name = document.createElement("span");
    const amount = document.createElement("strong");
    name.textContent = category;
    amount.textContent = currency.format(total);
    card.append(name, amount);
    categoryOutput.append(card);
  });
}

summarizeButton.addEventListener("click", renderTotals);
groupButton.addEventListener("click", renderCategories);
renderTransactions();
renderTotals();
renderCategories();
