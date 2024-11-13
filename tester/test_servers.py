import requests

def check_server(url):
    try:
        response = requests.get(url)
        print(f"Server {url} responded with status code: {response.status_code}")
        print(f"Response body: {response.text}")
    except Exception as e:
        print(f"Failed to connect to {url}: {e}")

# Test both servers directly
def test_nginx_servers():
    check_server('http://nginx:8080')
    check_server('http://nginx:8081')