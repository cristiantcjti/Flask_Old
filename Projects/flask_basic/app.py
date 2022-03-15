from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


stores = [
    {
        'name': 'store1',
        'items': [
            {
                'name': 'My item',
                'price': 20.00
            }
        ]    
    }
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
            'name': request_data['name'],
            'items': []
        }
    stores.append(new_store)
    return jsonify(new_store)



@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        
        return jsonify({'message': 'there is no store'})
    


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':  request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
            
    return jsonify({'message': 'Store not found'})



@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
        
        return jsonify({'message': 'there is no items'})

app.run(port=5000)

