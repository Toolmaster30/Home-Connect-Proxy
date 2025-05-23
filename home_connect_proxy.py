from flask import Flask, request, Response
import requests

app = Flask(__name__)

TOKEN_FILE = "/config/home_connect_access.txt"
HOME_CONNECT_API_BASE = "https://api.home-connect.com"

def get_access_token():
    with open(TOKEN_FILE, "r") as f:
        return f.read().strip()

@app.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    token = get_access_token()
    url = f"{HOME_CONNECT_API_BASE}/{path}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    if request.method == "GET":
        resp = requests.get(url, headers=headers, params=request.args)
    elif request.method == "POST":
        resp = requests.post(url, headers=headers, json=request.json)
    elif request.method == "PUT":
        resp = requests.put(url, headers=headers, json=request.json)
    elif request.method == "DELETE":
        resp = requests.delete(url, headers=headers)
    else:
        return Response("Method not allowed", status=405)

    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
