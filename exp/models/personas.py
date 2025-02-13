import web
import pyrebase

config = {
    "apiKey": "AIzaSyBpCAJn5-QBxSt1Er-DTxt59MBQn_839B4",
    "authDomain": "eddydemo-f3fa8.firebaseapp.com",
    "databaseURL": "https://eddydemo-f3fa8-default-rtdb.firebaseio.com",
    "storageBucket": "eddydemo-f3fa8.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)

# Conexión a la base de datos
db = firebase.database()

class Personas:
    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            response = {
                "status": 200,
                "message": "Todo en ordern",
                "personas": dict(personas.val())
            }
            return response
        except:
            response = {
                "status": 400,
                "message": "Todo mal",
                "personas": {}
            }
            return response

personas = Personas()
print(f"{personas.lista_personas()}")