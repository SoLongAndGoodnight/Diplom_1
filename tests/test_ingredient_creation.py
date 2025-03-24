import allure
import pytest
from stellar_burger.ingredient import Ingredient


@allure.feature("Ingredient")
class TestIngredient:
    @allure.title("Ingredient get_name()")
    @pytest.mark.parametrize("name", ["Ketchup", "Patty"])
    def test_get_name(self, name):
        ingredient = Ingredient("ingredient_type", name, 1)
        assert ingredient.get_name() == name

    @allure.title("Ingredient get_price()")
    @pytest.mark.parametrize("price", [
        50, 200
    ])
    def test_get_price(self, price):
        ingredient = Ingredient("ingredient_type", "name", price)
        assert ingredient.get_price() == price

    @allure.title("Ingredient get_type()")
    @pytest.mark.parametrize("ingredient_type", [
        "sauce",
        "filling",
    ])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "name", 1)
        assert ingredient.get_type() == ingredient_type
