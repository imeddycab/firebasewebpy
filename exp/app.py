import web
from controllers.index import Index as Index
from controllers.personas.lista_personas import ListaPersonas as ListaPersonas
from controllers.personas.insertar_persona import InsertarPersonas as InsertarPersonas

# Configuración de rutas
urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas',
    '/insertar_persona', 'InsertarPersonas'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run() # Inicializa el servidor web