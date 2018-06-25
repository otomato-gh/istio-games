from flask import Flask
import requests
app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return 'Healthy'

@app.route('/')
def hello_world():
    return 'We are front! Check out backends: <a href="/backends"> here </a>'

@app.route('/backends')
def backends():
    backends = {}
    out = "Backends List:<br>"
    for be in ['aleph', 'beth']:
        r = requests.get("http://"+be+"/version")
        if r.status_code != 500:
            version = r.text
            out += "Backend: " + be + "| Version:" + version + "<br>"
    return out

app.run(host='0.0.0.0', port=33333, debug=True)