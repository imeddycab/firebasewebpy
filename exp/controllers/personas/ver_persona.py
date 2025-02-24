import web
from models.personas import Personas

# Instancia del modelo Personas
personas_model = Personas()

# Configurar renderizado de plantillas
render = web.template.render("views/personas", base="../master")

class VerPersona:
    def GET(self, id_persona):
        try:
            # Obtener los datos de la persona
            respuesta = personas_model.obtener_persona(id_persona)

            if respuesta["status"] == 200:
                persona = respuesta["persona"]
                # Agregar el id a los datos de la persona para mostrarlo en la vista
                persona['id'] = id_persona
            else:
                persona = {}

            print(f"CONSULTA DE PERSONA {id_persona}: {persona}")

            # Renderizar la vista con los datos obtenidos
            return render.ver_persona(persona)
        except Exception as error:
            import traceback
            print(f"Error: {error}")
            traceback.print_exc()
            return "Se produjo un error, vuelve a intentar más tarde."