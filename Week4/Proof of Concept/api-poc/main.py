'''
name: Angelica Dinh
date: sept 16, 2014
class: dpw
assignment: final project: proof of concept

'''
import webapp2
from page import Page
import urllib2 #python classes and code needed to open url information
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Movie()
        p.options = [['title', 'text', 'Toy Story'], ['name', 'text', 'Tom Hanks' ], ['characters', 'text', 'Woody' ], ['submit', 'submit']]
        self.response.write(p.options)

        if self.request.GET:
            #get info from the API
            mv = Movie()
            title = self.request.GET['title']
            actor = self.request.GET['name']
            characters = self.request.GET['characters']

            #url from where the information will be requested
            url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=3wgzeuyj3ttnqnjbfr5xgafx"

        #3 steps allow us to fetch the url; load the contents and use the contents here in our python code
            #requests the info from the url
            request = urllib2.Request(url)

            #special method that allows us to open the results/response and we get to look inside the url
            opener = urllib2.build_opener()

            #we r fetching the url. in other words, we're telling it to open the url take the results and put them inside the result variable
            result = opener.open(request)

            print result







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
