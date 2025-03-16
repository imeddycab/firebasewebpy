import web
from models.personas import Personas

# Instancia del modelo Personas
personas_model = Personas()

# Configurar renderizado de plantillas
render = web.template.render("views/personas", base="../master")

class ListaPersonas:
    def GET(self):
        try:
            web.header("Content-Type", "text/html; charset=utf-8")

            # Obtener la lista de personas
            respuesta = personas_model.lista_personas()

            # Extraer los datos de personas si la respuesta es exitosa
            if respuesta["status"] == 200:
                lista_personas = list(respuesta["personas"].items())  # Convertir a lista de tuplas [(id, {datos}), ...]
            else:
                lista_personas = []

            # Parámetros de paginación
            user_data = web.input(page="1")
            try:
                page = int(user_data.page)
                if page < 1:
                    page = 1
            except ValueError:
                page = 1

            per_page = 15  # Cantidad de elementos por página
            total = len(lista_personas)
            total_pages = (total + per_page - 1) // per_page  # Calcular total de páginas

            # Obtener elementos de la página actual
            start = (page - 1) * per_page
            end = start + per_page
            personas_paginadas = dict(lista_personas[start:end])

            # Renderizar la plantilla con datos paginados
            return render.lista_personas(personas_paginadas, page, total_pages)
        except Exception as error:
            import traceback
            print(f"Error: {error}")
            traceback.print_exc()
            return "Se produjo un error, vuelve a intentar más tarde."
