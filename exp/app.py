import web
from controllers.index import Index as Index
from controllers.personas.lista_personas import ListaPersonas as ListaPersonas

# Configuración de rutas
urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas'
)

app = web.application(urls, globals())
render = web.template.render('views', base='master')

class Index:
    def GET(self):
        return render.index()

class ListaPersonas:
    def GET(self):
        return render.lista_personas()

if __name__ == "__main__":
    app.run() # Inicializa el servidor web