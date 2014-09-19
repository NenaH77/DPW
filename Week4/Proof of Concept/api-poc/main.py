'''
name: Angelica Dinh
date: sept 16, 2014
class: dpw
assignment: final project: proof of concept

'''
import webapp2
import urllib2 #python classes and code needed to open url information
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [["song", "text", "Song Name"], ["Submit", "submit"]]

        if self.request.GET:
            #get info from the API
            song = self.request.GET['song']
            url = "http://tinysong.com/b/" + song + "?format=json&key=d3464d3a1ab7f49b1dcb2acc520de571"

            #request the info from the url
            request = urllib2.Request(url)

            #special method that allows us to open the results and we get to look inside the url
            opener = urllib2.build_opener()

            #telling it to open the url take the results and put them inside the result variable
            result = opener.open(request)

            print result

            #parsing the JSON
            jsondoc = json.load(result)
            song = jsondoc['SongName']
            artist = jsondoc['ArtistName']
            album = jsondoc['AlbumName']

            self.reponse.write(jsondoc)
            self.response.write(song)
            self.response.write("Song Name:" + song)


class Page(object):
    pass


class FormPage(Page):
    pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
