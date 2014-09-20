'''
name: Angelica Dinh
date: sept 15, 2014
class: dpw
lab: weather-app_mvc

'''
import webapp2
import urllib2 #python classes and code needed to request info, receiving and opening
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'zip code'], ['Submit', 'submit']]

        if self.request.GET:
            #get info from the API
            zip = self.request.GET['zip']

            #we need to get zip into the weather model
            wm = WeatherModel()

            wm.zip = self.request.GET["zip"] #sends our Zip from the URL to our Model

            wm.callApi()#tells it to connect to the API

            #creates our View
            wv = WeatherView()

            # takes data obj [dos] from Model class and gives them to [wdos] in View class
            wv.wdos = wm.dos

            #so that the html body is displayed properly
            p._body = wv.content

        self.response.write(p.print_out())


class WeatherView(object):
    ''' this class handles how the data is shown to the user  '''
    def __init__(self):
        self.__wdos = []
        self.__content = "<br />"

    def update(self):#create a function that updates our display
        for do in self.__wdos: #need to go thru our list of dos
            self.__content += do.day + " HIGH:  " + do.high + " LOW:  " + do.low
            self.__content += " CONDITION:  " + do.condition
            self.__content += '<img src="images/' + do.code + '.png" width="20" /><br/>'

    @property #read only
    def content(self):
        return self.__content

    @property #empty getter
    def wdos(self):
        pass

    @wdos.setter #write only
    def wdos(self, arr):
        self.__wdos = arr
        self.update()

class WeatherModel(object):
    ''' this model handles fetching, parsing and sorting data from Yahoo's weather API  '''
    def __init__(self):
        self.__url = "http://xml.weather.yahoo.com/forecastrss?p="
        self.__zip = ''
        self.__xmldoc = ''

    def callApi(self):
        #REQUESTS AND LOADS INFO FROM API
        #assemble the request
        request = urllib2.Request(self.__url + self.__zip)
        #use the urllib2 to create and object to get the url
        opener = urllib2.build_opener()
        #use the url to get a result - request info from the API
        result = opener.open(request)

        #PARSING DATA
        self.__xmldoc = minidom.parse(result)

        #SORTING DATA
        list = self.__xmldoc.getElementsByTagName('yweather:forecast')
        #we need to create a loop because we want to add days of the week

        self._dos = []
        for tag in list:
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.low = tag.attributes['low'].value
            do.date = tag.attributes['date'].value
            do.code = tag.attributes['code'].value
            do.condition = tag.attributes['text'].value
            #put inside our array
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self.__zip = z

class WeatherData(object):
    ''' this data object holds the data fetched by the model and shown by the view   '''
    def __init__(self):
        self.day = ""
        self.high = ""
        self.low = ""
        self.code = ""
        self.condition = ""
        self.date = ""

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
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' +item[1]+ '"name="' + item[0]
            #if there is a 3rd item.. add it in....
            if len(item) >2:
                self._form_inputs += '"placeholder="' + item[2]+'" />'
            #otherwise.. end the tag
            else:
                self._form_inputs += '" />'

    def print_out(self):#move self.body after self._form_close
        return self._head + "Weather App" + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
