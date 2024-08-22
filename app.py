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

# @app.route('/run_transformer', methods=['GET'])
# def run_transformer_endpoint():
#     # Activate the virtual environment and run the script
#     command = [
#         'bash', '-c',
#         'source /Users/davidcrabtree/projects/tensorflow-metal/venv-metal-py310/bin/activate && python /Users/davidcrabtree/projects/tensorflow-metal/transformer_metal.py'
#     ]
    
#     try:
#         # Run the command and capture the output
#         result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
#         # Check for errors
#         if result.returncode != 0:
#             return jsonify({"error": result.stderr}), 500
        
#         # Return the script's output as the response
#         return jsonify({"output": result.stdout})
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/run_gpt2', methods=['POST'])
# def run_gpt2():
#     # Get the prompt from the POST request body
#     data = request.json
#     prompt = data.get("prompt", "")

#     if not prompt:
#         return jsonify({"error": "No prompt provided"}), 400
    
#     # Activate the virtual environment and run the script with the prompt
#     command = [
#         'bash', '-c',
#         f'source /Users/davidcrabtree/projects/tensorflow-metal/venv-metal-py310/bin/activate && python /Users/davidcrabtree/projects/tensorflow-metal/gpt2_external.py "{prompt}"'
#     ]
    
#     try:
#         # Run the command and capture the output
#         result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
#         # Check for errors
#         if result.returncode != 0:
#             return jsonify({"error": result.stderr}), 500
        
#         # Return the script's output as the response
#         return jsonify({"output": result.stdout})
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)