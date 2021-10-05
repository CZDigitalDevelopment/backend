from chalice import Chalice

from chalicelib.routes.user_routes import users

app = Chalice(app_name="balance")

app.register_blueprint(users)
