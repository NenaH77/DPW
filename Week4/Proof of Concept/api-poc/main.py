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
            score = self.request.GET['score']
            person = self.request.GET['type']
            url = "http://api.foxsports.com/v1/content?partnerkey=KfymW7p5W38=&pageTypes=story&enable=fulldata&disable=html"










class Page(object):
    def __init__(self):
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Detailed Sports</title>
    </head>
    <body> '''

        self.body = "Sports App"
        self.close = '''
    </body>
</html> '''

class Sports(Page):
    pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
