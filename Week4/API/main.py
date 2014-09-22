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
        p.inputs = ['movie', 'text', 'Movie Title'], ['Submit', 'submit']

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

            #html body is displayed properly
            p._body = mv.content

        self.response.write(p.print_out())


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
            self.__content += 'Title:' + mov.title + 'Critics Ratings:' + mov.critics_score + 'Year:' + mov.year
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


class MovieModel(object):
    ''' class handles how the data is shown to the user '''
    def __init__(self):
        self.__url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey="
        self.__key = "3wgzeuyj3ttnqnjbfr5xgafx&q="
        self.__movie = ""
        self.__page = self.__movie + "&page_limit=1"
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
        jsondoc = json.load(result)

        #stores data
        self.title = jsondoc['movies'][0]['title']
        self.ratings = jsondoc['movies'][0]['critics_score']
        self.year = jsondoc['movies'][0]['year']
        self.synopsis = jsondoc['movies'][0]['synopsis']
        self.name = jsondoc['movies'][0]['abridged_cast'][0]['name']

        #combine variables into 1 obj
        self.__cm = [self.title, self.ratings, self.year, self.synopsis, self.name]


        print self.title

    @property
    def cm(self):
        return self.__cm

    @cm.setter
    def cm(self, c):
        self.__cm = c

    @property
    def movie(self):
        pass

    @movie.setter
    def movie(self, m):
        self.__movie = m

class MovieData(object):
    ''' this data object holds the data fetched by the model and shown by the view '''
    def __init__(self):
        self.title = ''
        self.rating = ''
        self.year = ''
        self.synopsis = ''
        self.name = ''

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
    def __init__(self):
        super(FormPage, self).__init__()
        #create attributes for FormPage.
        self._form_open = '<form method = "GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr

        #sort through the mega array and create HTML inputs based on the info there
        for item in arr:
            #print item
            self._form_inputs += '<input type="' +item[1]+ '"name="' + item[0]
            #if there is a 3rd item.. add it in....
            if len(item) >2:
                self._form_inputs += '"placeholder="' + item[2]+'" />'
            #otherwise.. end the tag
            else:
                self._form_inputs += '" />'

    #move self.body after self._form_close
    def print_out(self):
        return self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
