const form = document.querySelector("#loop-form");
const limitInput = document.querySelector("#loop-limit");
const whileResult = document.querySelector("#while-result");
const doResult = document.querySelector("#do-result");
const whileCount = document.querySelector("#while-count");
const doCount = document.querySelector("#do-count");

function appendNumber(container, number) {
  const badge = document.createElement("span");
  badge.textContent = String(number);
  container.append(badge);
}

function compareLoops() {
  const limit = Number(limitInput.value);
  whileResult.replaceChildren();
  doResult.replaceChildren();
  let whileIndex = 0;
  let whileRuns = 0;
  while (whileIndex < limit) {
    whileIndex += 1;
    whileRuns += 1;
    appendNumber(whileResult, whileIndex);
  }
  let doIndex = 0;
  let doRuns = 0;
  do {
    doIndex += 1;
    doRuns += 1;
    appendNumber(doResult, doIndex);
  } while (doIndex < limit);
  whileCount.textContent = "Ejecuciones: " + whileRuns;
  doCount.textContent = "Ejecuciones: " + doRuns;
}

form.addEventListener("submit", event => {
  event.preventDefault();
  compareLoops();
});

compareLoops();
