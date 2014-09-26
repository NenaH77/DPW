'''
name: Angelica Dinh
date: sept 26, 2014
class: dpw
assignment: no assignment just practice

'''
import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage
        p.inputs = [['books', 'text', 'Book title'],['submit', 'Submit']]
        #['author', 'text', 'Author Name']

        if self.request.GET:
            books = self.request.GET['books']
            #author = self.request.GET['author']
            bm = BookModel()
            bm.books = self.request.GET['books']
            #bm.author = self.request.GET['author']
            bm.callApi()

            print bm.dos

            bv = BookView()
            bv.bdos = bm.dos
            p._body = bv.content

        self.response.write(p.print_out())



class BookView(object):
    def __init__(self):
        self.__bdos = []
        self.__content = ""

    def update(self):
        for do in self.__bdos:
            self.__content += do.title
            self.__content += do.author
            self.__content += do.description
            self.__content += do.price

    @property
    def content(self):
        return self.__content

    @property
    def bdos(self):
        pass

    @bdos.setter
    def bdos(self, arr):
        self.__bdos = arr
        self.update()




class BookModel(object):
    def __init__(self):
        self.__url = "https://www.googleapis.com/books/v1/volumes?q="
        self.__title = ""
        #self.__author = ""
        self.__jsondoc = ""

    def callApi(self):
        request = urllib2.Request(self.__url + self.__books)
        opener = urllib2.build_opener()
        result = opener.open(request)

        self.__jsondoc = json.load(result)

        books = self.__jsondoc['items']

        self._dos = []

        for item in books:
            do = BookData()
            do.title = item['items'][0]['volumeInfo'][0]['title']
            do.author = item['items'][0]['volumeInfo'][0]['authors']
            do.description = item['items'][0]['volumeInfo'][0]['description']
            do.price = item['items'][0]['saleInfo']['listPrice']['amount']
            self._dos.append(do)

        print self._dos

    @property
    def dos(self):
        return self._dos

    @property
    def title(self):
        pass

    @title.setter
    def title(self, t):
        self.__title = t


class BookData(object):
    def __init__(self):
        self.title = ''
        self.author = ''
        self.description = ''
        self.price = ''


class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Book and Author Search</title>
    </head>
    <body>
    '''
        self._body = 'Books'
        self._close = '''
    </body>
    <footer>
        <p>API Book Search | Angelica M. Dinh </p>
    </footer>
</html>
     '''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __abs__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method = "GET">'
        self.__form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self._form_inputs +='<input type"' + item[1]+ '"name="' +item[0]
            if len(item)>2:
                self._form_inputs +='"placeholder="' +item[2]+'"/>'
            else:
                self._form_inputs += '"/>'

    def print_out(self):
        return self._head + self._form_open + self._form_inputs + self.__form_close + self._body + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
