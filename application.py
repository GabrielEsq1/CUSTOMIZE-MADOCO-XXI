from flask import Flask, render_template
import os

# Configurar la ruta de templates manualmente
template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(__name__,
            template_folder=template_dir,
            static_folder=static_dir)

@app.route('/')
def index():
    return render_template('custom.html')

@app.route('/custom')
def custom():
    return render_template('custom.html')

# NUEVA RUTA AÑADIDA
@app.route('/location')
def location():
    return render_template('location.html')

if __name__ == '__main__':
    print(f"Buscando templates en: {template_dir}")
    print(f"¿Existe custom.html? {os.path.exists(os.path.join(template_dir, 'custom.html'))}")
    print(f"¿Existe location.html? {os.path.exists(os.path.join(template_dir, 'location.html'))}")
    app.run(debug=True)