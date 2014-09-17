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
            movie = self.request.GET['movie']

            #sending data and parses it with method I created
            m.send_info()



        self.response.write(p.print_out())

class MovieInfo(object):
    def __init__(self):
        self.url = "http://api.rottentomatoes.com/api/public/v1.0/" #url from where the information will be requested
        self.params = ".json?apikey=3wgzeuyj3ttnqnjbfr5xgafx"


    def send_info(self):
        full_url = self.url + '/lists/movies/in_theaters' + self.params
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




#
class MovieData(object):
    def __init__(self):
        self.title =""
        self.actor = ""
        self.year = ""
        self.mpaa_rating = ""
        self.synopsis = ""






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
