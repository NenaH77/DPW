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
        p = FormPage()
        p.inputs = [['books', 'text', 'Book title'],['author', 'text', 'Author Name'],['Submit', 'submit']]


        if self.request.GET:
            books = self.request.GET['books']
            author = self.request.GET['author']
            bm = BookModel()
            bm.books = self.request.GET['books']
            bm.books = self.request.GET['books'].replace(" ","+")
            bm.author = self.request.GET['author']
            bm.author = self.request.GET['author'].replace(" ","+")
            bm.callApi()

            print bm.dos

            bv = BookView()
            bv.bdos = bm.dos
            p._body = bv.content

        self.response.write(p.print_out())


class BookView(object):
    def __init__(self):
        self.__bdos = []
        self.__content = "<br />"

    def update(self):
        for do in self.__bdos:
            self.__content += "<h3>Title: " + do.title + "</h3>"
            self.__content += "<p>Author: " + do.author + "</p>"
            self.__content += "<img src=" + do.image + "alt='image' height='180' width='120'/>"
            self.__content += "<p>Description: " + do.description + "</p>"
            self.__content += "<p>Price: $" + str(do.price) + "</p>"



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
        self.__url = "https://www.googleapis.com/books/v1/volumes?q='"
        self.__title = ""
        self.__author = ""
        self.__jsondoc = ""

    def callApi(self):
        request = urllib2.Request(self.__url + self.__title + self.__author)
        opener = urllib2.build_opener()
        result = opener.open(request)

        self.__jsondoc = json.load(result)

        books = self.__jsondoc['items']

        self._dos = []

        for item in books:
            do = BookData()
            try:
                do.title = item['volumeInfo']['title']
                do.author = item['volumeInfo']['authors'][0]
                do.description = item['volumeInfo']['description']
                do.image = item['volumeInfo']['imageLinks']['thumbnail']
                do.price = item['saleInfo']['retailPrice']['amount']
                self._dos.append(do)
            except:
                self._dos.append(do)

        print do.price

    @property
    def dos(self):
        return self._dos

    @property
    def title(self):
        pass

    @title.setter
    def title(self, t):
        self.__title = t

    @property
    def author(self):
        pass

    @author.setter
    def author(self, a):
        self.__author = a

class BookData(object):
    def __init__(self):
        self.title = ''
        self.author = ''
        self.description = ''
        self.image = ''
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
        self._body = '''
        <div class='wrapper'>
            <h3>Welcome to HookBook</h3>
                <p>Search for your next book</p>
        </div>

        '''
        self._close = '''
    </body>
    <footer>
        <p>API Book Search | Angelica M. Dinh </p>
    </footer>
</html>
     '''

    #def print_out(self):
        #return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method = "GET">'
        self._form_inputs = ''
        self.__inputs = []
        self._form_close = '</form>'


    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' +item[1]+ '"name="' +item[0]
            if len(item) >2:
                self._form_inputs += '"placeholder="' +item[2]+'"/>'
            else:
                self._form_inputs += '"/>'

    def print_out(self):
        return self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
