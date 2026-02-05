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

## Failure Case
When Service A is stopped, Service B detects the timeout/connection error and returns HTTP 503.

## What makes this distributed?
Even though both services run on the same local machine, they operate as two distinct processes with separate memory spaces (Process IDs). They do not share state or memory; they communicate strictly over a network protocol (HTTP) via different ports (8080 and 8081). Because Service B acts as an independent client that must handle the network unavailability of Service A (as shown in the failure test), this demonstrates the core characteristics of a distributed system: independent failure and network-based communication.
