from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from models import get_db_connection
from chatbot import generate_response

app = Flask(__name__)

app.secret_key = 'supersecret'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
CORS(app)

# http://127.0.0.1:5000
@app.route("/")
def home():
    return "Welcome to the E-commerce Chatbot API"

# 🛍️ Search products
# http://127.0.0.1:5000/products?search=book
@app.route("/products", methods=["GET"])
def search_products():
    query = request.args.get("search", "")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE name LIKE ? OR category LIKE ?", (f"%{query}%", f"%{query}%"))
    products = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(products)


# 💬 Chatbot endpoint
# http://127.0.0.1:5000/chat
# {
#   "message": "hello"
# }

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if "history" not in session:
        session["history"] = []
    response = generate_response(user_message)
    session["history"].append({"user": user_message, "bot": response})
    return jsonify({"response": response, "session": session["history"]})

# 🧾 Chat history

@app.route("/session", methods=["GET"])
def get_session():
    return jsonify(session.get("history", []))

# 🔁 Reset conversation First make chat then check else it will show empty them 
@app.route("/reset", methods=["POST"])
def reset():
    session["history"] = []
    return jsonify({"status": "chat reset"})

if __name__ == "__main__":
    app.run(debug=True)
