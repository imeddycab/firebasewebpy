import web
from models.personas import Personas

# Instancia del modelo Personas
personas_model = Personas()

# Configurar renderizado de plantillas
render = web.template.render("views/personas", base="../master")

class BuscarPersona:
    def GET(self):
        try:
            # Obtener los parámetros de búsqueda y paginación
            user_data = web.input(q="", page="1")
            user_input = user_data.q.lower()

            # Obtener la lista de personas desde el modelo
            respuesta = personas_model.lista_personas()
            lista_personas = respuesta["personas"] if respuesta["status"] == 200 else {}

            # Filtrar por ID, nombre o teléfono
            personas_filtradas = {
                id_p: p for id_p, p in lista_personas.items()
                if user_input in id_p.lower() or 
                   user_input in p.get('name', '').lower() or 
                   user_input in str(p.get('phone', ''))
            }

            # Convertir a lista para paginación
            personas_lista = list(personas_filtradas.items())

            # Manejo de paginación
            try:
                page = int(user_data.page)
                if page < 1:
                    page = 1
            except ValueError:
                page = 1

            per_page = 10  # Cantidad de elementos por página
            total = len(personas_lista)
            total_pages = (total + per_page - 1) // per_page  # Calcular total de páginas

            # Obtener elementos de la página actual
            start = (page - 1) * per_page
            end = start + per_page
            personas_paginadas = dict(personas_lista[start:end])

            # Pasar los datos a la plantilla junto con la búsqueda y la paginación
            return render.buscar_persona(personas_paginadas, user_input, page, total_pages)
        except Exception as error:
            import traceback
            print(f"Error: {error}")
            traceback.print_exc()
            return "Se produjo un error, vuelve a intentar más tarde."
