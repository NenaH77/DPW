'''
name: Angelica Dinh
date: sept 9, 2014
class: dpw
lab: encapsulation

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')






















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
