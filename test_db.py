import unittest
from db import create_product, ProductModel

class TestCreateProduct(unittest.TestCase):
    
    def setUp(self):
        # Створення таблиці product перед кожним тестом
        ProductModel.create_table()
        
    def tearDown(self):
        # Видалення таблиці після кожного тесту
        ProductModel.drop_table()
        
    def test_create_product(self):
        # Arrange
        name = "Test Product"
        price = 10
        
        # Act
        product = create_product(name, price)
        
        # Assert
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)
        
        # Clean up (optional)
        product.delete_instance()  # Delete the test product from the database after testing
        
if __name__ == '__main__':
    unittest.main()
