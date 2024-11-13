import requests

def test_server(url):
    try:
        response = requests.get(url)
        print(f"Server {url} responded with status code: {response.status_code}")
        print(f"Response body: {response.text}")
    except Exception as e:
        print(f"Failed to connect to {url}: {e}")

# Check both servers
test_server('http://nginx:8080')
test_server('http://nginx:8081')