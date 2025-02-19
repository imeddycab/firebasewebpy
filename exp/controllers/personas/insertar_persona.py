import web
from models.personas import Personas

# Instancia del modelo Personas
personas_model = Personas()

# Configurar renderizado de plantillas
render = web.template.render("views/personas", base="../master")

class InsertarPersona:
    def GET(self):
        try:
            return render.insertar_persona()
        except Exception as error:
            print(f"Error: {error}")
            return "Se produjo un error, vuelve a intentar más tarde."

    def POST(self):
        data = web.input()
        name = data.name
        phone = data.phone

        try:
            # Insertar la persona en la base de datos
            resultado = personas_model.insertar_persona(name, phone)
            
            # Devolver la respuesta JSON
            web.header('Content-Type', 'application/json')
            return resultado
        except Exception as error:
            print(f"Error: {error}")
            # Devolver un JSON en caso de error
            web.header('Content-Type', 'application/json')
            return {
                "status": 400,
                "message": "Se produjo un error, vuelve a intentar más tarde.",
                "id": None
            }