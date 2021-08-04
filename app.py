from flask import Flask

from api.blueprints.analytics.analytics_api import ANALYTICS_BLUEPRINT

from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/')
def root():
    return 'default'


if __name__ == '__main__':
    app.register_blueprint(ANALYTICS_BLUEPRINT)
    app.run()
