from flask import Flask, jsonify, request

app = Flask(__name__)

funcionarios = [
    {
        'id':1,
        'nome': 'Karlos',
        'email': 'teste@teste.com',
        'telefone': '123456789'
    },
 
]

@app.route('/funcionarios', methods=['GET'])
def get_all_funcionarios():
    return jsonify(funcionarios)

@app.route('/funcionarios/<int:id>', methods=['GET'])
def get_one_funcionario(id):
    for funcionario_buscado in funcionarios:
        if funcionario_buscado.get('id') == id:
            return jsonify(funcionario_buscado)
        
@app.route('/funcionarios/<int:id>', methods=['PUT'])
def update_funcionario(id):
    funcionario_atualizado = request.get_json()
    for indice,funcionario in enumerate(funcionarios):
        if funcionario.get('id') == id:
            funcionarios[indice].update(funcionario_atualizado)       
            return jsonify(funcionarios[indice])

@app.route('/funcionarios', methods=['POST'])
def insert_funcionario():
    novo_funcionario = request.get_json()
    funcionarios.append(novo_funcionario)
    return jsonify(funcionarios)

@app.route('/funcionarios/<int:id>', methods=['DELETE'])
def delete_funcionario(id):
    for indice, funcionario in enumerate(funcionarios):
        if funcionario.get('id') == id:
            del funcionarios[indice]

    return jsonify(funcionarios)   
     
app.run(port=8080,host='localhost',debug=True)