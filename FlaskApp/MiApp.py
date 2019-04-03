#!/usr/bin/python3
#
# Organizacion: Universiada Bolivariana de Venezuela
# Autor: Miguel Marquez
# Nombre de Aplicacion: _FlaskUBV
# Version: 1.0
# Ubicacion: Caracas 24-03-2019
# 

# NOTA 1: La aplicacion presenta un error con el login, 
#		  el nombre de usuario deja de ser persistente
# 		  cuando se 	cae 	o desconecta el servidor
#
# SOLUCION: error corregido editando los parametros 
#			remember=True y duration=None de la funcion 
#			login_user(
#
from flask import Flask, render_template, request, json
from flask_login import LoginManager, current_user, login_user
from flask_login import logout_user, login_required, UserMixin
from flask import redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect 
from werkzeug.exceptions import BadRequestKeyError
import db, form, acceso
#--------------------------------- INSTANCIACION DE OBJETOS FLASK ------------------------
#instancia de la clase (nuevo objeto)
app= Flask(__name__)
#instancia para las sesiones
app.secret_key= 'm1p4l4br4s3cr3t4_'# importante para token csrf y sesiones, ojo con os.get() asignar?
csrf= CSRFProtect(app) # token anti-CSRF
#instancia para las sesiones flask_login
miLogin= LoginManager()
miLogin.init_app(app)
miLogin.login_view= 'login'
miLogin.login_message= "por favor autentiquese para acceder a esta pagina"
#instacia para el frontend
Bootstrap(app)
#--------------------------------- RENDERIZADO DE LAS PAGINAS WEB ------------------------

#Pagina de Error
@app.errorhandler(404)
def paginaNoEncontrada(e):
	return render_template('404.html'), 404

#Pagina Principal
@app.route("/")#decorador indica ruta del servidor al usuario
@app.route("/index")

def main():
	miFormulario= form.Login()
	return render_template('index.html', form= miFormulario)

#Pagina Registrar
@app.route('/showSignUp')
def showSignUp():# crea los formularios en la pagina web

	if not current_user.is_authenticated:

		miFormulario= form.Formulario()
		return render_template('signup.html', form= miFormulario)
		
	else:
		return redirect(url_for('main'))

#Pagina CRUD
#NOTA: cuando intento acceder a /crud imprime error por el metodo de envio POST
#NOTA2: necesito metodo GET 
@app.route('/crud',methods=['GET','POST'])
@login_required
def crud():
	#li=('1','2','3','4','5')
	#usuarioActual= current_user.id
	#usuarioActual= current_user.nombre
	#print("el usuario actual es: "+ str(usuarioActual))

	#OJO HACER UNA EXCEPCION try except????????????????????????????????????????????
	try:

		valorEditar= request.form['valorEditar']
		tuplaEliminar= request.form['tuplaEliminar']

		print(tuplaEliminar)
		dropDB(tuplaEliminar)

	except BadRequestKeyError:
	 	print(BadRequestKeyError)

	return render_template('crud.html', lista=getDB()) #, user=usuarioActual)
#-------------------------------------------------------------------------------------------
#--------------------------------- OPERACIONES DE SESION------------------------------------
nombre='' #variable global OJO EL ERROR EN LA SESION QUIZA ES PROBOCADO POR ESO 1
@app.route('/login',methods=['POST'])
def login():

	misDatos= form.Login(request.form)# NOTA: quiza haya que transladar a clase User()
	cedula= misDatos.cedula.data
	global nombre # OJO EL ERROR EN LA SESION QUIZA ES PROBOCADO POR ESO 2
	nombre= misDatos.nombre.data 

	print("cedula: "+str(cedula)+" "+"nombre: "+nombre)

	if noEstaVacio(cedula, nombre) and coincidenConLaBD(cedula, nombre):

		login_user(acceso.User(cedula, nombre),remember=True, duration=None)

		usuarioActual= current_user.nombre

		#print("el usuario actual es: "+ str(usuarioActual)+" y esta autenticado?: "+ str(current_user.is_authenticated))
		#return 'usted tiene acceso'
		#return redirect(url_for('crud')) << OJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
		#flash('Usted ha accedido') #Ojo con esto
		return render_template('crud.html', lista=getDB(), user=usuarioActual)#, form= miFormulario)

	else:
		flash('Error: cedula o nombre incorrectos!')
		return redirect(url_for('main'))

