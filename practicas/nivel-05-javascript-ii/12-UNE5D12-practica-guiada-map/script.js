const students = [
  {name:"Ana", score:92},
  {name:"Luis", score:68},
  {name:"Marta", score:84},
  {name:"Carlos", score:74}
];
const grid = document.querySelector("#student-grid");
const summary = document.querySelector("#map-summary");
const generateButton = document.querySelector("#generate-report");
const bonusButton = document.querySelector("#add-bonus");
let bonus = 0;

const letterFor = score => score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : score >= 60 ? "D" : "F";

function generateReport() {
  const report = students.map(student => {
    const finalScore = Math.min(student.score + bonus, 100);
    return {
      ...student,
      finalScore,
      letter:letterFor(finalScore),
      passed:finalScore >= 70
    };
  });
  grid.replaceChildren();
  report.forEach(student => {
    const card = document.createElement("article");
    card.className = "student-card";
    card.innerHTML = "<h3>" + student.name + "</h3><strong>" + student.finalScore + "</strong><p>Letra " + student.letter + "</p><span class=\"" + (student.passed ? "passed" : "failed") + "\">" + (student.passed ? "Aprobado" : "Debe reforzar") + "</span>";
    grid.append(card);
  });
  summary.textContent = JSON.stringify(report);
}

generateButton.addEventListener("click", generateReport);
bonusButton.addEventListener("click", () => {
  bonus = bonus === 0 ? 5 : 0;
  bonusButton.textContent = bonus === 0 ? "Aplicar 5 puntos extra" : "Quitar puntos extra";
  generateReport();
});
generateReport();
