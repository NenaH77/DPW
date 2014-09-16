'''
name: Angelica Dinh
date: sept 15, 2014
class: dpw
lab: weather-app

'''
import webapp2
import urllib2 #python classes and code needed to request info, receiving and opening
from xml.dom import minidom

#Will b used more of an exception thn a rule. Polymorphism will not b sumthig used all d time.

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'zip code'], ['Submit', 'submit']]
        self.response.write(p.print_out())

        if self.request.GET: #only if there is a zip variable in the url
            #get info form the API
            zip = self.request.GET['zip']
            url = "http://xml.weather.yahoo.com/forecastrss?p=" + zip

            #assemble the request
            request = urllib2.Request(url) #we are using the class and accessing the static method in the class. We don't need to create an instance

            #use the urllib2 to create and object to get the url
            opener = urllib2.build_opener()

            #use the url to get a result - request info from the API
            result = opener.open(request)

            print result

            #parse the XML
            xmldoc = minidom.parse(result)
            self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
            self.content = '<br/>'
            list = xmldoc.getElementsByTagName('yweather:forecast')
            #we need to create a loop because we want to add days of the week
            for item in list:
                self.content += item.attributes['day'].value
                self.content += " HIGH: " + item.attributes['high'].value
                self.content += " LOW: " + item.attributes['low'].value
                self.content += " CONDITION: " + item.attributes['text'].value
                self.content += ' <img src="images/'+item.attributes['code'].value+'.png" width ="30"/>'
                self.content += '<br/>'

            self.response.write(self.content)

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body> '''

        self._body = 'Weather App'
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
