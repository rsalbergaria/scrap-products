# Scrap Products

Scrap Products is a Python api to receive a product url and return datas about this product;

Use products from https://www.saraiva.com.br/

## Usage

1 - Run docker to dabatabase
```bash
cd mongo 
docker compose up -d
```

2 - Run api
```bash
cd app 
pip3 install -r requirements.txt
python app.py
```

3 - Request Example:
```bash
curl --location 'http://127.0.0.1:5000/products' \
--header 'Content-Type: application/json' \
--data '{
    "url": "https://www.saraiva.com.br/cabo-micro-usb-general-electric-pro-0-9m-ultra-resistente-com-adaptador-lightning-para-iphone/p"
}'
```

