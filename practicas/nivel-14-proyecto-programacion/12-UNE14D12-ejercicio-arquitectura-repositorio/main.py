arquitectura={"app":["routes.py","database.py","ai.py"],"templates":["index.html"],"static":["styles.css","app.js"],"tests":["test_app.py"]}
for carpeta,archivos in arquitectura.items(): print(carpeta,"->",", ".join(archivos))
