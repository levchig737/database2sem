import pytest
from mongomock import MongoClient
from main import ProductQueryApp

@pytest.fixture
def mock_mongo_client():
    return MongoClient()

@pytest.fixture
def mock_collection(mock_mongo_client):
    database = mock_mongo_client['test_database']
    collection = database['test_collection']
    return collection

def test_get_product_names_by_category(mock_collection):
    app = ProductQueryApp(mock_collection)
    mock_collection.insert_one({"product_name": "Product1", "category": "TestCategory"})
    mock_collection.insert_one({"product_name": "Product2", "category": "TestCategory"})
    mock_collection.insert_one({"product_name": "Product3", "category": "TestCategory"})

    result = app.get_product_names_by_category('TestCategory')
    assert result == ['Product1', 'Product2', 'Product3']

def test_get_product_names_by_category_empty_result(mock_collection):
    app = ProductQueryApp(mock_collection)
    result = app.get_product_names_by_category('NonExistingCategory')
    assert result == []

def test_get_product_characteristics_by_category(mock_collection):
    app = ProductQueryApp(mock_collection)
    mock_collection.insert_one({"product_name": "Product1", "category": "TestCategory", "characteristics": {"color": "Red"}})

    result = app.get_product_characteristics_by_category('TestCategory')
    assert "Product1" in result
    assert "color" in result[0]["characteristics"]

# Добавим еще тесты для других методов

def test_get_products_by_customer(mock_collection):
    app = ProductQueryApp(mock_collection)
    mock_collection.insert_one({"product_name": "Product1", "customer_info": {"customer_name": "Customer1"}})

    result = app.get_products_by_customer('Customer1')
    assert "Product1" in result
    assert "price" in result[0]

def test_get_products_by_color(mock_collection):
    app = ProductQueryApp(mock_collection)
    mock_collection.insert_one({"product_name": "Product1", "characteristics": {"color": "Blue"}})

    result = app.get_products_by_color('Blue')
    assert "Product1" in result
    assert "manufacturer" in result[0]
    assert "price" in result[0]

# Тесты для негативных сценариев
def test_get_product_names_by_category_invalid_category(mock_collection):
    app = ProductQueryApp(mock_collection)
    with pytest.raises(ValueError):
        app.get_product_names_by_category(None)

def test_get_product_names_by_category_invalid_type(mock_collection):
    app = ProductQueryApp(mock_collection)
    with pytest.raises(TypeError):
        app.get_product_names_by_category(123)

# Добавим еще тесты для других негативных сценариев

# Запуск тестов с помощью pytest
# Запустите этот файл с помощью команды `pytest имя_вашего_файла.py` в командной строке.
# Например: `pytest test_product_query_app.py`
