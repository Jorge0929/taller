from flask import current_app as app
from flask import render_template,redirect,url_for,request, Blueprint
import pyodbc
bp= Blueprint(
    "rut_bp",
    __name__
)
# Función para obtener la lista de las tareas desde la base de datos
def obtener_tareas():
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jorge\OneDrive\Documentos\universidad\Buenas practicas de desarrollo\RUBRICA\myprojectweb\TaskDB.accdb;")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tareas")
    tareas = cursor.fetchall()
    cursor.close()
    conn.close()
    return tareas
#Funcion para eliminar 
def eliminar_tarea_por_id(registro_id):
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jorge\OneDrive\Documentos\universidad\Buenas practicas de desarrollo\RUBRICA\myprojectweb\TaskDB.accdb;")
    cursor = conn.cursor()

    # Define la consulta de eliminación
    sql = "DELETE FROM Tareas WHERE ID = ?;"  

    # Ejecuta la consulta de eliminación con el ID proporcionado
    cursor.execute(sql, (registro_id,))
    conn.commit()

    cursor.close()
    conn.close()
# Función para mostrar el índice
@bp.route("/")
def index():
    return render_template("index.html")

# Función para mostrar la lista de tareas
@bp.route("/mostrar_tareas/")
def mostrar_tareas():
    Tareas = obtener_tareas()
    return render_template("mostrar_tareas.html", Tareas=Tareas)

# Función para agregar tareas a la lista
@bp.route("/agregar/", methods=["GET", "POST"])
def agregar_tarea():
    if request.method == "POST":
        nueva_tarea = request.form["descripcion"]
        conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jorge\OneDrive\Documentos\universidad\Buenas practicas de desarrollo\RUBRICA\myprojectweb\TaskDB.accdb;")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tareas (descripcion) VALUES (?)", nueva_tarea)
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for("rut_bp.mostrar_tareas"))

    return render_template("agregar.html")

# Función para eliminar tareas
@bp.route("/eliminar/", methods=["GET", "POST"])
def eliminar_tarea():
    if request.method == "POST":
        eliminar_tarea = request.form["descripcion"]
        conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jorge\OneDrive\Documentos\universidad\Buenas practicas de desarrollo\RUBRICA\myprojectweb\TaskDB.accdb;")
        cursor = conn.cursor()
        sql = "DELETE FROM TAREAS WHERE descripcion = ?;"
        cursor.execute(sql, eliminar_tarea)
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for("rut_bp.mostrar_tareas"))

    return render_template("eliminar.html")
#Funcion para marcar tareas
@bp.route("/marcar_tareas/", methods=["GET", "POST"])
def marcar_tarea():
    if request.method == "POST":
        buscar = request.form["descripcion"]
        nuevo_estado = request.form.get("estado")  # Obtiene "true" o None
        if nuevo_estado == "true":
            nuevo_estado = True  # Convierte a valor booleano True si es "true"
        else:
            nuevo_estado = False  # Si es None o cualquier otro valor, asume False
        conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jorge\OneDrive\Documentos\universidad\Buenas practicas de desarrollo\RUBRICA\myprojectweb\TaskDB.accdb;")
        cursor = conn.cursor()
        cursor.execute("UPDATE Tareas SET estado = ? WHERE descripcion = ?", nuevo_estado, buscar)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("rut_bp.mostrar_tareas"))
    return render_template("marcar_tareas.html")
