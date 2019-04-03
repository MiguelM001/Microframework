#DB_Conexion
from flask import Flask
from flaskext.mysql import MySQL

app= Flask(__name__)

mysql= MySQL()

#Configuracion

app.config['MYSQL_DATABASE_USER']= 'flask'
app.config['MYSQL_DATABASE_PASSWORD']= '123456'
app.config['MYSQL_DATABASE_DB']= 'Login'
app.config['MYSQL_DATABASE_HOST']= 'localhost'
mysql.init_app(app)

#conexion= mysql.connect()
#cursor= conexion.cursor()
#cursor.execute('SELECT * FROM Datos')
#datos= cursor.fetchall()

#print(datos[0][0])
