import web
import pyrebase

render = web.template.render("views/personas", base="../master")

class InsertarPersonas:
    def GET(self):
        try:
            return render.insertar_persona()
        except Exception as error:
            message = {
                "error": error.args[0]
            }
            print(f"error: {message}")
            return message