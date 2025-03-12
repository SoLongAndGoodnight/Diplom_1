import pytest
import allure
from stellar_burger.bun import Bun


@pytest.mark.parametrize("name, price", [
    ("Black Bun", 100),
    ("White Bun", 200),
    ("Red Bun", 300)
])
@allure.feature("Bun")
@allure.story("Создание булочки")
def test_bun_creation(name, price):
    with allure.step("Создаем булочку"):
        bun = Bun(name, price)

    with allure.step("Проверяем имя булочки"):
        assert bun.get_name() == name

    with allure.step("Проверяем цену булочки"):
        assert bun.get_price() == price
