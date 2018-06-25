from flask import Flask
import requests
app = Flask(__name__)

def getForwardHeaders(request):
    headers = {}

    user_cookie = request.cookies.get("user")
    if user_cookie:
        headers['Cookie'] = 'user=' + user_cookie

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            #print "incoming: "+ihdr+":"+val

    return headers

@app.route('/healthz')
def healthz():
    return 'Healthy'

@app.route('/')
def hello_world():
    return 'We are front! Check out backends: <a href="/backends"> here </a>'

@app.route('/backends')
def backends():
    headers = getForwardHeaders(request)
    backends = {}
    out = "Backends List:<br>"
    for be in ['aleph', 'beth']:
        r = requests.get("http://"+be+"/version", headers=headers)
        if r.status_code != 500:
            version = r.text
            out += "Backend: " + be + "| Version:" + version + "<br>"
    return out

app.run(host='0.0.0.0', port='80', debug=True)