@miLogin.user_loader
def load_user(user_id):
	global nombre# OJO EL ERROR EN LA SESION QUIZA ES PROBOCADO POR ESO 3
	#print("load_user >> user_id: "+user_id+" nombre:"+acceso.nombre)
	return acceso.User(user_id, nombre)
	

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('usted ha salido!')
	return redirect(url_for('main'))
#salir
#@app.route('/logout')
#def logout():
#	if 'username' in session:
#		session.pop()
#	return redirect(url_for('main'))# main es la funcion
def noEstaVacio(cedula, nombre): 

	'''
	Funcion que verifica que los parametros 
	cedula y nombre no esten vacios
	'''

	if cedula != None and nombre != '':
		return True
	else:
		return False
	##
	##

def coincidenConLaBD(cedula, nombre):

	'''
	Funcion que comprueba que los datos
	de acceso existan en la base de datos
	'''

	datos= getDB()
	bandera= False

	for i in range(0, len(datos)):

		comparaCedula= datos[i][0]
		comparaNombre= nombre.upper().find(datos[i][1].upper())# ojo mayusculas y minusculas
		if comparaNombre != -1 and comparaCedula == cedula:#  fin() devuelve -1 si no encuentra ocurrencias
			bandera= True
			break

	return bandera

#--------------------------------OPERACIONES CON EL FORMULARIO------------------------------
#Captura de Datos de Formulario
@app.route('/signUp',methods=['POST'])
def signUp():
	'''
	Funcion que captura los datos del formulario
	de la pagina /showSignUp y los carga en la 
	base de datos mediante la funcion putDB()
	'''
	misDatos= form.Formulario(request.form)
	cedula= misDatos.cedula.data
	nombre= misDatos.nombre.data
	apellido= misDatos.apellido.data
	telefono= misDatos.telefono.data
	direccion= misDatos.direccion.data
	#print(str(cedula)+' '+nombre+' '+apellido+' '+telefono+' '+direccion)
	putDB(cedula, nombre, apellido, telefono, direccion) 
	flash('datos enviados!')
	return redirect(url_for('main'))
	#return json.dumps({'html':'<span> Prueba Json </span>'})

		
#--------------------------------- OPERACIONES CON LA BD------------------------------------
#Insertar en la Base de Datos	
def putDB(cedula, nombre, apellido, telefono, direccion):
	print(str(cedula)+' '+nombre+' '+apellido+' '+telefono+' '+direccion)
	conexion= db.mysql.connect()
	cursor= conexion.cursor()
	consulta='INSERT INTO Datos(cedulad, nombred, apellidod, direccion, telefono) VALUES ("'+str(cedula)+'", "'+nombre+'", "'+apellido+'", "'+direccion+'", "'+telefono+'")'
	#consulta='INSERT INTO Datos(cedulad, nombred, apellidod, direccion, telefono) VALUES (%s, %s, %s, %s, %s)'
	#cursor.execute(consulta,(cedula, nombre, apellido, direccion, telefono))
	cursor.execute(consulta)
	conexion.commit()

#Imprimir la Base de Datos
def getDB():
	conexion= db.mysql.connect()
	cursor= conexion.cursor()
	cursor.execute('SELECT * FROM Datos')
	return cursor.fetchall()
	#datos= cursor.fetchall()
	#print(datos[0][0])

#Eliminar de la Base de Datos
def dropDB(valor):
	conexion= db.mysql.connect()
	cursor= conexion.cursor()
	cursor.execute('DELETE FROM Datos WHERE cedulad = '+valor)
	conexion.commit()

#-------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, host='10.0.70.23', port=80)#ejecuta el servidor en el púerto 5000
