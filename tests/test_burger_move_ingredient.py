import allure


@allure.feature("Burger")
@allure.story("Перемещение ингредиента")
def test_move_ingredient(burger, mock_ingredient1, mock_ingredient2):
    with allure.step("Добавляем два ингредиента"):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

    with allure.step("Меняем местами ингредиенты"):
        burger.move_ingredient(0, 1)

    with allure.step("Проверяем порядок ингредиентов"):
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1
