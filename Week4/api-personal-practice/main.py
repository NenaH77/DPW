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
        p.inputs = [['books', 'text', 'Book title'], ['author', 'text', 'Author Name'], ['submit', 'Submit']]



        if self.request.GET:
            books = self.request.GET['books']
            author = self.request.GET['author']
            bm = BookModel()
            bm.books = self.request.GET['books']
            bm.author = self.request.GET['author']
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
        pass

    @property
    def content(self):
        return self.__content

    @property
    def bdos(self):
        pass

    @bdos.setter
    def bdos(self, arr):
        self.__bdos = arr

        print self.__bdos





class BookModel(object):
    pass

class BookData(object):
    pass


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
        return self._body + self._body + self._close




class FormPage(Page):
    pass



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
