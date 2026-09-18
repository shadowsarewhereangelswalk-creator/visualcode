const dibujo = document.getElementById("lienzo");
const ctx = dibujo.getContext("2d");

const colores = [
  "Yellow",
  "Blue",
  "Red",
  "Orange",
  "Purple",
  "Green",
  "Pink"
];

colores.sort();

let x = 0;
let y = 0;

for (let i = 0; i < colores.length; i += 1) {
  ctx.fillStyle = colores[i];
  ctx.fillRect(x, y, 100, 100);
  x += 100;
  y += 100;
}
