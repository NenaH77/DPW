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
        p.inputs = [['books', 'text', 'Book title'],['Submit', 'submit']]
        #['author', 'text', 'Author Name']

        self.response.write(p.print_out())


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

    #def print_out(self):
        #return self._head + self._body + self._close

class FormPage(Page):
    def __abs__(self):
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
