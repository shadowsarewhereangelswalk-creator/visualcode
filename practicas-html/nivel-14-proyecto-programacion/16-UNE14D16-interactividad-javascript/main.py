from pathlib import Path
js='''const formulario=document.querySelector("#form");formulario.addEventListener("submit",evento=>{evento.preventDefault();const datos=Object.fromEntries(new FormData(formulario));localStorage.setItem("solicitud",JSON.stringify(datos));alert("Solicitud guardada")});'''
Path("app.js").write_text(js,encoding="utf-8")
print("app.js creado")
