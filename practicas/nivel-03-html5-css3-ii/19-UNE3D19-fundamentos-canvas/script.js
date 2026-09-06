const canvas = document.querySelector("#scene");
const context = canvas.getContext("2d");

context.fillStyle = "#eff6ff";
context.fillRect(0, 0, canvas.width, canvas.height);

context.fillStyle = "#1d4ed8";
context.fillRect(70, 70, 230, 140);

context.strokeStyle = "#0f2f57";
context.lineWidth = 8;
context.strokeRect(90, 90, 230, 140);

context.beginPath();
context.arc(500, 150, 78, 0, Math.PI * 2);
context.fillStyle = "#f97316";
context.fill();

context.beginPath();
context.moveTo(80, 360);
context.lineTo(380, 280);
context.lineTo(620, 370);
context.lineTo(830, 250);
context.strokeStyle = "#16a34a";
context.lineWidth = 12;
context.lineCap = "round";
context.lineJoin = "round";
context.stroke();

context.fillStyle = "#172554";
context.font = "700 38px Arial";
context.textAlign = "center";
context.fillText("Canvas 2D", 680, 120);

context.font = "24px Arial";
context.fillText("Formas creadas con JavaScript", 680, 165);
