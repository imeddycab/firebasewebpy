import web
from models.personas import Personas

# Instancia del modelo Personas
personas_model = Personas()

# Configurar renderizado de plantillas
render = web.template.render("views/personas", base="../master")

class EliminarPersona:
    def GET(self, id_persona):
        try:
            # Obtener los datos de la persona
            respuesta = personas_model.obtener_persona(id_persona)
            
            if respuesta["status"] == 200:
                persona = respuesta["persona"]
                persona["id"] = id_persona
            else:
                persona = {}

            # Renderizar la página de confirmación
            return render.confirmar_eliminar(id_persona=id_persona, persona=persona, eliminado=False)
        except Exception as error:
            print(f"Error: {error}")
            return "Se produjo un error, vuelve a intentar más tarde."

    def POST(self, id_persona):
        try:
            # Eliminar la persona
            resultado = personas_model.eliminar_persona(id_persona)
            
            if resultado["status"] == 200:
                # Mostrar la página de confirmación con el mensaje de éxito
                return render.confirmar_eliminar(id_persona=id_persona, persona={}, eliminado=True)
            else:
                # Mostrar un mensaje de error
                return "Error al eliminar la persona."
        except Exception as error:
            print(f"Error: {error}")
            return "Se produjo un error, vuelve a intentar más tarde."