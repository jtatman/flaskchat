from flask import Flask, jsonify, request, abort
from datetime import datetime
import json
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['message_queue']
collection = db['messages']

# post receives messages using requests
@app.route('/post', methods=['POST'])
def post_message():
    json_data = request.get_json()
    message = json_data['message']
    if message:
        timestamp = datetime.utcnow().isoformat()
        message_data = {'timestamp': timestamp, 'message': message}
        collection.insert_one(message_data)
        return jsonify({'status': 'success', 'message': 'Message added to the queue'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request'})

@app.route('/get', methods=['GET'])
def throw_messages():
    messages = collection.find().sort('_id', -1).limit(3)
    message_queue = [{'timestamp': msg['timestamp'], 'message': msg['message']} for msg in messages]
    if len(message_queue) > 0:
        return jsonify(message_queue)
    else:
        abort(404, description="Not enough messages in the queue")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4231)
