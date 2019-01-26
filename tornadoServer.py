import tornado.ioloop
import tornado.web
import signal

countReq = 0

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        global countReq
        countReq =  countReq +1
        print(self._headers.get('Date'))
        self.render("template.html", count= countReq)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
def sig_exit(signum, frame):
    tornado.ioloop.IOLoop.instance().add_callback_from_signal(do_stop)

def do_stop(signum, frame):
    tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    print("Server running at http://127.0.0.1:8888/")
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)     ##forks one process per cpu
    signal.signal(signal.SIGBREAK, sig_exit)
    tornado.ioloop.IOLoop.current().start()

    
    