from flask import Flask, request
from app.database import query_database
from app.vulnerable import deserialize_data

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the vulnerable app!"

@app.route("/query", methods=["GET"])
def query():
    user_query = request.args.get("q")
    result = query_database(user_query)  # SQL injection vulnerability
    return f"Query Result: {result}"

@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.data
    result = deserialize_data(data)  # Insecure deserialization vulnerability
    return f"Deserialized: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
