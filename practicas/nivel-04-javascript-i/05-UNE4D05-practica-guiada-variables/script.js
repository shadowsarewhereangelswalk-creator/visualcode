const programName = "AI Career";
const form = document.querySelector("#profile-form");
const nameInput = document.querySelector("#name");
const roleInput = document.querySelector("#role");
const goalInput = document.querySelector("#goal");
const nameOutput = document.querySelector("#profile-name");
const roleOutput = document.querySelector("#profile-role");
const goalOutput = document.querySelector("#profile-goal");
const initialsOutput = document.querySelector("#initials");
const revisionOutput = document.querySelector("#revision");
const programOutput = document.querySelector("#program");
let revision = 0;

programOutput.textContent = programName;

form.addEventListener("submit", event => {
  event.preventDefault();
  let name = nameInput.value.trim();
  let role = roleInput.value.trim();
  let goal = goalInput.value.trim();
  revision += 1;
  nameOutput.textContent = name;
  roleOutput.textContent = role;
  goalOutput.textContent = goal;
  initialsOutput.textContent = name.charAt(0).toUpperCase();
  revisionOutput.textContent = "Versión " + revision;
});
