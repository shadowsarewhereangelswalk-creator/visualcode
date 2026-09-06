const students = [
  {name:"Ana", score:92},
  {name:"Luis", score:78},
  {name:"Marta", score:86}
];
const form = document.querySelector("#score-form");
const studentInput = document.querySelector("#student");
const scoreInput = document.querySelector("#student-score");
const list = document.querySelector("#score-list");
const countOutput = document.querySelector("#student-count");
const averageOutput = document.querySelector("#average-score");
const highestOutput = document.querySelector("#highest-score");

function renderScores() {
  list.replaceChildren();
  let total = 0;
  let highest = 0;
  for (let index = 0; index < students.length; index += 1) {
    const student = students[index];
    total += student.score;
    if (student.score > highest) highest = student.score;
    const row = document.createElement("article");
    row.className = "score-row";
    const position = document.createElement("span");
    const name = document.createElement("span");
    const score = document.createElement("strong");
    position.className = "index";
    position.textContent = String(index);
    name.textContent = student.name;
    score.textContent = student.score + "/100";
    row.append(position, name, score);
    list.append(row);
  }
  const average = students.length === 0 ? 0 : total / students.length;
  countOutput.textContent = String(students.length);
  averageOutput.textContent = average.toFixed(1);
  highestOutput.textContent = String(highest);
}

form.addEventListener("submit", event => {
  event.preventDefault();
  students.push({name:studentInput.value.trim(), score:Number(scoreInput.value)});
  form.reset();
  scoreInput.value = "80";
  renderScores();
});

renderScores();
