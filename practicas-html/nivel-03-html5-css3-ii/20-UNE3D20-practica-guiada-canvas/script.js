const canvas = document.querySelector("#landscape");
const context = canvas.getContext("2d");
const redraw = document.querySelector("#redraw");

function drawLandscape() {
  const sky = context.createLinearGradient(0, 0, 0, canvas.height);
  sky.addColorStop(0, "#60a5fa");
  sky.addColorStop(0.68, "#dbeafe");
  sky.addColorStop(1, "#fef3c7");
  context.fillStyle = sky;
  context.fillRect(0, 0, canvas.width, canvas.height);

  context.beginPath();
  context.arc(820, 105, 58, 0, Math.PI * 2);
  context.fillStyle = "#fde047";
  context.shadowColor = "rgba(253, 224, 71, 0.7)";
  context.shadowBlur = 28;
  context.fill();
  context.shadowBlur = 0;

  context.beginPath();
  context.moveTo(0, 390);
  context.lineTo(210, 190);
  context.lineTo(390, 390);
  context.lineTo(585, 150);
  context.lineTo(820, 390);
  context.lineTo(1000, 230);
  context.lineTo(1000, 560);
  context.lineTo(0, 560);
  context.closePath();
  context.fillStyle = "#475569";
  context.fill();

  context.beginPath();
  context.moveTo(120, 560);
  context.quadraticCurveTo(430, 350, 1000, 470);
  context.lineTo(1000, 560);
  context.closePath();
  context.fillStyle = "#16a34a";
  context.fill();

  context.fillStyle = "#92400e";
  context.fillRect(160, 390, 28, 110);
  context.beginPath();
  context.arc(174, 360, 72, 0, Math.PI * 2);
  context.fillStyle = "#15803d";
  context.fill();

  context.fillStyle = "rgba(15, 23, 42, 0.78)";
  context.fillRect(45, 45, 360, 82);
  context.fillStyle = "#ffffff";
  context.font = "700 34px Arial";
  context.fillText("Paisaje Canvas", 75, 96);
}

redraw.addEventListener("click", drawLandscape);
drawLandscape();
