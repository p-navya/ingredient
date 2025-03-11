from flask import Flask, request, jsonify, render_template
from utils.extractor import extract_ingredients

app = Flask(__name__)

# Home page (Frontend)
@app.route("/")
def home():
    return render_template("index.html")

# API Endpoint for extraction
@app.route("/extract", methods=["POST"])
def extract():
    text = request.form.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    ingredients = extract_ingredients(text)
    return jsonify({"ingredients": ingredients})

if __name__ == "__main__":
    app.run(debug=True)
