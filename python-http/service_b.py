from flask import Flask, request, jsonify
import requests
import logging
import time

app = Flask(__name__)

# Basic Request Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SERVICE_A_URL = "http://127.0.0.1:8080/echo"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/call-echo', methods=['GET'])
def call_echo():
    start_time = time.time()
    msg = request.args.get('msg', '')
    
    try:
        # Call Service A with a timeout of 2 seconds
        # This satisfies the requirement: "Service B must use a timeout"
        response = requests.get(SERVICE_A_URL, params={'msg': msg}, timeout=2)
        
        # If Service A returns an error (4xx or 5xx), raise an exception
        response.raise_for_status()
        
        data = response.json()
        result = {
            "service_b_message": "Hello from B",
            "service_a_response": data
        }
        status_code = 200

    except requests.exceptions.RequestException as e:
        # This satisfies: "Demonstrate failure... Service B returns 503"
        app.logger.error(f"Failed to reach Service A: {e}")
        result = {"error": "Service A is unavailable"}
        status_code = 503

    latency = time.time() - start_time
    app.logger.info(f"Service: B | Endpoint: /call-echo | Status: {status_code} | Latency: {latency:.4f}s")

    return jsonify(result), status_code

if __name__ == '__main__':
    # Run on port 8081
    app.run(port=8081, debug=True)