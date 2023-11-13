from flask import Flask, jsonify, request, abort
from datetime import datetime
import json
import redis

redis_client = redis.Redis()

app = Flask(__name__)

# store messages in redis for independent recoverable storage
#redis_client.rpush('message_queue', message)
#message_queue = redis_client.lrange('message_queue', -3, -1)

# post receives messages using requests
@app.route('/post', methods=['POST'])
def post_message():
    json_data = request.get_json()
    message = json_data['message']
    if message:
        redis_client.rpush('message_queue', message)
        return jsonify({'status': 'success', 'message': 'Message added to the queue'})
        with open("message_queue.json") as f:
            json.dump(message_queue, f, indent=None)
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request'})

@app.route('/get', methods=['GET'])
def throw_messages():
    message_queue = redis_client.lrange('message_queue', -3, -1)
    if len(message_queue) >= 3:
        return jsonify(message_queue)
    elif len(message_queue) > 0:
        return jsonify(message_queue)
    else:
        abort(404, description="Not enough messages in the queue")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4231)

