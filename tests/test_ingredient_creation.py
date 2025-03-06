import pytest
from ingredient import Ingredient

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("sauce", "Ketchup", 50),
    ("filling", "Patty", 200)
])
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
    assert ingredient.get_type() == ingredient_type
