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
    text = request.form.get("text", "").strip()
    url = request.form.get("url", "").strip()
    uploaded_file = request.files.get("file")

    # Extract content based on user input
    if url:
        try:
            text = extract_text_from_url(url)
        except Exception as e:
            return jsonify({"error": f"Error extracting from URL: {str(e)}"}), 400

    elif uploaded_file:
        try:
            text = uploaded_file.read().decode("utf-8")
        except Exception as e:
            return jsonify({"error": f"Error reading file: {str(e)}"}), 400

    if not text:
        return jsonify({"error": "No valid input provided"}), 400

    # Extract ingredients
    ingredients = extract_ingredients(text)

    # Handle empty or invalid extraction results
    if not ingredients:
        return jsonify({"error": "No ingredients found or invalid input provided."}), 404

    return jsonify({"ingredients": ingredients})

# Vercel compatibility for serverless functions
def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    app.run(debug=True)
