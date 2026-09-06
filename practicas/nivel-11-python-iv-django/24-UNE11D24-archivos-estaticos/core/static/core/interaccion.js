const boton = document.querySelector("#alternar");

boton.addEventListener("click", () => {
    document.body.classList.toggle("oscuro");
    localStorage.setItem("tema", document.body.classList.contains("oscuro") ? "oscuro" : "claro");
});

if (localStorage.getItem("tema") === "oscuro") {
    document.body.classList.add("oscuro");
}

