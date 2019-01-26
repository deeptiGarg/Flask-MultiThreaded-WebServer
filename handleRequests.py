import requests
from threading import Thread
import sys
import time
import json

class webGetThread(Thread):
    def __init__(self,webServerUrl):
        Thread.__init__(self)
        self.webServerUrl = webServerUrl

    def run(self):
            # Make a request to the Flask app url provided
            makeReq(self.webServerUrl)

headerServer, requestTimes = [], []  # in-process lists to store the incoming request time and user agaent from HTTP Header

def main():
    
    if len(sys.argv) < 2:
	    sys.exit()
    else:
        totalReqs = sys.argv[1] 
        webServerUrl = sys.argv[2]
        
    for i in range(int(totalReqs)):
        worker = webGetThread(webServerUrl)
        # Setting daemon to False so that the main thread doesn't exits until all workers have exited.
        worker.daemon = False
        worker.start()    # Start each thread
    allRequests = [{"Time": t, "Server": hs} for t, hs in zip(requestTimes, headerServer)]
    
    # Print JSON object 
    print(json.dumps(allRequests))

def makeReq(serverUrlReq):
    r = requests.get(serverUrlReq, auth=('user', 'pass'))
    requestTimes.append(time.time())
    headerServer.append(r.headers['Server'])

if __name__ == "__main__":
    main()