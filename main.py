import requests
import time

github_token = os.environ['GITHUB_TOKEN']
codespace_url = "https://studious-space-tribble-74w54g55p94hpr96.github.dev/"

headers = {
    "Authorization": f"Bearer {github_token}",
    "Content-Type": "application/json"
}

while True:
    response = requests.get(codespace_url, headers=headers)
    if response.status_code == 200:
        print(f"Codespace is running at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"Error: {response.status_code}")
    time.sleep(600)  # Wait for 10 minutes
