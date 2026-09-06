const canvas = document.querySelector("#board");
const context = canvas.getContext("2d");
const color = document.querySelector("#color");
const size = document.querySelector("#size");
const clearButton = document.querySelector("#clear");
const status = document.querySelector("#canvas-status");
let drawing = false;

function pointFromEvent(event) {
  const bounds = canvas.getBoundingClientRect();
  return {
    x: (event.clientX - bounds.left) * (canvas.width / bounds.width),
    y: (event.clientY - bounds.top) * (canvas.height / bounds.height)
  };
}

function startDrawing(event) {
  drawing = true;
  const point = pointFromEvent(event);
  context.beginPath();
  context.moveTo(point.x, point.y);
  canvas.setPointerCapture(event.pointerId);
  status.textContent = "Dibujando en el lienzo.";
}

function draw(event) {
  if (!drawing) {
    return;
  }
  const point = pointFromEvent(event);
  context.lineWidth = Number(size.value);
  context.lineCap = "round";
  context.lineJoin = "round";
  context.strokeStyle = color.value;
  context.lineTo(point.x, point.y);
  context.stroke();
}

function stopDrawing() {
  if (!drawing) {
    return;
  }
  drawing = false;
  context.closePath();
  status.textContent = "Trazo terminado.";
}

canvas.addEventListener("pointerdown", startDrawing);
canvas.addEventListener("pointermove", draw);
canvas.addEventListener("pointerup", stopDrawing);
canvas.addEventListener("pointercancel", stopDrawing);
clearButton.addEventListener("click", () => {
  context.clearRect(0, 0, canvas.width, canvas.height);
  status.textContent = "El lienzo quedó limpio.";
});
