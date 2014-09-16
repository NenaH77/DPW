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
        p = Sports()
        p.options = [['name', 'text', 'name'], ['submit', 'submit']]
        self.response.write(p.options)

class Page(object):
    pass

class Sports(Page):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
