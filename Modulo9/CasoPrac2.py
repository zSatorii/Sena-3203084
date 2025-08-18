from flask import Flask, request, jsonify
import sys
import os

# Añadir directorio padre al path para importar nuestro paquete
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matematicas.aritmetica import suma, resta, multiplicacion
from matematicas.geometria import area_circulo, area_rectangulo

app = Flask(__name__)

@app.route('/suma', methods=['GET'])
def api_suma():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    resultado = suma(a, b)
    return jsonify({'operacion': 'suma', 'a': a, 'b': b, 'resultado': resultado})

@app.route('/area/circulo', methods=['GET'])
def api_area_circulo():
    radio = float(request.args.get('radio', 0))
    resultado = area_circulo(radio)
    return jsonify({'figura': 'circulo', 'radio': radio, 'area': resultado})

@app.route('/area/rectangulo', methods=['GET'])
def api_area_rectangulo():
    ancho = float(request.args.get('ancho', 0))
    alto = float(request.args.get('alto', 0))
    resultado = area_rectangulo(ancho, alto)
    return jsonify({'figura': 'rectangulo', 'ancho': ancho, 'alto': alto, 'area': resultado})

if __name__ == '__main__':
    app.run(debug=True)
