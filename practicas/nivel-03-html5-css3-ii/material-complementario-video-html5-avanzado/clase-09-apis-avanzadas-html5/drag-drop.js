function allowDrop(event) {
  event.preventDefault();
}

function drag(event) {
  event.dataTransfer.setData("text/plain", event.target.id);
}

function drop(event) {
  event.preventDefault();

  const data = event.dataTransfer.getData("text/plain");
  const element = document.getElementById(data);

  if (element) {
    event.currentTarget.appendChild(element);
  }
}
