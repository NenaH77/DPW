'''
name: Angelica Dinh
date: sept 16, 2014
class: dpw
assignment: final project: proof of concept

'''
import webapp2
import urllib2 #python classes and code needed to open url information
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
