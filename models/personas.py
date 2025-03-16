import web
import pyrebase

config = {
    "apiKey": "AIzaSyBpCAJn5-QBxSt1Er-DTxt59MBQn_839B4",
    "authDomain": "eddydemo-f3fa8.firebaseapp.com",
    "databaseURL": "https://eddydemo-f3fa8-default-rtdb.firebaseio.com",
    "storageBucket": "eddydemo-f3fa8.appspot.com"
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
                "message": "Todo en orden",
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

    def obtener_ultimo_id(self):
        try:
            personas = db.child("personas").get()
            if personas.val():
                # Obtener todos los IDs existentes y convertirlos a enteros
                ids = [int(id) for id in personas.val().keys()]
                # Encontrar el ID máximo y sumarle 1
                ultimo_id = max(ids) + 1
                # Formatear el ID para que tenga 3 dígitos (001, 002, etc.)
                return f"{ultimo_id:03}"
            else:
                # Si no hay personas registradas, empezar con 001
                return "001"
        except Exception as error:
            print(f"Error al obtener el último ID: {error}")
            return "001"

    def insertar_persona(self, name, phone):
        try:
            person_id = self.obtener_ultimo_id()
            person_data = {"name": name, "phone": phone}
            db.child("personas").child(person_id).set(person_data)
            
            # Devolver el JSON con el formato deseado
            response = {
                "status": 200,
                "message": "Persona registrada con éxito",
                "id": person_id
            }
            return response
        except Exception as error:
            print(f"Error: {error}")
            # Devolver un JSON en caso de error
            response = {
                "status": 400,
                "message": "Se produjo un error, vuelve a intentar más tarde.",
                "id": None
            }
            return response

    def obtener_persona(self, id_persona):
        try:
            persona = db.child("personas").child(id_persona).get()
            if persona.val():
                response = {
                    "status": 200,
                    "message": "Persona encontrada",
                    "persona": persona.val()
                }
            else:
                response = {
                    "status": 404,
                    "message": "Persona no encontrada",
                    "persona": {}
                }
            return response
        except:
            response = {
                "status": 400,
                "message": "Error al obtener persona",
                "persona": {}
            }
            return response

    def actualizar_persona(self, id_persona, name, phone):
        try:
            # Actualizar los datos de la persona en Firebase
            db.child("personas").child(id_persona).update({"name": name, "phone": phone})
            
            # Devolver una respuesta exitosa
            response = {
                "status": 200,
                "message": "Persona actualizada con éxito",
                "id": id_persona
            }
            return response
        except Exception as error:
            print(f"Error: {error}")
            # Devolver un JSON en caso de error
            response = {
                "status": 400,
                "message": "Se produjo un error al actualizar la persona.",
                "id": None
            }
            return response

    def eliminar_persona(self, id_persona):
        try:
            # Eliminar la persona de Firebase
            db.child("personas").child(id_persona).remove()
            
            # Devolver una respuesta exitosa
            response = {
                "status": 200,
                "message": "Persona eliminada con éxito",
                "id": id_persona
            }
            return response
        except Exception as error:
            print(f"Error: {error}")
            # Devolver un JSON en caso de error
            response = {
                "status": 400,
                "message": "Se produjo un error al eliminar la persona.",
                "id": None
            }
            return response

personas = Personas()