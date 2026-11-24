# Self Review: Recipe Directory

I was the odd one out in the peer-review pairing, so this is a self-review against the task requirements.

## Does it meet the user stories?
- Recipes have a **name** (`name text`) - yes
- Recipes have an **average cooking time in minutes** (`cooking_time int`) - yes
- Recipes have a **rating from 1 to 5** (`rating int CHECK (rating BETWEEN 1 AND 5)`) - yes

## Was it test-driven?
Yes. For both `Recipe` and `RecipeRepository` I wrote the tests first and ran them to see them fail (red: `ModuleNotFoundError`), then wrote the code to make them pass (green). All 13 tests pass (`python -m pytest`).

## Design decisions
- **Schema:** designed with the Single Table Design Recipe (`recipes_table_design.md`).
- **Rating validation in the database:** the `CHECK` constraint means the database rejects ratings outside 1-5, even if the Python code has a bug.
- **Model vs repository:** `Recipe` only holds data; `RecipeRepository` is the only class that contains SQL.
- **Safe SQL:** `find` uses a `%s` parameter instead of string formatting, which protects against SQL injection.
- **Predictable results:** `all()` uses `ORDER BY id`, so tests can rely on the order.
- **Repeatable tests:** each test re-seeds the database from `seeds/recipes.sql`, so tests don't affect each other.

## What I would improve
1. `find` with an id that doesn't exist raises an `IndexError`. It should return `None` (or raise a clear error), with a test for that case.
2. The starter's `Artist` files and tests are still in the project. They could be removed to keep it focused.
3. Add `create` and `delete` methods (not required for this task) to cover full CRUD, as I did in `music_library`.
4. Add a test that tries to insert a rating of 6 and checks the database rejects it.

## What I learned
Following red-green TDD made each step small and safe, and putting validation in the schema means bad data can't get in, whatever the code does.
