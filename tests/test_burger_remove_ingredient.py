import allure


@allure.feature("Burger")
class TestBurgerRemoveIngredient:
    @allure.story("Удаление ингредиента")
    def test_remove_ingredient(self, burger, mock_ingredient1, mock_ingredient2):
        with allure.step("Добавляем два ингредиента"):
            burger.add_ingredient(mock_ingredient1)
            burger.add_ingredient(mock_ingredient2)

        with allure.step("Удаляем первый ингредиент"):
            burger.remove_ingredient(0)

        with allure.step("Проверяем, что первый ингредиент удалён"):
            assert mock_ingredient1 not in burger.ingredients
            assert len(burger.ingredients) == 1
