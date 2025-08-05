from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Global list to store submitted numbers
submitted_numbers = []

@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/")
def root():
    return render_template("home.html")

@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "POST":
        try:
            number = int(request.form.get("number"))
            submitted_numbers.append(number)
            return f"Number {number} added successfully!", 200
        except (ValueError, TypeError):
            return "Invalid input. Please enter a valid number.", 400
    elif request.method == "GET":
        return jsonify(submitted_numbers)

if __name__ == "__main__":
    app.run(debug=True)
