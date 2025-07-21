from flask import Flask, render_template, request, redirect, url_for, flash
from models.pila import PilaApoyos
from models.cola import ColaTarjetas

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Instanciar las estructuras de datos
pila_apoyos = PilaApoyos()
cola_tarjetas = ColaTarjetas()

@app.route('/')
@app.route('/menu')
def menu():
    """Página principal del menú"""
    return render_template('menu.html')

@app.route('/cola', methods=['GET', 'POST'])
def cola():
    """Maneja la cola de tarjetas de apoyo"""
    mensaje = ""
    
    if request.method == 'POST':
        if 'agregar_persona' in request.form:
            persona = request.form.get('persona', '').strip()
            if persona:
                mensaje = cola_tarjetas.encolar(persona)
            else:
                mensaje = "Por favor ingrese el nombre de la persona"
        
        elif 'procesar_tarjeta' in request.form:
            if not cola_tarjetas.esta_vacia():
                persona_procesada = cola_tarjetas.desencolar()
                mensaje = f"Tarjeta entregada a: {persona_procesada}"
            else:
                mensaje = "No hay personas en la cola para procesar"
        elif 'eliminar_persona' in request.form:
            indice = int(request.form.get('eliminar_persona', -1))
            mensaje = cola_tarjetas.eliminar_por_indice(indice)
    
    return render_template('cola.html', 
                         cola=cola_tarjetas.mostrar_cola(), 
                         mensaje=mensaje,
                         tamano=cola_tarjetas.obtener_tamano())

@app.route('/pila', methods=['GET', 'POST'])
def pila():
    """Maneja la pila de historial de apoyos"""
    mensaje = ""
    
    if request.method == 'POST':
        if 'agregar_apoyo' in request.form:
            apoyo = request.form.get('apoyo', '').strip()
            if apoyo:
                mensaje = pila_apoyos.empilar(apoyo)
            else:
                mensaje = "Por favor ingrese el tipo de apoyo"
        
        elif 'remover_apoyo' in request.form:
            if not pila_apoyos.esta_vacia():
                apoyo_removido = pila_apoyos.desempilar()
                mensaje = f"Apoyo removido: {apoyo_removido}"
            else:
                mensaje = "No hay apoyos en el historial para remover"
        elif 'eliminar_apoyo' in request.form:
            indice = int(request.form.get('eliminar_apoyo', -1))
            mensaje = pila_apoyos.eliminar_por_indice(indice)
    
    return render_template('pila.html', 
                         pila=pila_apoyos.mostrar_pila(), 
                         mensaje=mensaje,
                         tamano=pila_apoyos.obtener_tamano())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
