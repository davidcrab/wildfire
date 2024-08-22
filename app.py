import sys
import os
from flask import Flask, request, jsonify

from run_transformer import run_transformer  # Now this import should work
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Less than 25 minutes. more endpoints to come '

@app.route('/data', methods=['POST'])
def process_data():
    data = request.json
    response = {
        "message": "Data received successfully!",
        "received_data": data
    }
    return jsonify(response)

@app.route('/run_transformer', methods=['POST'])
def run_transformer_endpoint():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt or len(prompt) > 100:
        return jsonify({"error": "Invalid or too long prompt"}), 400
    
    try:
        # Directly call the function from the imported script
        output = run_transformer(prompt)
        return jsonify({"output": output})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)