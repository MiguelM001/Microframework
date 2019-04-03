#Mejorar
from flask_login import  UserMixin

class User(UserMixin):
	def __init__(self, id, nombre):# constructor
		self.id= id
		self.nombre= nombre