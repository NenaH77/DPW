'''
name: Angelica Dinh
date: sept 10, 2014
class: dpw
assignment: encapsulated calculator

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):







        














        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
