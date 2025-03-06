import pytest
from unittest.mock import Mock
from bun import Bun
from ingredient import Ingredient
from burger import Burger
from database import Database

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100
    bun.get_name.return_value = "Mock Bun"
    return bun

@pytest.fixture
def mock_ingredient1():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 200
    ingredient.get_name.return_value = "Mock Ingredient 1"
    ingredient.get_type.return_value = "filling"
    return ingredient

@pytest.fixture
def mock_ingredient2():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 50
    ingredient.get_name.return_value = "Mock Ingredient 2"
    ingredient.get_type.return_value = "sauce"
    return ingredient

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()
