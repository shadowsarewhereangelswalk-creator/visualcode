const form = document.querySelector("#grade-form");
const scoreInput = document.querySelector("#score");
const letterOutput = document.querySelector("#grade-letter");
const titleOutput = document.querySelector("#grade-title");
const detailOutput = document.querySelector("#grade-detail");

function evaluateGrade() {
  const score = Number(scoreInput.value);
  let letter;
  let title;
  let detail;
  if (score >= 90) {
    letter = "A";
    title = "Excelente resultado";
    detail = "Dominaste los objetivos de la evaluación.";
  } else if (score >= 80) {
    letter = "B";
    title = "Muy buen trabajo";
    detail = "Cumpliste los objetivos principales.";
  } else if (score >= 70) {
    letter = "C";
    title = "Resultado satisfactorio";
    detail = "Comprendes la base y puedes seguir practicando.";
  } else if (score >= 60) {
    letter = "D";
    title = "Necesitas reforzar";
    detail = "Repasa los temas antes de continuar.";
  } else {
    letter = "F";
    title = "Vuelve a intentarlo";
    detail = "Practica los fundamentos y repite la evaluación.";
  }
  letterOutput.textContent = letter;
  titleOutput.textContent = title;
  detailOutput.textContent = detail;
}

form.addEventListener("submit", event => {
  event.preventDefault();
  evaluateGrade();
});

evaluateGrade();
