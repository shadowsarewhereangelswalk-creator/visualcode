const passwordInput = document.querySelector("#password");
const toggleButton = document.querySelector("#toggle-password");
const meter = document.querySelector("#strength-meter");
const title = document.querySelector("#strength-title");
const card = document.querySelector("#strength-card");
const lengthRule = document.querySelector("#length-rule");
const numberRule = document.querySelector("#number-rule");
const uppercaseRule = document.querySelector("#uppercase-rule");

function evaluatePassword() {
  const password = passwordInput.value;
  const longEnough = password.length >= 8;
  const hasNumber = /[0-9]/.test(password);
  const hasUppercase = /[A-ZÁÉÍÓÚÑ]/.test(password);
  const score = Number(longEnough) + Number(hasNumber) + Number(hasUppercase);
  const label = score === 3 ? "Fortaleza alta" : score === 2 ? "Fortaleza media" : "Fortaleza baja";
  const color = score === 3 ? "#16a34a" : score === 2 ? "#f59e0b" : "#dc2626";
  const background = score === 3 ? "#f0fdf4" : score === 2 ? "#fffbeb" : "#fef2f2";
  title.textContent = label;
  meter.style.width = score / 3 * 100 + "%";
  meter.style.backgroundColor = color;
  card.style.backgroundColor = background;
  lengthRule.classList.toggle("passed", longEnough);
  numberRule.classList.toggle("passed", hasNumber);
  uppercaseRule.classList.toggle("passed", hasUppercase);
}

toggleButton.addEventListener("click", () => {
  const hidden = passwordInput.type === "password";
  passwordInput.type = hidden ? "text" : "password";
  toggleButton.textContent = hidden ? "Ocultar" : "Mostrar";
});

passwordInput.addEventListener("input", evaluatePassword);
evaluatePassword();
