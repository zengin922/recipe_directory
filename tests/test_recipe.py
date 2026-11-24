from lib.recipe import Recipe

"""
Recipe constructs with an id, name, cooking_time and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Pancakes", 20, 3)
    assert recipe.id == 1
    assert recipe.name == "Pancakes"
    assert recipe.cooking_time == 20
    assert recipe.rating == 3

"""
Two recipes with the same contents are equal
"""
def test_recipes_are_equal():
    assert Recipe(1, "Pancakes", 20, 3) == Recipe(1, "Pancakes", 20, 3)

"""
Recipe formats nicely as a string
"""
def test_recipe_formats_nicely():
    recipe = Recipe(1, "Pancakes", 20, 3)
    assert str(recipe) == "Recipe(1, Pancakes, 20, 3)"