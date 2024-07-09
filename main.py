import requests
import time

codespace_url = "https://studious-space-tribble-74w54g55p94hpr96.github.dev/"

while True:
    try:
        response = requests.get(codespace_url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        print(f"Sent request to {codespace_url} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    except requests.RequestException as e:
        print(f"Error sending request: {e}")

    time.sleep(600)  # Sleep for 30 minutes
