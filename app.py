from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
            "name": "Chair",
            "price": 15.99
            },
            {
            "name": "Desk",
            "price": 79.99
            },
            {
            "name": "Laptop",
            "price": 1999.99
            }
        ]
        
    }
]

@app.get('/store') # 'http://127.0.0.1:5000/store'
def get_stores():
    return {"stores": stores}
