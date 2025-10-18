from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista de reportes almacenados en memoria (solo para prototipo)
reportes = []

@app.route('/')
def index():
    return render_template('index.html', reportes=reportes)

@app.route('/reporte', methods=['POST'])
def agregar_reporte():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos vacíos'}), 400
    data['id'] = len(reportes) + 1  # ID incremental
    reportes.append(data)
    return jsonify({'status': 'Reporte agregado', 'id': data['id']})

@app.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_reporte(id):
    global reportes
    reportes = [r for r in reportes if r['id'] != id]
    return jsonify({'status': 'Reporte eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
