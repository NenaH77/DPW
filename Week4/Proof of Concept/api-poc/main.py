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

        if self.request.GET:
            name = self.request.GET['name']
            url = "http://api.foxsports.com/v1/content?partnerkey=KfymW7p5W38=&pageTypes=story&enable=fulldata&disable=html" + name

            print name








class Page(object):
    pass

class Sports(Page):
    pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
