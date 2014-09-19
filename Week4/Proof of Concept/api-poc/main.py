'''
name: Angelica Dinh
date: sept 16, 2014
class: dpw
assignment: final project: proof of concept

'''
import webapp2
from page import * #maybe changing my page name still deciding will name my import later
import urllib2 #python classes and code needed to open url information
import json




class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [["movie", "text", "Movie Title"], ["Submit", "submit"]]
        self.response.write(p.print_out())

        if self.request.GET:
            self.request.GET['']
            self.request.GET['']
            url = " "



class Page(object):
    pass


class FormPage(Page):
    pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
