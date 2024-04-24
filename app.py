from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "faris": {
        "balance": 1000
    },
    "refan": {
        "balance": 2000
    }
}

@app.route('/topup', methods=['POST'])
def topup():
    data = request.get_json()
    username = data.get('username')
    amount = data.get('amount')

    if username not in users:
        return jsonify({'message': 'User not found'}), 404

    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'message': 'Invalid amount'}), 400

    if amount <= 0:
        return jsonify({'message': 'Amount must be greater than 0'}), 400

    users[username]['balance'] += amount

    return jsonify({'message': 'Top-up successful', 'balance': users[username]['balance']}), 200

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    username = data.get('username')
    price = data.get('price')

    if username not in users:
        return jsonify({'message': 'User not found'}), 404

    try:
        price = float(price)
    except ValueError:
        return jsonify({'message': 'Invalid price'}), 400

    if price <= 0:
        return jsonify({'message': 'Price must be greater than 0'}), 400

    balance = users[username]['balance']
    if balance < price:
        return jsonify({'message': 'Insufficient balance'}), 400

    users[username]['balance'] -= price

    transaction_detail = {
        'username': username,
        'price': 100,
        'balance_after_transaction': users[username]['balance']
    }

    return jsonify({'message': 'Transaction successful', 'transaction_detail': transaction_detail}), 200

if __name__ == '__main__':
    app.run(debug=True)

# kami menggunnakan aplikasi postman untuk mengubah data di dalam /calculate dan,top-pup