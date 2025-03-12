import allure


@allure.feature("Database")
@allure.story("Available Ingredients")
def test_available_ingredients(database):
    with allure.step("Получаем список доступных ингредиентов"):
        ingredients = database.available_ingredients()

    with allure.step("Проверяем количество ингредиентов"):
        assert len(ingredients) == 6

    with allure.step("Проверяем названия ингредиентов"):
        assert "hot sauce" in [ing.get_name() for ing in ingredients]
        assert "cutlet" in [ing.get_name() for ing in ingredients]
        assert "sausage" in [ing.get_name() for ing in ingredients]
