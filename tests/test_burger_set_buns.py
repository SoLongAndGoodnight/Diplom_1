import allure


@allure.feature("Burger")
@allure.story("Удаление ингредиента")
def test_set_buns(burger, mock_bun):
    with allure.step("Устанавливаем булочку в бургер"):
        burger.set_buns(mock_bun)

    with allure.step("Проверяем, что булочка установлена корректно"):
        assert burger.bun == mock_bun
