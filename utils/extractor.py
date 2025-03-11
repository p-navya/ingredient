import re

def extract_ingredients(text):
    pattern = r"(\d+\s*(?:[\/\d.]+)?\s*(?:cup|cups|tbsp|tablespoon|tablespoons|tsp|teaspoon|teaspoons|g|gram|grams|kg|kilogram|kilograms|ml|milliliter|milliliters|l|liter|liters|oz|ounce|ounces|lb|pound|pounds|pinch|dash|clove|cloves|slice|slices)?)\s+([a-zA-Z\s-]+)"
    matches = re.findall(pattern, text, re.IGNORECASE)

    ingredients = []
    for match in matches:
        quantity, ingredient = match
        ingredients.append({"quantity": quantity.strip(), "ingredient": ingredient.strip()})

    return ingredients
