import web
from models.personas import Personas

# Instancia del modelo Personas
personas_model = Personas()

# Configurar renderizado de plantillas
render = web.template.render("views/personas", base="../master")

class EditarPersona:
    def GET(self, id_persona):
        try:
            # Obtener los datos de la persona
            respuesta = personas_model.obtener_persona(id_persona)
            
            if respuesta["status"] == 200:
                persona = respuesta["persona"]
                persona["id"] = id_persona
            else:
                persona = {}

            # Renderizar la plantilla con los datos de la persona
            return render.editar_persona(persona=persona)
        except Exception as error:
            print(f"Error: {error}")
            return "Se produjo un error, vuelve a intentar más tarde."

    def POST(self, id_persona):
        data = web.input()
        name = data.name
        phone = data.phone

        try:
            # Actualizar los datos de la persona
            resultado = personas_model.actualizar_persona(id_persona, name, phone)
            
            # Renderizar la plantilla con el resultado de la actualización
            return render.editar_persona(resultado=resultado, persona={"id": id_persona, "name": name, "phone": phone})
        except Exception as error:
            print(f"Error: {error}")
            # Renderizar la plantilla con un mensaje de error
            return render.editar_persona(resultado={
                "status": 400,
                "message": "Se produjo un error al actualizar la persona.",
                "id": None
            }, persona={"id": id_persona})