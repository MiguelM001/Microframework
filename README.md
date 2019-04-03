# Microframework
Microframework Flask Personalizado

PROCESO DE INSTALACION DE FLASK
INSTALAR PIP 3

pip: es un sistema de gestion de paquetes para python (instalador e paquetes) que usa el repositorio PYPI (Python Package Index)

    1.- apt-get install python3-pip
    2.- ver modulos instalados via pip:
        pip3 freeze
        pip3 list

INSTALAR VIRTUALENV

virtualenv: es un entorno virtual de python, que nos permite aislar recursos y librerias, posibilitando la instalacion de una libreria y sus distintas versiones sin que haya ningun tipo de conflicto.

    1.- pip3 install virtualenv #Para usar con python3
    2.- ubicarse en directorio deseado ejemplo: cd /home/user
    3.- virtualenv env --python=python3 #donde env es el nombre del proyecto/carpeta del entorno virtual
    3.- ls | grep env #cerciorarse de que se creo la carpeta
    4.- cd env/ #entrar en la carpeta
    5.- source bin/activate #activar el entorno virtual: se ejecuta el escript activate de virtualenv en bin/
    (env) root@debian:/home/miguel/env #debe mostar algo similar

INSTALAR FLASK

flask: es un microframework de python, ideal para principiantes, que usa la tecnologia WSGI (Web Server Gateway Interface), similar a la especificacion de java servlet o ASP/ASP.NET pero mucho mas simple, basado en el estandar CGI, enfocado en python.

    1.- pip3 install flask #dentro del entorno virutal y en minusculas
    2.- ejecutar flask: FLASK_APP=mi_archivo_flask.py flask run
        otra manera de ejecutar flask es llamando a la funcion "app.run()" dentro del archivo que contiene el codigo fuente, luego de: if __name__ == "__main__":
        
codigo de ejemplo:

from flask import Flask

app= Flask(__name__)

@app.route("/")
def main():
	return "Hola mundo!"

if __name__ == "__main__":
    app.run()

problemas y soluciones:

Mensaje de error: WARNING: "Do not use the development server in a production environment".

A menos que le indique al servidor, que se está ejecutando en modo de desarrollo, asumirá que lo está utilizando en producción y le advertirá que no lo haga.

Habilite el modo de desarrollo estableciendo la variable de entorno FLASK_ENV para el desarrollo.

Por defecto: export FLASK_ENV=production #ideal cuando el sistema esté culminado

Cambiar a: export FLASK_ENV=development #se habilita el modo de depuracion

En caso de que su sistema web no se visualice en el navegador quiza el problema se derive de la interfaz loopback, abrir puerto por defecto (5000) creando una regla iptables:

iptables -t filter -I INPUT -i lo -p tcp --dport 5000 -j ACCEPT

nota:

Cuando lance su aplicacion web a produccion en lugar de en desarrollo, no debería utilizar el servidor de desarrollo incorporado (flask run). El servidor de desarrollo es proporcionado por Werkzeug por conveniencia o simplicidad, pero no está diseñado para ser particularmente eficiente, estable o seguro.

En su lugar, utilice un servidor WSGI de producción. Por ejemplo: Waitress, tambien puede utilizar otros servidores web como Apache2 o Ngix, que puede integrar con flask a traves de un servidor de aplicaciones tal que: uWSGI.

esquema:

    flask/
    templates/ #todos los archivos html(renderizado) se guardan aca
        auth/
        blog/
        base/ #herencia
    static/ #imagenes, hojas de estilo, javascript
        css/
        js/
        img/

entre sus propiedades mas destacadas:

    Herencia
    Macros

JINJA2

Jinja es un lenguaje de plantillas (templates) escrito en Python, el cual permite insertar datos procesados y texto predeterminado dentro de un documento de texto.

a.- expresiones.

Las expresiones deben estar encerradas entre llaves "{ }".

Sintaxis:

{{ <expresión> }}

b.- declaraciones.

Las declaraciones deben estar encerradas entre signos de porcentaje "%".

{% <declaración> %}

...

...

{% endof <tipo de declaración> %}

c.- comentarios.

Sintaxis:

{# <comentario> #}
INSTALAR MODULOS FLASK

pip3 install flask-modulo #(ojo dentro del entorno virtualenv)

Modulos usados en este sistema:

    Flask 1.0.2 #microframework
    Flask-Login 0.4.1 #modulo para sesiones
    Flask-MySQL 1.4.0 #modulo para conectar con base de datos
    Flask-WTF 0.14.2 #modulo para formularios
    Flask-Bootstrap 3.3.7.1 #modulo framework frontend
    Jinja2 2.10 #lenguaje de plantillas (instalado por defecto con Flask )
    Werkzeug 0.14.1 # librería de utilidades HTTP y WSGI para Python ( instalado por defecto con Flask )

REFERENCIAS

    documentacion:
    http://www.python.org.ar/wiki/WSGI
    https://es.wikipedia.org/wiki/Flask
    https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen?rq=1
    http://flask.pocoo.org/docs/dev/tutorial/deploy/

    configuracion:
    http://flask.pocoo.org/docs/1.0/config/

    API:
    http://flask.pocoo.org/docs/1.0/api/

    flask-wtf:
    https://wtforms.readthedocs.io/en/stable/validators.html#

    wtforms:
    https://www.tutorialspoint.com/flask/flask_wtf.htm
    https://wtforms.readthedocs.io/en/stable/validators.html#wtforms.validators.IPAddress

    jinja2:
    https://pythonista.io/cursos/py201/introduccion-a-jinja-2
    http://jinja.pocoo.org/docs/2.10/templates/

    bootstrap:
    https://pythonhosted.org/Flask-Bootstrap/basic-usage.html

    flask-login:
    https://plataforma.josedomingo.org/pledin/cursos/flask/curso/u30/
    https://flask-login.readthedocs.io/en/latest/
    https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one#toc-auth-blueprint
    https://ernestocrespo13.wordpress.com/2016/09/24/tutorial-de-flask-parte-5-login-de-los-usuarios/
    https://yo.toledano.org/desarrollo/login-con-flask.html
    https://infinidum.com/2018/08/18/making-a-simple-login-system-with-flask-login/
    https://teamtreehouse.com/community/how-usermixin-and-class-inheritance-work
    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis

