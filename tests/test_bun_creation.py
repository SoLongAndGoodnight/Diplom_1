import pytest
import allure
from stellar_burger.bun import Bun


@allure.feature("Bun")
class TestBun:
    @allure.title("Создание булочки")
    def test_bun_creation(self):
        assert Bun("name", 1)

    @allure.title("Проверяем имя булочки")
    @pytest.mark.parametrize("name", [
        "Black Bun",
        "White Bun",
        "Red Bun",
    ])
    def test_get_name(self, name):
        bun = Bun(name, 1)

        assert bun.get_name() == name

    @allure.title("Проверяем цену булочки")
    @pytest.mark.parametrize("price", [
        100, 200, 300
    ])
    def test_get_price(self, price):
        bun = Bun("name", price)

        assert bun.get_price() == price
