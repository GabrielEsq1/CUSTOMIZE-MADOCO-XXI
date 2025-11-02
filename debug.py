import os
from flask import Flask

app = Flask(__name__)

# Mostrar estructura de carpetas
print("Estructura actual:")
for root, dirs, files in os.walk("."):
    level = root.replace(".", "").count(os.sep)
    indent = " " * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = " " * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

# Verificar si existe templates/custom.html
template_path = os.path.join("templates", "custom.html")
print(f"\n¿Existe templates/custom.html? {os.path.exists(template_path)}")

@app.route('/')
def index():
    return "¡Flask funciona! Ahora agrega los templates."

if __name__ == '__main__':
    app.run(debug=True)