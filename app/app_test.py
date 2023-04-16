import unittest
from unittest.mock import patch
from datetime import datetime
from app import get_product_data

class TestGetProductData(unittest.TestCase):
    @patch('app.requests.get')
    def test_get_product_data(self, mock_get):
        mock_response = b'<html><body><h1 data-testid="heading-product-title">Product Title</h1></body></html>'
        mock_get.return_value.content = mock_response
        url = 'http://example.com/product'
        result = get_product_data(url)
        self.assertIsNotNone(result)
        self.assertIn('_id', result)
        self.assertIsInstance(result['_id'], str)
        self.assertEqual(result['title'], 'Product Title')
        self.assertEqual(result['url'], url)
        self.assertIsInstance(result['timestamp'], datetime)
