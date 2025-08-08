from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store
users = {}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the User Management API"}), 200

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = str(data.get("id"))
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User created successfully"}), 201

# PUT update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id].update({
        "name": data.get("name"),
        "email": data.get("email")
    })
    return jsonify({"message": "User updated successfully"}), 200

# DELETE user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)