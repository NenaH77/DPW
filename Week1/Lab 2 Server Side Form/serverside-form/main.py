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

    def get(self):#calling my function and where it begins
        pg = page1() #pg is stored as simple variable

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
            self.response.write(pg.page_header + pg.page_content + pg.page_end) #writes to our browser page
        #if no info, display form
        else:
            self.reponse.write(pg.page_header + pg.page_content + pg.page_end)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
