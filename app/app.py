import tornado.ioloop
import tornado.web
import socket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(socket.gethostname())

    def data_received(self, data):
        pass

def application_start():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])

if __name__ == "__main__":
    APP = application_start()
    APP.listen(8888)
    tornado.ioloop.IOLoop.current().start()