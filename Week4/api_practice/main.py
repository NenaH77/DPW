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
        self.response.write('Hello world!')





class Page(object):
    pass


class FormPage(Page):
    pass



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
