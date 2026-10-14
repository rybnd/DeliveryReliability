import sys
import time
import urllib.request

def check_endpoint(url="http://localhost:8080", timeout=5):
    print(f"Checking service health at {url}...")
    try:
        start_time = time.time()
        req = urllib.request.urlopen(url, timeout=timeout)
        latency = time.time() - start_time
        if req.status == 200:
            print(f"SUCCESS: Service is healthy. Response time: {latency:.4f}s")
            sys.exit(0)
        else:
            print(f"FAILURE: Received status code {req.status}")
            sys.exit(1)
    except Exception as e:
        print(f"FAILURE: Could not connect to service. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_endpoint()