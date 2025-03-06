import allure


@allure.feature("Database")
@allure.story("Available Buns")
def test_available_buns(database):
    with allure.step("Получаем список доступных булочек"):
        buns = database.available_buns()

    with allure.step("Проверяем количество булочек"):
        assert len(buns) == 3

    with allure.step("Проверяем названия булочек"):
        assert "black bun" in [bun.get_name() for bun in buns]
        assert "white bun" in [bun.get_name() for bun in buns]
        assert "red bun" in [bun.get_name() for bun in buns]


