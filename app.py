from flask import Flask, jsonify, request
import json
app = Flask(__name__)

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

@app.route('/dev/<int:id>', methods=['GET'])
def desenvolvedor(id):
    try:
        response = desenvolvedores[id]
    except IndexError:
        mensagem = 'Dev com id {} não existe'.format(id)
        response = {'status':'erro', 'mensagem': mensagem}
    except Exception:
        mensagem = 'Erro desconhecido'
        response = {'status': 'erro', 'mensagem': mensagem}
    return jsonify(response)

@app.route('/dev/<int:id>', methods=['PUT'])
def changeDev(id):
    dados = json.loads(request.data)
    desenvolvedores[id] = dados
    return jsonify(dados)

@app.route('/dev/<int:id>', methods=['DELETE'])
def deleteDev(id):
    desenvolvedores.pop(id)
    return jsonify({'status':'sucesso','mensagem':'registro excluido'})

@app.route('/dev', methods=['GET'])
def listar():
    return jsonify(desenvolvedores)

@app.route('/dev', methods=['POST'])
def adicionar():
    dados = json.loads(request.data)
    dados['id'] = len(desenvolvedores)
    desenvolvedores.append(dados)
    return jsonify({'status':'sucesso','mensagem':'registro inserido'})

if __name__ == '__main__':
    app.run(debug=True)