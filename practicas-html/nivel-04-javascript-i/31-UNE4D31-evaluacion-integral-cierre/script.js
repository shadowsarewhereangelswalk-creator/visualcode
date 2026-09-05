const questions = [
  {text:"¿Qué palabra permite reasignar una variable?", options:["const","let","return"], answer:1, explanation:"let permite actualizar el valor de una variable."},
  {text:"¿Qué operador exige igualdad de valor y tipo?", options:["=","==","==="], answer:2, explanation:"=== compara valor y tipo sin conversión implícita."},
  {text:"¿Qué estructura selecciona entre varias condiciones?", options:["if, else if y else","for","push"], answer:0, explanation:"if, else if y else ejecutan una rama según las condiciones."},
  {text:"¿Qué ciclo es apropiado para un número conocido de repeticiones?", options:["prompt","for","const"], answer:1, explanation:"for reúne inicio, condición y actualización."},
  {text:"¿Qué ciclo se ejecuta al menos una vez?", options:["while","for","do-while"], answer:2, explanation:"do-while evalúa la condición después de ejecutar."},
  {text:"¿Qué método agrega un elemento al final de un arreglo?", options:["push","pop","splice"], answer:0, explanation:"push añade uno o más elementos al final."},
  {text:"¿Qué palabra entrega un resultado desde una función?", options:["alert","return","querySelector"], answer:1, explanation:"return devuelve el resultado de la función."},
  {text:"¿Qué método selecciona el primer elemento que coincide con un selector CSS?", options:["console.log","Number","querySelector"], answer:2, explanation:"document.querySelector devuelve el primer elemento coincidente."}
];
const form = document.querySelector("#quiz-form");
const questionsContainer = document.querySelector("#questions");
const scoreOutput = document.querySelector("#score");
const resultSection = document.querySelector("#evaluation-result");
const resultTitle = document.querySelector("#result-title");
const resultMessage = document.querySelector("#result-message");
const resultProgress = document.querySelector("#result-progress");
const corrections = document.querySelector("#corrections");
const resetButton = document.querySelector("#reset-quiz");

function renderQuestions() {
  questionsContainer.replaceChildren();
  questions.forEach((question, questionIndex) => {
    const fieldset = document.createElement("fieldset");
    const legend = document.createElement("legend");
    const options = document.createElement("div");
    fieldset.className = "question";
    fieldset.dataset.index = String(questionIndex);
    legend.textContent = questionIndex + 1 + ". " + question.text;
    options.className = "options";
    question.options.forEach((option, optionIndex) => {
      const label = document.createElement("label");
      const input = document.createElement("input");
      input.type = "radio";
      input.name = "question-" + questionIndex;
      input.value = String(optionIndex);
      input.required = true;
      label.append(input, option);
      options.append(label);
    });
    fieldset.append(legend, options);
    questionsContainer.append(fieldset);
  });
}

form.addEventListener("submit", event => {
  event.preventDefault();
  let score = 0;
  corrections.replaceChildren();
  questions.forEach((question, index) => {
    const selected = form.elements["question-" + index].value;
    const correct = Number(selected) === question.answer;
    const fieldset = questionsContainer.querySelector('[data-index="' + index + '"]');
    fieldset.className = "question " + (correct ? "correct" : "incorrect");
    if (correct) {
      score += 1;
    } else {
      const item = document.createElement("li");
      item.textContent = "Pregunta " + (index + 1) + ": " + question.explanation;
      corrections.append(item);
    }
  });
  const percentage = score / questions.length * 100;
  scoreOutput.textContent = String(score);
  resultTitle.textContent = score === questions.length ? "Nivel dominado" : score >= 6 ? "Buen resultado" : "Continúa practicando";
  resultMessage.textContent = "Obtuviste " + score + " de " + questions.length + " respuestas correctas.";
  resultProgress.style.width = percentage + "%";
  resultSection.hidden = false;
  resultSection.scrollIntoView({behavior:"smooth"});
});

resetButton.addEventListener("click", () => {
  form.reset();
  scoreOutput.textContent = "0";
  resultSection.hidden = true;
  document.querySelectorAll(".question").forEach(question => question.className = "question");
  window.scrollTo({top:0, behavior:"smooth"});
});

renderQuestions();
