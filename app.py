from flask import Flask, render_template, request

app = Flask(__name__)

def generate_recipe(ingredients: str) -> str:
    return f"""Recipe Idea for: {ingredients}

1. Prepare the ingredients.
2. Heat a pan and add a little oil.
3. Cook the ingredients together for 10–15 minutes.
4. Add salt, pepper, or simple spices.
5. Serve warm.

AI Tip: You can adjust the recipe depending on what you have at home.
"""

@app.route("/", methods=["GET", "POST"])
def home():
    recipe = None
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        recipe = generate_recipe(ingredients)
    return render_template("index.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)