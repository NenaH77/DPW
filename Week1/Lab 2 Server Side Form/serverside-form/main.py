'''
name: Angelica M. Dinh
date: Sept 8, 2014
class: DWP
assignment: Simple Form
'''


import webapp2

#import file
from page import page1

class MainHandler(webapp2.RequestHandler):
    def get(self):#where my function begins
        pg = page1() #p represents class page(object) from page.py


        if self.request.GET:
            #stores info from the variable form
            fn = self.request.GET['first_name']
            ln = self.request.GET['last_name']
            em = self.request.GET['email']
            ph = self.request.GET['phone']
            ay = self.request.GET['about-you']
            rel = self.request.GET['religion']
            edu = self.request.GET['edu']
            gend = self.request.GET['gender']
            eth = self.request.GET['ethnicity']

            #call print function (displays info)
            self.response.write(pg.print_out(fn + ln + em + ph + ay + rel + edu + gend + eth)) #writes to our browser page
        else:
            self.response.write(pg.print_out(""))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
