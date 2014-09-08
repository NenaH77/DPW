'''
name: Angelica M. Dinh
date: Sept 8, 2014
class: DWP
assignment: Simple Form
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):#where my function begins
        p = page() #p represents class page(object) from page.py


        if self.request.GET:
            #stores info from the variable form
            first_name = self.request.GET['first_name']
            last_name = self.request.GET['last_name']
            email = self.request.GET['email']
            phone = self.request.GET['phone']
            aboutyou = self.request.GET['about-you']
            religion = self.request.GET['religion']
            edu = self.request.GET['edu']
            gender = self.request.GET['gender']
            ethnicity = self.request.GET['ethnicity']

            #call print function (displays info)
            self.response.write(p.print_out(all)) #writes to our browser page
        else:
            self.response.write(p.print_out(" "))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
