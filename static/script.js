document.querySelector("form").onsubmit = async function(e) {
    e.preventDefault();
    let formData = new FormData(this);
    let response = await fetch("/extract", { method: "POST", body: formData });
    let result = await response.json();
    let outputDiv = document.getElementById("output");

    if (result.ingredients.length > 0) {
        outputDiv.innerHTML = "<h2>Extracted Ingredients:</h2><ul>" + 
            result.ingredients.map(ing => `
                <li>
                    <img src="{{ url_for('static', filename='images/${ing.ingredient.toLowerCase().replace(/ /g, '_')}.png') }}" alt="${ing.ingredient}">
                    ${ing.quantity} - ${ing.ingredient}
                </li>`).join("") + "</ul>";
        outputDiv.classList.add('active');
    } else {
        outputDiv.innerHTML = "<p>No ingredients found.</p>";
        outputDiv.classList.add('active');
    }
};
