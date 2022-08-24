from api import create_app
from settings import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DATABASE

app = create_app(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DATABASE)

app.run(debug = True)