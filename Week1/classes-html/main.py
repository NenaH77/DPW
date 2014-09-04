'''
name: Angelica Dinh
date: sept 4, 2014
class: dpw
lab: class-html

'''
import webapp2

from pages import Page #from file/package import Class(p = Page())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        #print p.print_out() # this prints on our log console google engine
        #p.body = "Miss Piggy likes Kermit de Frog!"
        self.response.write(p.print_out()) #writes to our browser page



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
