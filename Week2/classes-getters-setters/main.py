'''
name: Angelica Dinh
date: sept 8, 2014
class: dpw
lab: getters and setters

'''
import webapp2

from pages import Page #from file/package import Class(p = Page())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "My page!" #Setter was created so we could change
        p.css = "css/style.css"
        p.body = "Miss Piggy likes Kermit de Frog!"
        p.update()
        self.response.write(p.whole_page)



        #print p.print_out() # this prints on our log console google engine
        #self.response.write(p.print_out()) #writes to our browser page



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
