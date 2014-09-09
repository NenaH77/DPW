'''
name: Angelica M. Dinh
date: Sept 8, 2014
class: DWP
assignment: Simple Form
'''


import webapp2

#import file
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):#calling my function and where it begins
        page = Page() #pg is stored as simple variable

        if self.request.GET:
            #stores info that user submits in form
            fn = self.request.GET['first_name']
            ln = self.request.GET['last_name']
            em = self.request.GET['email']
            ph = self.request.GET['phone']
            ay = self.request.GET['aboutyou']
            rel = self.request.GET['religion']
            edu = self.request.GET['edu']
            gend = self.request.GET['gender']
            eth = self.request.GET['ethnicity']

            #displays function (displays info)
            self.response.write(page.page_header + page.page_content + fn + ln + em + ph + ay + rel + edu + gend + eth + page.page_end) #writes to our browser page
            #if no info, display form
        else:
            #displays original form
            self.response.write(page.page_header + page.page_content + page.page_end)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
