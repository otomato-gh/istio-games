from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)
app.config.from_object('settings')
app.config.from_object('version')
from flask_bootstrap import Bootstrap
Bootstrap(app)

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

@app.route('/version')
def version():
    return app.config['VERSION']

@app.route('/')
def hello_world():
    return 'We are front! Check out backends: <a href="/backends"> here </a>'

@app.route('/login', methods=['POST'])
def login():
    user = request.values.get('username')
    response = app.make_response(redirect(request.referrer))
    response.set_cookie('user', user)
    return response


@app.route('/logout', methods=['GET'])
def logout():
    response = app.make_response(redirect(request.referrer))
    response.set_cookie('user', '', expires=0)
    return response

@app.route('/backends')
def backends():
    headers = getForwardHeaders(request)
    user = request.cookies.get("user", "")
    backends = {}
    out = "Backends List:<br>"
    for be in app.config['BACKENDS']:
        try:
            r = requests.get("http://"+be+"/version", headers=headers, timeout=10)
            if r.status_code != 500:
                backends[be] = {}
                backends[be]['title'] = requests.get("http://"+be+"/name", 
                                                     headers=headers, 
                                                     timeout=10).text
                print (backends[be]['title'])
                backends[be]['version'] = r.text
            else:
                backends[be] = {}
                backends[be]['title'] = be
                backends[be]['version'] = "Error: {}".format(r.status_code)
        except requests.exceptions.ReadTimeout:
            backends[be]['title'] = be
            backends[be]['version'] = "Is taking too long to answer. Please try again later"    
     #       out += "Backend: " + be + "| Version:" + version + "<br>"
    return render_template(
        'front.html',
        backends=backends,
        user=user
    )

app.run(host='0.0.0.0', port=app.config['PORT'], debug=True)