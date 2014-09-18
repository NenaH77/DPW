'''
name: Angelica Dinh
date: sept 16, 2014
class: dpw
assignment: final project: proof of concept

'''
import webapp2
from page import * #maybe changing my page name still deciding will name my import later
import urllib2 #python classes and code needed to open url information
import json




class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [["movie", "text", "Movie Title"], ["Submit", "submit"]]

        if self.request.GET:
            my_movie = self.request.GET["movie"]#passes url into MovieInfo class
            movinfo = MovieInfo() #creates an instance of my MovieInfo class


class MovieInfo(object):
    #MovieInfo will allow me to fetch the url; load the contents and use the contents here in my python code
    def __init__(self):
        self.movie = ""




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
