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
        self.response.write(p.print_out())

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
            song = jsondoc['song']
            #artist = jsondoc['ArtistName']
            #album = jsondoc['AlbumName']

            self.reponse.write(jsondoc)
            self.response.write(song)
            self.response.write("Song Name:" + song)

            for item in song:
               album = item['object']['AlbumName']
               artist = item['object']['ArtistName']
               song = item['object']['SongName']
            self.response.write('Album Name:' + album + '<br>' + 'Artist Name:' + artist + '<br>' + 'Song Name:' + song)

class Page(object):
    def __init__(self):
        self.head = '''
<DOCTYPE HTML>
<html>
    <head>
        <title>Music</title>
    </head>
    <body>'''

        self.body = "Music App"
        self.close = '''
    </body>
</html>'''

    def print_out(self):
        return self.head + self.body + self.close

class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()#constructor function for the super class
        #create attribute for formpage
        self.form_open = '<form method ="GET">'
        self.form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

        #getter
        @property
        def inputs(self):
            pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
