from flask import Flask, request, jsonify
import logging
import time

app = Flask(__name__)

# Basic Request Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/echo', methods=['GET'])
def echo():
    start_time = time.time()
    msg = request.args.get('msg', '')
    # Simulate processing (optional)
    response = {"echo": msg}
    
    # Log the request
    latency = time.time() - start_time
    app.logger.info(f"Service: A | Endpoint: /echo | Status: 200 | Latency: {latency:.4f}s")
    
    return jsonify(response)

if __name__ == '__main__':
    # Run on port 8080
    app.run(port=8080, debug=True)