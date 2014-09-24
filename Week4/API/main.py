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
        p.inputs = [['movies', 'text', 'Movie Title'], ['Submit', 'submit']]

        if self.request.GET:
            #get info from the API
            movies = self.request.GET['movies']

            #we need to get movie into the MovieModel
            mm = MovieModel()

            #send our movie from the URL to our Model
            mm.movies = self.request.GET['movies']

            #tells it to connect to the API
            mm.callApi()

            #creates our MovieView
            mv = MovieView()

            #takes data obj from Model and gives them to the View
            mv.mdos = mm.cm

            #html body is displayed properly
            p._body = '<h3>Movie Title:' + mm.cm_title + '</h3><br/><p class="info">Critics Rating:' + str(mm.cm_ratings) + '</p><br/><p class="info">Year:' + str(mm.cm_year) + '</p><br/><p class="info">Synopsis:' + mm.cm_synopsis + '</p><br/><p class="info">Featuring:' + mm.cm_name + '</p>'

        self.response.write(p.print_out())


class MovieView(object):
    ''' class handles how the data is shown to the user '''
    def __init__(self):
        #holds data found from another class
        self.__mdos= []
        #Placeholder for content section
        self.__content = '<br />'


    #this will allow us to read our content
    @property
    def content(self):
        return self.__content

    #we don't need to read our mdos, we need to change it so this can be empty
    @property
    def mdos(self):
        #pass
        return self.__mdos

    #write only
    @mdos.setter
    def mdos(self, arr):
        self.__mdos = arr


class MovieModel(object):
    ''' class handles how the data is shown to the user '''
    def __init__(self):
        self.__movies = ""



    #function used to call API and gather info Api
    def callApi(self):
        url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=3wgzeuyj3ttnqnjbfr5xgafx&q=" + self.__movies.replace('','+') + "&page_limit=1"

        print url

        #assembles the request
        request = urllib2.Request(url)
        #use the urllib2 to create object and get url
        opener = urllib2.build_opener()
        #use the url to get a result - request info from the API
        result = opener.open(request)

        #parsing the json
        jsondoc = json.load(result)


        #dos "Data Objects" property to contain do "Data Object" being passed from below for loop
        self._dos = []
        try:
            self.cm_title = jsondoc['movies'][0]['title']
            self.cm_ratings = jsondoc['movies'][0]['ratings']['critics_score']
            self.cm_year = jsondoc['movies'][0]['year']
            self.cm_synopsis = jsondoc['movies'][0]['synopsis']
            self.cm_name =jsondoc['movies'][0]['abridged_cast'][0]['name']
            self.cm = [self.cm_title, self.cm_ratings, self.cm_year, self.cm_synopsis, self.cm_name]
        except:
            pass

        #print self._dos

    #@property
    def dos(self):
        return self._dos

    @property
    def movies(self):
        pass

    @movies.setter
    def movies(self, m):
        self.__movies = m


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
        <title>Welcome to Movie Search</title>
    </head>
    <body> '''

        self._body = 'Movie App'
        self._close = '''
    </body>
</html> '''


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()
        #create attributes for FormPage.
        self._form_open = '<form method = "GET">'
        self._form_inputs = ''
        self.__inputs = []
        self._form_close = '</form>'

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
