from flask import Flask, request, jsonify

app_orders = Flask(__name__)
orders = []

@app_orders.route('/pedidos', methods=['POST'])
def createOrder():
    data = request.json
    orders.append(data)
    return jsonify({"mensagem": "pedido criado com sucesso!", "pedido": data}), 201

@app_orders.route('/pedidos', methods=['GET'])
def listOrders():
    return jsonify(orders)

if __name__ == '__main__':
    app_orders.run(port=5002)