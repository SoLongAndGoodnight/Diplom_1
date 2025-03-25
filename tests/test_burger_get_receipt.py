import allure


@allure.feature("Burger")
class TestBurgerGetReceipt:
    @allure.story("Проверка ресипта")
    def test_get_receipt(self, burger, mock_bun, mock_ingredient1, mock_ingredient2):
        with allure.step("Устанавливаем булочку"):
            burger.set_buns(mock_bun)

        with allure.step("Добавляем ингредиенты"):
            burger.add_ingredient(mock_ingredient1)
            burger.add_ingredient(mock_ingredient2)

        with allure.step("Проверяем, что метод get_receipt() возвращает правильную цену"):
            assert burger.get_receipt() == (
                "(==== Mock Bun ====)\n"
                 "= filling Mock Ingredient 1 =\n"
                 "= sauce Mock Ingredient 2 =\n"
                 "(==== Mock Bun ====)\n"
                 "\n"
                 "Price: 450"
            )
