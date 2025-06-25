# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la conexión a PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:luis8877@localhost:5432/tareaspadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de datos
class Tarea(db.Model):
    __tablename__ = 'tareas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    hecha = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

# CRUD básico

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    tareas = Tarea.query.all()
    return jsonify([{'id': t.id, 'nombre': t.nombre, 'hecha': t.hecha} for t in tareas])

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    datos = request.json
    nueva = Tarea(nombre=datos['nombre'])
    db.session.add(nueva)
    db.session.commit()
    return jsonify({'mensaje': 'Tarea creada'}), 201

@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea = Tarea.query.get(id)
    if tarea:
        return jsonify({'id': tarea.id, 'nombre': tarea.nombre, 'hecha': tarea.hecha})
    return jsonify({'error': 'No encontrada'}), 404

@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({'error': 'No encontrada'}), 404
    datos = request.json
    tarea.nombre = datos.get('nombre', tarea.nombre)
    tarea.hecha = datos.get('hecha', tarea.hecha)
    db.session.commit()
    return jsonify({'mensaje': 'Tarea actualizada'})

@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({'error': 'No encontrada'}), 404
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({'mensaje': 'Tarea eliminada'})

# Rutas adicionales

# 1. Tareas completadas
@app.route('/tareas/completadas', methods=['GET'])
def tareas_completadas():
    tareas = Tarea.query.filter_by(hecha=True).all()
    return jsonify([{'id': t.id, 'nombre': t.nombre, 'hecha': t.hecha} for t in tareas])

# 2. Tareas pendientes
@app.route('/tareas/pendientes', methods=['GET'])
def tareas_pendientes():
    tareas = Tarea.query.filter_by(hecha=False).all()
    return jsonify([{'id': t.id, 'nombre': t.nombre, 'hecha': t.hecha} for t in tareas])

# 3. Buscar por palabra clave
@app.route('/tareas/buscar/<string:palabra>', methods=['GET'])
def buscar_tareas(palabra):
    filtro = "%{}%".format(palabra)
    tareas = Tarea.query.filter(Tarea.nombre.ilike(filtro)).all()
    return jsonify([{'id': t.id, 'nombre': t.nombre, 'hecha': t.hecha} for t in tareas])

if __name__ == '__main__':
    app.run(debug=True)
