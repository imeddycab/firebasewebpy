import web
from controllers.index import Index as Index
from controllers.personas.lista_personas import ListaPersonas as ListaPersonas
from controllers.personas.insertar_persona import InsertarPersona as InsertarPersona

# Configuración de rutas
urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas',
    '/insertar_persona', 'InsertarPersona'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run() # Inicializa el servidor web