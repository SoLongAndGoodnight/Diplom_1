import allure


@allure.feature("Database")
@allure.story("Доступные булочки")
def test_available_buns(database):
    with allure.step("Получаем список доступных булочек"):
        buns = database.available_buns()

    with allure.step("Проверяем количество булочек"):
        assert len(buns) == 3

    with allure.step("Проверяем названия булочек"):
        assert "black stellar_burger" in [bun.get_name() for bun in buns]
        assert "white stellar_burger" in [bun.get_name() for bun in buns]
        assert "red stellar_burger" in [bun.get_name() for bun in buns]


