'''
name: Angelica Dinh
date: sept 16, 2014
class: dpw
assignment: final project: proof of concept

'''
import webapp2
from page import Page
import urllib2 #python classes and code needed to open url information
from xml.dom import minidom




class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        if self.request.GET:
            #create an instance of my class MovieInfo
            m = MovieInfo()

            #get info from the API
            search = self.request.GET['search']

            #sending data and parses it with method I created
            m.send_info()






        self.response.write(p.print_out())

class MovieInfo(object):
    def __init__(self):
        self._url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=3wgzeuyj3ttnqnjbfr5xgafx&q=" #url from where the information will be requested
        self._id = " "
        self._params = "&page_limit"


    def send_info(self):
        full_url = self._url + self._id + self._params
        request = urllib2.Request(full_url)#requests the info from the url
        opener = urllib2.build_opener()#special method that allows us to open the results/response and we get to look inside the url
        result = opener.open(request)#we r fetching the url. in other words, we're telling it to open the url take the results and put them inside the result variable

        #parse it
        xmldoc = minidom.parse(result)




        #finding tags using minidom
        self. mv.title = xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue
        self. mv.actor =xmldoc.getElementsByTagName('actor')[0].firstChild.nodeValue
        self. mv.year =xmldoc.getElementsByTagName('year')[0].firstChild.nodeValue
        self. mv.mpaa_rating =xmldoc.getElementsByTagName('mpaa_rating')[0].firstChild.nodeValue
        self. mv.synopsis =xmldoc.getElementsByTagName('synopsis')[0].firstChild.nodeValue


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
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, new_movie_info):
        self.__movie = new_movie_info




#
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
