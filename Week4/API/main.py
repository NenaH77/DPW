'''
name: Angelica Dinh
date: sept 20, 2014
class: dpw
assignment: api

'''
import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = ['movie', 'text', 'Movie Title'] ['Submit', 'submit']

        if self.request.GET:
            #get info from the API
            movie = self.request.GET['movie']

            #we need to get movie into the MovieModel
            mm = MovieModel()

            #send our movie from the URL to our Model
            mm.movie = self.request.GET['movie']

            #tells it to connect to the API
            mm.callApi()

            #creates our MovieView
            mv = MovieView()

            #takes data obj from Model and gives them to the View





class MovieView(object):
    ''' class handles how the data is shown to the user '''
    def __init__(self):
        self.mdos= []
        self.content = '<br />'


class MovieModel(object):
    ''' class handles how the data is shown to the user '''
    def __init__(self):
        self.__url = "http://api.rottentomatoes.com/api/public/v1.0"
        self.__key = "3wgzeuyj3ttnqnjbfr5xgafx&q="
        self.__full_url = self.__url + '/lists/movies/in_theaters' + self.__key + '&page_limit='

class MovieData(object):
    pass

class Page(object):
    pass

class FormPage(Page):
    pass


        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
