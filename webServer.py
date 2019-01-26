import requests
from flask import Flask, render_template, request
from threading import Lock

app = Flask(__name__)
app.debug = True
lock = Lock()           # Lock to safely access the counter variable to keep track of number of requets to the webserver
countReq = 0            # global count to keep track of number of requests. 

## All GET requests are handled by this function
@app.route('/', methods=['GET'])
def showCounter():
    global countReq
    lock.acquire()
    tmp = countReq
    tmp += 1
    countReq = tmp
    lock.release()
    ## template.html is the UI view which is being used
    return render_template('template.html', count= countReq)

## Main Function to run the Flask app
if __name__ == "__main__":
    print("Server running at http://127.0.0.1:8888/")
    app.run(port=8888, threaded = True)

	
