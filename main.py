from flask import Flask, jsonify, request, abort
from datetime import datetime
import json

app = Flask(__name__)

# use a robust data structure or database in a real-world scenario
message_queue = []

# post receives messages using requests
@app.route('/post', methods=['POST'])
def post_message():
    json_data = request.get_json()
    message = json_data['message']
    if message:
        #timestamp = datetime.utcnow().isoformat()
        #message_queue.append({'timestamp': timestamp, 'message': message})
        message_queue.append({'message': message})
        return jsonify({'status': 'success', 'message': 'Message added to the queue'})
        with open("message_queue.json") as f:
            json.dump(message_queue, f, indent=None)
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request'})

@app.route('/get', methods=['GET'])
def throw_messages():
    if len(message_queue) >= 3:
        return jsonify(message_queue[-3:])
    elif len(message_queue) < 3 and len(message_queue) > 0:
        return jsonify(message_queue)
    else:
        abort(404, description="Not enough messages in the queue")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4231)

