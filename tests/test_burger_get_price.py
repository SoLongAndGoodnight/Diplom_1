import allure


@allure.feature("Burger")
class TestBurgerGetPrice:
    @allure.story("Расчёт цены бургера")
    def test_get_price(self, burger, mock_bun, mock_ingredient1, mock_ingredient2):
        with allure.step("Устанавливаем булочку"):
            burger.set_buns(mock_bun)

        with allure.step("Добавляем ингредиенты"):
            burger.add_ingredient(mock_ingredient1)
            burger.add_ingredient(mock_ingredient2)

        with allure.step("Рассчитываем ожидаемую цену"):
            expected_price = (100 * 2) + 200 + 50  # Две булочки + ингредиенты

        with allure.step("Проверяем, что метод get_price() возвращает правильную цену"):
            assert burger.get_price() == expected_price
