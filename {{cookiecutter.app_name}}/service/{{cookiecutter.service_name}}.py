from flask import Flask, jsonify
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app, version='1.0', title='{{cookiecutter.service_name|title}} API',
          description='{{cookiecutter.description}} API', )


@api.route('/{{cookiecutter.service_name}}/<string:text>')
@api.doc(params={'text': 'Text'})
class {{cookiecutter.service_name|title}}(Resource):
    def get(self, text):
        message = [f'Text: {text}!']
        return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
