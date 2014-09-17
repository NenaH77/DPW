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
        p = Page()

        self.response.write(p.open + p.close) #test to see if I'm getting errors

        if self.request.GET:
            #get info from the API
            title = self.request.GET['title']
            actor = self.request.GET['name']
            mv = MovieInfo(title)

            #create an instance of my class MovieInfo
            m = MovieInfo()

        self.response.write(p.print_out())

class MovieInfo(object):
    def __init__(self):
        self.url = "http://api.rottentomatoes.com/api/public/v1.0/" #url from where the information will be requested
        self.params = ".json?apikey=3wgzeuyj3ttnqnjbfr5xgafx"


    def send_info(self):
        full_url = self.url + '/lists/movies/in_theaters' + self.params
        request = urllib2.Request(full_url)#requests the info from the url
        opener = urllib2.build_opener()#special method that allows us to open the results/response and we get to look inside the url
        result = opener.open(request)#we r fetching the url. in other words, we're telling it to open the url take the results and put them inside the result variable





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
