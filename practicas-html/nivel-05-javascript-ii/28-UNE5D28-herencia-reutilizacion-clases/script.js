class Vehicle {
  constructor(brand, model) {
    this.brand = brand;
    this.model = model;
  }

  getName() {
    return this.brand + " " + this.model;
  }

  describe() {
    return "Vehículo de propósito general";
  }
}

class ElectricVehicle extends Vehicle {
  constructor(brand, model, range) {
    super(brand, model);
    this.range = range;
  }

  describe() {
    return "Autonomía eléctrica: " + this.range + " km";
  }
}

class CargoVehicle extends Vehicle {
  constructor(brand, model, capacity) {
    super(brand, model);
    this.capacity = capacity;
  }

  describe() {
    return "Capacidad de carga: " + this.capacity + " kg";
  }
}

const vehicles = [
  new ElectricVehicle("Nexo", "E1", 410),
  new CargoVehicle("Rumbo", "Cargo", 950)
];
const form = document.querySelector("#vehicle-form");
const brandInput = document.querySelector("#vehicle-brand");
const modelInput = document.querySelector("#vehicle-model");
const typeSelect = document.querySelector("#vehicle-type");
const extraInput = document.querySelector("#vehicle-extra");
const grid = document.querySelector("#vehicle-grid");

function renderVehicles() {
  grid.replaceChildren();
  vehicles.forEach(vehicle => {
    const card = document.createElement("article");
    const type = document.createElement("span");
    const name = document.createElement("h3");
    const description = document.createElement("p");
    card.className = "vehicle-card";
    type.textContent = vehicle.constructor.name;
    name.textContent = vehicle.getName();
    description.textContent = vehicle.describe();
    card.append(type, name, description);
    grid.append(card);
  });
}

form.addEventListener("submit", event => {
  event.preventDefault();
  const VehicleClass = typeSelect.value === "electric" ? ElectricVehicle : CargoVehicle;
  vehicles.push(new VehicleClass(
    brandInput.value.trim(),
    modelInput.value.trim(),
    Number(extraInput.value)
  ));
  renderVehicles();
});

typeSelect.addEventListener("change", () => {
  extraInput.value = typeSelect.value === "electric" ? "320" : "800";
});

renderVehicles();
