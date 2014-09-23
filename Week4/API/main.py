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

        self.response.write(p.print_out())

        if self.request.GET: #only if there is a zip variable in the url
            #get info form the API
            movies = self.request.GET['movies']
            url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=3wgzeuyj3ttnqnjbfr5xgafx&q=" + movies + "&page_limit=1"
            self.jsondoc = ""
            #assemble the request
            request = urllib2.Request(url) #we are using the class and accessing the static method in the class. We don't need to create an instance

            #use the urllib2 to create and object to get the url
            opener = urllib2.build_opener()

            #use the url to get a result - request info from the API
            result = opener.open(request)

            #parsing the JSON
            jsondoc = json.load(result)

            #var to contain json call to "movies" from API call
            current_movies = self.jsondoc['movies']
            #dos 'data obj' property to contain do 'data object' being passed from loop
            self._dos = []
            #for loop will run thru ea item of 'do.data obj' in the current_movies 'dos data obj' var
            for item in current_movies:
                #instantiation of MovieData
                do = MovieData()
                do.title = item['movies'][0]['title']
                do.ratings = item['movies'][0]['critics_score']
                do.year = item['movies'][0]['year']
                do.synopsis = item['movies'][0]['synopsis']
                do.name = item['movies'][0]['abridged_cast'][0]['name']
                #put inside my array
                self._dos.append(do)

            print self._dos



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

        self._body = 'Movie App'
        self._close = '''
    </body>
</html> '''

    #this is being overridden below
    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #2 ways to write:
        #1. Page.__init__()    or   2. super(FormPage, self).__init__()
        super(FormPage, self).__init__()#constructor function for the super class
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

        print self._form_inputs

#Polymorphism Alert!!! -------method overriding
    #we are overriding the def print_out method in the parent class
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
