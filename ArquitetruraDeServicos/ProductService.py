from flask import Flask, jsonify

app_products = Flask(__name__)

products = [
    {"id":1, "name":"Notebook", "price":4500},
    {"id":2, "name":"Teclado", "price":250}
]

@app_products.route('/produtos', methods=['GET'])
def listProducts():
    return jsonify(products)

@app_products.route('/produtos/<int:id>', methods=['GET'])
def getProduct(id):
    product = next((p for p in products if p["id"]==id), None)
    return jsonify(product) if product else ("produto nao encontrado!", 404)

if __name__ == '__main__':
    app_products.run(port=5001)