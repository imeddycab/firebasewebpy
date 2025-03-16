import web
from controllers.index import Index as Index
from controllers.personas.lista_personas import ListaPersonas as ListaPersonas
from controllers.personas.insertar_persona import InsertarPersona as InsertarPersona
from controllers.personas.ver_persona import VerPersona as VerPersona
from controllers.personas.buscar_persona import BuscarPersona as BuscarPersona
from controllers.personas.editar_persona import EditarPersona as EditarPersona
from controllers.personas.eliminar_persona import EliminarPersona as EliminarPersona

# Configuración de rutas
urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas',
    '/insertar_persona', 'InsertarPersona',
    '/buscar_persona', 'BuscarPersona',
    '/persona/(.*)', 'VerPersona',
    "/editar_persona/(.*)", "EditarPersona",
    "/eliminar_persona/(.*)", "EliminarPersona",
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run() # Inicializa el servidor web
