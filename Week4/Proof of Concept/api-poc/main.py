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




        self.response.write(p.new_print_out(self.new_content + p.form));






class MovieInfo(object):
    #MovieInfo will allow me to fetch the url; load the contents and use the contents here in my python code
    def __init__(self, my_movie):
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

        self.__cm = [self.current_movie_title, self.current_movie_rating, self.current_movie_critic_rating, self.current_movie_synopsis, self.current_movie_actor]

    @property
    def cm(self):
        return self.__cm

    @cm.setter
    def cm(self, new_cm):
        self.__cm = new_cm
        return self.__cm

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, new_movie):
        self.__movie = new_movie
        return self.__movie

class MovieView(object):
    def __init__(self):
        self.__new_content = " "

        self.__new_content += "<div class='movies'><p><strong>Movie Title:</strong>" + self.cm[0] + "</p>" + "<br>" + "<p><strong>Staring:</strong></p>" + self.cm[4] + "<br>" + "<p><strong>Rating:</strong></p>" + self.cm[1] + "<br>" + "<p><strong>synopsis:</strong></p>" + self.cm[3] + "<br>"+ "<p><strong>Critics Rating:</strong></p>" + self.cm[2] + "</div>"

    @property
    def new_content(self):
        return self.__new_content

    @new_content.setter
    def new_content(self, nc):
        self.__new_content = nc



class MovieData(object):
    def __init__(self):
        self.title =""
        self.rating = ""
        self.critic_rating = ""
        self.synopsis = ""
        self.actor = ""








app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
