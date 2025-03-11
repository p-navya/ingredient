from flask import Flask, request, jsonify, render_template
from utils.extractor import extract_ingredients, extract_text_from_url

app = Flask(__name__)

# Home page (Frontend)
@app.route("/")
def home():
    return render_template("index.html")

# API Endpoint for text extraction
@app.route("/extract", methods=["POST"])
def extract():
    text = request.form.get("text", "")
    url = request.form.get("url", "")
    uploaded_file = request.files.get("file")

    # Extract content based on user input
    if url:
        text = extract_text_from_url(url)
    elif uploaded_file:
        try:
            text = uploaded_file.read().decode("utf-8")
        except Exception as e:
            return jsonify({"error": f"Error reading file: {str(e)}"}), 400

    if not text:
        return jsonify({"error": "No valid input provided"}), 400

    ingredients = extract_ingredients(text)
    return jsonify({"ingredients": ingredients})

if __name__ == "__main__":
    app.run(debug=True)
