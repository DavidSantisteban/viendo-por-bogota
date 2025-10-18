from flask import Flask, render_template, request, redirect

app = Flask(__name__)
reportes = []  # Guardará los reportes temporalmente

@app.route('/')
def index():
    return render_template('index.html', reportes=reportes)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    tipo = request.form['tipo']
    descripcion = request.form['descripcion']
    latitud = request.form['latitud']
    longitud = request.form['longitud']

    nuevo_reporte = {
        'nombre': nombre,
        'tipo': tipo,
        'descripcion': descripcion,
        'latitud': latitud,
        'longitud': longitud
    }

    reportes.append(nuevo_reporte)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
