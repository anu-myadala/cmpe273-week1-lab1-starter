# CMPE 273 Lab 1: Distributed Echo Service

## Goal
Build a tiny, locally distributed system with two services that communicate over the network, include basic logging, and demonstrate independent failure.

## How to Run Locally

### 1. Prerequisites
- Python 3.10+
- Flask (`pip install flask requests`)

### 2. Start Service A (Echo Server)
Open a terminal and run:
```bash
cd python-http
# source venv/bin/activate  # (If using virtualenv)
python3 service_a.py
Runs on localhost:8080

### 3. Start Service B (Client)
Open a second terminal and run:

Bash

cd python-http
# source venv/bin/activate  # (If using virtualenv)
python3 service_b.py
Runs on localhost:8081

## Test Results
## Success Case
Running curl "http://127.0.0.1:8081/call-echo?msg=hello" returns a combined response from both services.
message:
anumyad@Anus-Laptop cmpe273-week1-lab1-starter % curl "http://127.0.0.1:8081/call-echo?msg=hello"
{
  "service_a_response": {
    "echo": "hello"
  },
  "service_b_message": "Hello from B"
}

## Failure Case
When Service A is stopped, Service B detects the timeout/connection error and returns HTTP 503.
message:
anumyad@Anus-Laptop cmpe273-week1-lab1-starter % curl -v "http://127.0.0.1:8081/call-echo?msg=hello"
*   Trying 127.0.0.1:8081...
* Connected to 127.0.0.1 (127.0.0.1) port 8081
> GET /call-echo?msg=hello HTTP/1.1
> Host: 127.0.0.1:8081
> User-Agent: curl/8.4.0
> Accept: */*
> 
< HTTP/1.1 503 SERVICE UNAVAILABLE
< Server: Werkzeug/3.1.5 Python/3.14.3
< Date: Thu, 05 Feb 2026 03:02:02 GMT
< Content-Type: application/json
< Content-Length: 42
< Connection: close
< 
{
  "error": "Service A is unavailable"
}
* Closing connection

## What makes this distributed?
Even though both services run on the same local machine, they operate as two distinct processes with separate memory spaces (Process IDs). They do not share state or memory; they communicate strictly over a network protocol (HTTP) via different ports (8080 and 8081). Because Service B acts as an independent client that must handle the network unavailability of Service A (as shown in the failure test), this demonstrates the core characteristics of a distributed system: independent failure and network-based communication.
