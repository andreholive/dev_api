from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':0,
        'nome':'Andre',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id':1,
        'nome':'Daniela',
        'habilidades': ['Java', 'Spring Boot']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Dev com id {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido'}

class ListaDesenvolvedor(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        dados['id'] = len(desenvolvedores)
        desenvolvedores.append(dados)
        return {'status': 'sucesso', 'mensagem': 'registro inserido'}

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedor, '/dev')
api.add_resource(Habilidades, '/habilidades')

if __name__ == '__main__':
    app.run(debug=True)