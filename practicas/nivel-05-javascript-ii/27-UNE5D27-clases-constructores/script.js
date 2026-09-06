class Course {
  constructor(name, hours, price) {
    this.name = name;
    this.hours = hours;
    this.price = price;
    this.completed = false;
  }

  getPrice() {
    return new Intl.NumberFormat("es-US", {style:"currency", currency:"USD"}).format(this.price);
  }

  getSummary() {
    return this.hours + " horas · " + (this.completed ? "Completado" : "Disponible");
  }
}

const courses = [
  new Course("Funciones avanzadas", 10, 35),
  new Course("Asincronía", 14, 52)
];
const form = document.querySelector("#course-form");
const nameInput = document.querySelector("#course-name");
const hoursInput = document.querySelector("#course-hours");
const priceInput = document.querySelector("#course-price");
const grid = document.querySelector("#course-grid");
const countOutput = document.querySelector("#instance-count");

function renderCourses() {
  grid.replaceChildren();
  courses.forEach(course => {
    const card = document.createElement("article");
    const title = document.createElement("h3");
    const summary = document.createElement("p");
    const price = document.createElement("strong");
    card.className = "course-card";
    title.textContent = course.name;
    summary.textContent = course.getSummary();
    price.textContent = course.getPrice();
    card.append(title, summary, price);
    grid.append(card);
  });
  countOutput.textContent = courses.length + " instancias creadas";
}

form.addEventListener("submit", event => {
  event.preventDefault();
  courses.push(new Course(nameInput.value.trim(), Number(hoursInput.value), Number(priceInput.value)));
  form.reset();
  hoursInput.value = "12";
  priceInput.value = "45";
  renderCourses();
});

renderCourses();
