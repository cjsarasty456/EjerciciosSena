# Se procede a importar la libreria de Flask
# para la gestión de peticiones Web
from flask import Flask
# Se procede a importar la libreria de render_template
# para renderizar y mostrar las páginas web
# Para poder enviar información se incorpora el modulo request
# para enviar la información se envía como una request o solicitud
# de información
from flask import render_template,request
# Para establecer conexión con la base de datos se importa la
# Libreria flaskext.mysql
from flaskext.mysql import MySQL
# se importa la libreria de fecha y tiempo en el objeto datetime
from datetime import datetime

# Se procede a utilizar la libreria flask instanciando
app= Flask(__name__)

# Se procede a ejecutar la librería MySQL
mysql=MySQL()
# Para establecer conexión con la base de datos
# MYSQL_DATABASE_HOST permite establecer la ubicación del 
# servidor que ejecuta la base de datos
# localhost representa el servidor local
app.config['MYSQL_DATABASE_HOST']='localhost'
# MYSQL_DATABASE_USER permite establecer el usuario
#se debe registrar un usuario valido para la base de datos
#root es el usuario raíz, que es el usuario por defecto
app.config['MYSQL_DATABASE_USER']='root'
# MYSQL_DATABASE_PASSWORD permite establecer la contraseña
#se debe registrar la contraseña que tiene el usuario
#por defecto la contraseña del usuario root es una cadena
# vacia
app.config['MYSQL_DATABASE_PASSWORD']=''
# MYSQL_DATABASE_DB permite establecer el nombre
# la base de datos
app.config['MYSQL_DATABASE_DB']='sistemapython'
# Se procede a iniciar la conexión
mysql.init_app(app)

# Para saber que acción o página mostrar se necesita enrutar
# indicando hacia donde ir según la url registrada
# El valor por defecto para cargar nuestra página se 
# indica la carpeta raíz o default
@app.route('/')
def index():
    # # ejemplo instrucción sql
    # # Se define la variable sql para almacenar la sentencia SQL que
    # # se va a ejecutar en el gestor de Base de datos
    # # en el ejemplo se procede a registrar la información en la
    # # tabla empleado
    # sql="INSERT INTO empleado (id, nombre, correo, foto) VALUES (NULL, 'Carlos', 'carlos@email.com', 'foto.jpg')"
    # # se define una variable llamada conn que almacena la conexión
    # # con el servidor de base de datos
    # # mysql.connect() es una función que establece conexión
    # # con la base de datos 
    # conn=mysql.connect()
    # # El cursor se utiliza para recorrer los registros resultado de la consulta
    # #  
    # cursor=conn.cursor()
    # # función execute se utiliza para ejecutar la consulta definida
    # # dentro de la sentencia sql
    # cursor.execute(sql)
    # # la función commit se utiliza para cerrar la conexión
    # conn.commit()
# cuan el usuario ingrese el slash se retorna la página
# html renderizada para que el usuario la visualice
    return render_template('empleados/index.html')

# Página formulario para crear un registro de empleado
@app.route("/create")
def create():
    return render_template('empleados/create.html')

# Función para crear un registro de empleado

# ruta que recibe las peticiones con envío POST
@app.route('/store', methods=['POST'])
def storage():
    #mediante el request.form se recibe los datos del formulario
    #en el corchete se agrega lo que se agregó en el atributo name
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtfoto']
    #se procede a cambiar el nombre de la foto para que no se
    #reemplace en dado caso que tenga dos archivos con el
    #mismo nombre ejemplo foto.jpg
    #por lo cual se procede a cambiar el nombre del archivo
    #usando la fecha y hora en el momento que se carga
    #Se obtiene la fecha y hora actual
    now=datetime.now()
    #luego se procede a guardar la fecha en el formato
    #año hora minuto segundo todo pegado
    tiempo=now.strftime("%Y%H%M%S")
    #se evalua que si el nombre es diferente a vacio se procede
    
    if _foto.filename!='':
    #al crear el nombre del archivo con el tiempo y el nombre actual
    #del archivo actual
    # y por ultimo se guarda el archivo en la ubicación uploads
    #y el nombre gene rado
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
    # ejemplo instrucción sql
    # Se define la variable sql para almacenar la sentencia SQL que
    # se va a ejecutar en el gestor de Base de datos
    # en el ejemplo se procede a registrar la información en la
    # tabla empleado
    sql="INSERT INTO empleado (id, nombre, correo, foto) VALUES (NULL,%s,%s,%s)"
    #Se reemplaza los datos fijos por %s, para indicar que ahí van los datos que
    #se van a agregar con el arreglo encontrado posteriormente, y en el orden
    #agregados
    # datos=(_nombre,_correo,_foto.filename)
    datos=(_nombre,_correo,nuevoNombreFoto)
    # se define una variable llamada conn que almacena la conexión
    # con el servidor de base de datos
    # mysql.connect() es una función que establece conexión
    # con la base de datos 
    conn=mysql.connect()
    # El cursor se utiliza para recorrer los registros resultado de la consulta
    #  
    cursor=conn.cursor()
    # función execute se utiliza para ejecutar la consulta definida
    # dentro de la sentencia sql
    #se agrega el arreglo datos
    cursor.execute(sql,datos)
    # la función commit se utiliza para cerrar la conexión
    conn.commit()
    return render_template('empleados/index.html')

# Para que se pueda interpretar lo que se está haciendo 
# si el archivo que se está ejecutando correr la aplicación
# y habilitar la depuración para hacer modificaciones o depurar
if __name__=='__main__':
    app.run(debug=True)

# para ejecutar el archivo python en terminal se escribe
# python app.py