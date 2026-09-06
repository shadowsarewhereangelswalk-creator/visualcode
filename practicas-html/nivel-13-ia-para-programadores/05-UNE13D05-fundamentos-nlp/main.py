from collections import Counter
import re
texto="La inteligencia artificial ayuda a procesar lenguaje natural y automatizar tareas"
tokens=re.findall(r"[a-záéíóúñ]+",texto.lower())
print(tokens)
print(Counter(tokens).most_common(5))
