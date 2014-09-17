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
        p = Movies()
        p.options = [['title', 'text', 'Toy Story'], ['name', 'text', 'Tom Hanks' ], ['characters', 'text', 'Woody' ], ['submit', 'submit']]
        self.response.write(p.options)

        if self.request.GET:
            title = self.request.GET['title']
            actor = self.request.GET['name']
            url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=[3wgzeuyj3ttnqnjbfr5xgafx]"








class Page(object):
    def __init__(self):
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Detailed Movies</title>
    </head>
    <body> '''

        self.body = "Movies App"
        self.close = '''
    </body>
</html> '''

class Sports(Page):
    def __init__(self):
        super(Sports, self).__init__()
        self._sport_open = ''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
