class Person {
  constructor(name, email) {
    this.name = name;
    this.email = email;
    this.createdAt = new Date().toLocaleDateString();
  }

  getContact() {
    return this.name + " · " + this.email;
  }
}

class Student extends Person {
  constructor(name, email, track) {
    super(name, email);
    this.track = track;
    this.role = "Estudiante";
  }

  getDescription() {
    return "Estudia la ruta de " + this.track + ".";
  }
}

class Mentor extends Person {
  constructor(name, email, specialty) {
    super(name, email);
    this.specialty = specialty;
    this.role = "Mentor";
  }

  getDescription() {
    return "Acompaña proyectos de " + this.specialty + ".";
  }
}

const members = [
  new Student("Ana Torres", "ana@example.com", "Frontend"),
  new Mentor("Luis Pérez", "luis@example.com", "JavaScript")
];
const form = document.querySelector("#member-form");
const nameInput = document.querySelector("#member-name");
const emailInput = document.querySelector("#member-email");
const roleSelect = document.querySelector("#member-role");
const areaInput = document.querySelector("#member-area");
const grid = document.querySelector("#member-grid");

function renderMembers() {
  grid.replaceChildren();
  members.forEach(member => {
    const card = document.createElement("article");
    card.className = "member-card " + (member instanceof Student ? "student" : "mentor");
    const role = document.createElement("span");
    const name = document.createElement("h3");
    const description = document.createElement("p");
    const contact = document.createElement("small");
    role.className = "pill";
    role.textContent = member.role;
    name.textContent = member.name;
    description.textContent = member.getDescription();
    contact.textContent = member.getContact();
    card.append(role, name, description, contact);
    grid.append(card);
  });
}

form.addEventListener("submit", event => {
  event.preventDefault();
  const MemberClass = roleSelect.value === "student" ? Student : Mentor;
  members.push(new MemberClass(nameInput.value.trim(), emailInput.value.trim(), areaInput.value.trim()));
  form.reset();
  areaInput.value = "JavaScript";
  renderMembers();
});

renderMembers();
