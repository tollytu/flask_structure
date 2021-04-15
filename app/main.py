from flask import Flask
from flask_restplus import Api

from app.utils import exampleupdate
from app import controller

example_app = Flask(__name__)
# 设置参数错误回显
example_app.config['BUNDLE_ERRORS'] = True

authorizations = {
    "ApiKeyAuth": {
        "type": "apiKey",
        "in": "header",
        "name": "Token"
    }
}

api = Api(example_app, prefix="/api", doc="/api/doc", title='example backend API', authorizations=authorizations,
          description='example', security="ApiKeyAuth", version="2.2")

api.add_namespace(controller.example_ns)
api.add_namespace(controller.user_ns)

exampleupdate.arl_update()

if __name__ == '__main__':
    example_app.run(debug=True, port=5018, host="0.0.0.0")
