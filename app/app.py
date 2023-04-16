import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Connect to MongoDB using the root user and password
client = MongoClient('mongodb://root:password@localhost:27017/')

# Select the database
db = client['product_database']

# Select the collection
collection = db['products']

# Set expiration time for cache (1 hour)
cache_expiration = timedelta(hours=1)

# Define a function to scrape product data from a URL
def get_product_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title_element = soup.find('h1', {'class': 'product-name'})
    title = title_element.get_text() if title_element else None

    image_element = soup.find('img', {'class': 'js-main-image'})
    image = image_element['src'] if image_element else None

    price_element = soup.find('span', {'class': 'price-current'})
    price = price_element.get_text() if price_element else None

    description_element = soup.find('div', {'class': 'product-description'})
    description = description_element.get_text() if description_element else None

    data = {
        '_id': str(ObjectId()),
        'title': title,
        'image': image,
        'price': price,
        'description': description,
        'url': url,
        'timestamp': datetime.utcnow()
    }

    return data

# Define a function to check if cached data is still valid
def is_cached_data_valid(data):
    now = datetime.utcnow()
    timestamp = data.get('timestamp')
    if not timestamp:
        return False
    return (now - timestamp) < cache_expiration

# Define the API endpoint
@app.route('/products', methods=['POST'])
def get_product():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided.'}), 400
    
     # Check if product data is already in cache
    cached_data = collection.find_one({'url': url})
    if cached_data and is_cached_data_valid(cached_data):
        # Convert the ObjectId to a string representation before returning as JSON
        cached_data['_id'] = str(cached_data['_id'])
        return jsonify(cached_data)
    
    # Scrape product data from URL
    product_data = get_product_data(url)
    
    # Cache product data in database
    collection.replace_one({'url': url}, product_data, upsert=True)
    
    return jsonify(product_data)

if __name__ == '__main__':
    app.run()
