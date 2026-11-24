from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository

# Connect to the database and reset it to the seed data
connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/recipes.sql")

# Retrieve all recipes and print them
recipe_repository = RecipeRepository(connection)

print("My recipes:")
for recipe in recipe_repository.all():
    print(f" * {recipe.id} - {recipe.name} ({recipe.cooking_time} mins, rated {recipe.rating}/5)")
