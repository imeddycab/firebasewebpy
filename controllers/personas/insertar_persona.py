import web
from models.personas import Personas

# Instancia del modelo Personas
personas_model = Personas()

# Configurar renderizado de plantillas
render = web.template.render("views/personas", base="../master")

class InsertarPersona:
    def GET(self):
        try:
            # Inicializar resultado como None para el método GET
            return render.insertar_persona(resultado=None)
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
            
            # Renderizar la plantilla con el resultado
            return render.insertar_persona(resultado=resultado)
        except Exception as error:
            print(f"Error: {error}")
            # Renderizar la plantilla con un mensaje de error
            return render.insertar_persona(resultado={
                "status": 400,
                "message": "Se produjo un error, vuelve a intentar más tarde.",
                "id": None
            })