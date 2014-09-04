'''
name: Angelica Dinh
date: sept 4, 2014
class: dpw
lab: class-html

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        #print p.print_out() # this prints on our log console google engine
        self.response.write(p.print_out()) #writes to our browser page


class Page(object):
    def __init__(self): #constructor function
        self.title = "Welcome!" #Attribute is the page element: Title of page, Head of page, Body of page, etc
        self.css = "css/style.css" # DON'T FORGET TO ADD CSS INFO INSIDE 'app.yaml'
        self.head =  """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>{self.title}</title>
                <link href ="{self.css}" rel="stylesheet" type="text/css" />
            </head>
            <body>
        """
        self.body = "Welcome to my OOP Python page!"
        self.close = '''
            </body>
        </html>
        '''
    def print_out(self): #create method for printing
        #return self.head + self.body + self.close
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
