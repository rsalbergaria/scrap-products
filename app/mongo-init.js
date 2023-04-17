db = db.getSiblingDB('product_database');

db.products.insertMany([
  {
    title: 'Product 1',
    image: 'https://example.com/product1.jpg',
    price: 9.99,
    description: 'This is product 1.',
    url: 'https://example.com/product1'
  },
  {
    title: 'Product 2',
    image: 'https://example.com/product2.jpg',
    price: 19.99,
    description: 'This is product 2.',
    url: 'https://example.com/product2'
  },
  {
    title: 'Product 3',
    image: 'https://example.com/product3.jpg',
    price: 29.99,
    description: 'This is product 3.',
    url: 'https://example.com/product3'
  }
]);
