from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
all() returns every recipe as a Recipe object
"""
def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    assert repository.all() == [
        Recipe(1, "Spaghetti Bolognese", 45, 5),
        Recipe(2, "Chicken Curry", 60, 4),
        Recipe(3, "Pancakes", 20, 3),
        Recipe(4, "Caesar Salad", 15, 4),
    ]

"""
find(id) returns the single recipe with that id
"""
def test_find_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    assert repository.find(2) == Recipe(2, "Chicken Curry", 60, 4)