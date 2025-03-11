import re
import requests
from bs4 import BeautifulSoup

# Ingredient Extraction Logic
def extract_ingredients(text):
    pattern = r"(\d+\s*(?:[\/\d.]+)?\s*(?:cup|cups|tbsp|tablespoon|tablespoons|tsp|teaspoon|teaspoons|g|gram|grams|kg|kilogram|kilograms|ml|milliliter|milliliters|l|liter|liters|oz|ounce|ounces|lb|pound|pounds|pinch|dash|clove|cloves|slice|slices)?)\s+([a-zA-Z\s-]+)"
    matches = re.findall(pattern, text, re.IGNORECASE)

    ingredients = []
    for match in matches:
        quantity, ingredient = match
        ingredients.append({"quantity": quantity.strip(), "ingredient": ingredient.strip()})

    return ingredients

# Extract and Filter Ingredients from a URL
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract content from known ingredient sections
        ingredient_sections = soup.find_all(class_=re.compile(r'(ingredient|recipe-ingredient)', re.IGNORECASE)) or \
                              soup.find_all(['ul', 'ol'])

        extracted_text = ""
        for section in ingredient_sections:
            for li in section.find_all('li'):
                extracted_text += li.get_text() + " "

        # Clean extracted text
        extracted_text = re.sub(r"\s+", " ", extracted_text.strip())

        return extracted_text if extracted_text else "No specific ingredient section found."

    except Exception as e:
        return f"Error extracting text from URL: {str(e)}"
