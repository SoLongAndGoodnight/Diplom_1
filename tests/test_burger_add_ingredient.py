import allure


@allure.feature("Burger")
@allure.story("Добавление ингредиента")
def test_add_ingredient(burger, mock_ingredient1):
    with allure.step("Добавляем ингредиент в бургер"):
        burger.add_ingredient(mock_ingredient1)

    with allure.step("Проверяем, что ингредиент добавлен"):
        assert mock_ingredient1 in burger.ingredients
