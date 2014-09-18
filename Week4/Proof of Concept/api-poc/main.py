'''
name: Angelica Dinh
date: sept 16, 2014
class: dpw
assignment: final project: proof of concept

'''
import webapp2
from page import Page
import urllib2 #python classes and code needed to open url information
#from xml.dom import minidom
import json




class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        if self.request.GET:
            #create an instance of my class MovieInfo
            m = MovieInfo()

            #get info from the API
            movie = self.request.GET['movie']

            #sending data and parses it with method I created
            m.send_info()
            #creates my instance
            pg_view = MovieView()
            #transfers info that's in MovieInfo to MovieView
            pg_view.mov = m.mv
            #updates my update
            pg_view.update()
            #making form (in page.py) to hold new content from Movie view class
            p.form = pg_view.new_content

        self.response.write(p.print_out())

class MovieInfo(object):
    def __init__(self):
        self.apikey = "3wgzeuyj3ttnqnjbfr5xgafx&q="
        self.baseUrl = "http://api.rottentomatoes.com/api/public/v1.0"

    def send_info(self):
        url = self.baseUrl + "/movies.json?apikey=" + self.apikey

        request = urllib2.Request(url)#requests the info from the url

        opener = urllib2.build_opener()#special method that allows us to open the results/response and we get to look inside the url

        result = opener.open(request)#we r fetching the url. in other words, we're telling it to open the url take the results and put them inside the result variable

        jsondoc = json.load(result)
        title = jsondoc['title']
        actor = jsondoc['actor']
        year = jsondoc['year']
        rating = jsondoc['mpaa_rating']
        synopsis = jsondoc['synopsis']


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self.__id = new_id




    @property
    def mv(self):
        return self.__mv

    @property
    def search(self):
        return self.search

    @search.setter
    def search(self, new_search):
        self.__search = new_search





class MovieData(object):
    def __init__(self):
        self.title =""
        self.actor = ""
        self.year = ""
        self.mpaa_rating = ""
        self.synopsis = ""


class MovieView(object):
    def __init__(self):

        self.mov = MovieData()
        self.new_content = " "

    def update(self):

        self.new_content = '''
        <div class="content">
            <p>{mv.title}</p>
            <p>{mv.actor}<p>
            <p>{mv.year}</p>
<           p>{mv.mpaa_rating}</p>
            <p>{mv.synopsis}</p>
        </div>
        '''

        self.new_content = self.new_content.format(**locals())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
