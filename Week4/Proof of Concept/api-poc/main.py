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
            #passes url into MovieInfo class
            my_movie = self.request.GET["movie"]

            #creates an instance of my MovieInfo class
            movinfo = MovieInfo()

            #sending request to api method
            movinfo.apiInfo()

            #creates my instance
            movview = MovieView()


class MovieInfo(object):
    #MovieInfo will allow me to fetch the url; load the contents and use the contents here in my python code
    def __init__(self):
        self.__movie = ""
        self.jsondoc = ""

    def apiInfo(self):
        #get info from API
        url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=3wgzeuyj3ttnqnjbfr5xgafx&q="+ self.__movie + "&page_limit"
        #request the info from the url
        request = urllib2.Request(url)
        #special method that allows us to open the results and we get to look inside the url
        opener = urllib2.build_opener()
        #we r fetching the url. in other words, we're telling it to open the url take the results and put them inside the result variable
        result = opener.open(request)

        #parsing the JSON
        jsondoc = json.load(result)
        #stores my variables
        self.current_movie_title = jsondoc["movies"][0]["title"]
        self.current_movie_rating = jsondoc["movies"][0]["mpaa_rating"]
        self.current_movie_critic_rating = jsondoc["movies"][0]["ratings"]["critics_rating"]
        self.current_movie_synopsis = jsondoc["movies"][0]["synopsis"]
        self.current_movie_actor = jsondoc["movies"][0]["abridged_cast"][0]["name"]

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, new_movie):
        self.__movie = new_movie


class MovieView(object):
    def __init__(self):






class MovieData(object):
    def __init__(self):
        pass



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
