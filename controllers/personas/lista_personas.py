import web
from models.personas import Personas

# Instancia del modelo Personas
personas_model = Personas()

# Configurar renderizado de plantillas
render = web.template.render("views/personas", base="../master")

class ListaPersonas:
    def GET(self):
        try:
            # Obtener la lista de personas desde el modelo
            respuesta = personas_model.lista_personas()
            
            # Extraer los datos de personas si la respuesta es exitosa
            if respuesta["status"] == 200:
                lista_personas = respuesta["personas"]
            else:
                lista_personas = {}

            print(f"CONSULTA DE PERSONAS: {lista_personas}")

            # Pasar los datos a la plantilla HTML
            return render.lista_personas(lista_personas)
        except Exception as error:
            import traceback
            print(f"Error: {error}")
            traceback.print_exc()
            return "Se produjo un error, vuelve a intentar más tarde."
