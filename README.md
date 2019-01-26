#Flask-MultiThreaded-WebServer

Contains multi-threaded Flask web app and a python script to create multiple GET requests to this web app

handleRequests.py - Script which creates multi-threaded requests to the app. 
                  - Returns a JSON object with 2 fields - TIME (indicating the time of the request) and SERVER (server details)

templates/template.html - Basic HTML page which shows the number of requests received by the app since it is running. 

webServer.py - A simple Flask web app server which displays the counter for the requests received in the front-end.

tornadoServer.py - Tried Tornado framework to create the above Flask server.
