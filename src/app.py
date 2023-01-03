from flask import Flask, jsonify, request, json


app = Flask(__name__)

#lista en Python
todos = [ 
    { 'label': 'My first task', 'done' : False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    text_json = jsonify(todos) #Transforma la lista Python en JSON
    return text_json
    
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body) #Transforma el texto JSON a Python
    print("Incoming request with the following body", request_body, decoded_object)
    todos.append(decoded_object) #Añade el objeto decodificado en la lista
    return jsonify(todos)

@app.route('/todos/<position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(int(position)) #Elimina elemnto por posicion
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug= True)