'''
name: Angelica Dinh
date: sept 16, 2014
class: dpw
assignment: final project: proof of concept

'''
import webapp2
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






class Page(object):
    def __init__(self):
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Detailed Movies</title>
    </head>
    <body> '''

        self.body = "Movies App"
        self.close = '''
    </body>
</html> '''

    def print_out(self):
        return self.head + self.body + self.close

class Movie(Page):
    def __init__(self):
        #constructor function for the super class
        super(Movie, self).__init__()
        self._open = '<form method = "GET">'
        self._end = '</form>'
        self._options = []
        self._movie_options = ''

    @property
    def options(self):
        pass

    @options.setter
    def options(self, movie_array):
        self._options = movie_array

        for item in movie_array:
            self._movie_options += '<input type="' + item[1] + '"name="' + item[0]
            if len(item) >2:
                self._movie_options += '"placeholder="' + item[2]+ '" />'
            else:
                self._movie_options += '" />'

        print self._movie_options

    def print_out(self):
        return self.head + self.body + self._open + self._movie_options + self._end + self.close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
