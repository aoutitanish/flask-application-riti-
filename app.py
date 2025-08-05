from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Global list to store submitted numbers
submitted_numbers = []

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "POST":
        try:
            number = int(request.json.get("number"))
            submitted_numbers.append(number)
            return jsonify({"status": "success"}), 200
        except (ValueError, TypeError):
            return jsonify({"status": "error", "message": "Invalid input"}), 400
    elif request.method == "GET":
        return jsonify(submitted_numbers)

if __name__ == "__main__":
    app.run(debug=True)

