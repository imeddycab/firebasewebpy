import web
import pyrebase

class Personas:
    def get_personas(self):
        data = db.child("personas").get()
        return data
    def insertar_persona(self,data):
        