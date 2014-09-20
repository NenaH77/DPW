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
            mv.mdos = mm.dos




class MovieView(object):
    ''' class handles how the data is shown to the user '''
    def __init__(self):
        #holds data found from another class
        self.__mdos= []
        #Placeholder for content section
        self.__content = ''

    #create function that updates our display
    def update(self):
        for mov in self.__mdos:
            self.__content += 'Title:' + mov.title + 'Year:' + mov.year
            self.__content += 'Synopsis:' + mov.synopsis
            self.__content += 'Cast:' + mov.name

    @property#this will allow us to read our content
    def content(self):
        return self.__content

    @property#we don't need to read our mdos, we need to change it so this can be empty
    def mdos(self):
        pass

    @mdos.setter#write only
    def mdos(self, arr):
        self.__mdos = arr
        self.update()#this will allow us to update our function above

        print self.__mdos




class MovieModel(object):
    ''' class handles how the data is shown to the user '''
    def __init__(self):
        self.__url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey="
        self.__key = "3wgzeuyj3ttnqnjbfr5xgafx&q="
        self.__movie = ""
        self.__page = self.__movie + "&page_limit="
        self.__jsondoc = ""

    #function used to call API and gather info Api
    def callApi(self):

        #assembles the request
        request = urllib2.Request(self.__url + self.__key + self.__page)
        #use the urllib2 to create object and get url
        opener = urllib2.build_opener()
        #use the url to get a result
        result = opener.open(request)

        #parsing the json
        self.__jsondoc = json.load(result)

        #sorting data
        #we want to hold our content inside a data obj
        self._dos =[]
        #creating a data obj and assigning the value from our json file
        do = MovieData()





class MovieData(object):
    pass

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body> '''

        self._body = 'Test My Movie App'
        self._close = '''
    </body>
</html> '''


class FormPage(Page):
    




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
