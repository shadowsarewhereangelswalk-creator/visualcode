const profile = {
  name:"Karen",
  role:"Desarrolladora web",
  level:5,
  active:true
};
const form = document.querySelector("#object-form");
const nameInput = document.querySelector("#profile-name");
const roleInput = document.querySelector("#profile-role");
const levelInput = document.querySelector("#profile-level");
const activeInput = document.querySelector("#profile-active");
const titleOutput = document.querySelector("#object-title");
const jsonOutput = document.querySelector("#object-json");
const propertyList = document.querySelector("#property-list");

function renderObject() {
  titleOutput.textContent = profile.name + " · " + profile.role;
  jsonOutput.textContent = JSON.stringify(profile, null, 2);
  propertyList.replaceChildren();
  Object.entries(profile).forEach(([property, value]) => {
    const card = document.createElement("article");
    const label = document.createElement("span");
    const content = document.createElement("strong");
    label.textContent = property;
    content.textContent = String(value);
    card.append(label, content);
    propertyList.append(card);
  });
}

form.addEventListener("submit", event => {
  event.preventDefault();
  profile.name = nameInput.value.trim();
  profile.role = roleInput.value.trim();
  profile.level = Number(levelInput.value);
  profile.active = activeInput.checked;
  profile.updatedAt = new Date().toLocaleTimeString();
  renderObject();
});

renderObject();
