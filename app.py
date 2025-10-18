from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Lista para almacenar los reportes
reportes = []

# Diccionario base para asignar entidad según tipo de problema
ENTIDADES = {
    "bache": "IDU - Instituto de Desarrollo Urbano",
    "alumbrado": "UAESP - Unidad Administrativa de Servicios Públicos",
    "basura": "UAESP - Aseo y Gestión de Residuos",
    "vandalismo": "Policía Metropolitana de Bogotá",
    "ruido": "Secretaría de Ambiente",
    "otro": "Alcaldía Local correspondiente"
}

@app.route('/')
def index():
    return render_template('index.html', reportes=reportes)

@app.route('/reporte', methods=['POST'])
def reporte():
    data = request.get_json()
    tipo = data.get("tipo", "otro").lower()
    entidad = ENTIDADES.get(tipo, "Alcaldía Local correspondiente")
    
    nuevo_reporte = {
        "lat": data["lat"],
        "lng": data["lng"],
        "tipo": tipo,
        "descripcion": data["descripcion"],
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "entidad": entidad
    }
    reportes.append(nuevo_reporte)
    return jsonify({"status": "ok"})

@app.route('/data')
def data():
    return jsonify(reportes)

if __name__ == '__main__':
    app.run(debug=True)
