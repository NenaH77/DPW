'''
name: Angelica M. Dinh
date: Sept 6, 2014
class: DWP
assignment: Simple Form
'''

import webapp2  #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Catalyst (something that starts a reaction

#GET = friendlier to work with, visible, part of the URL, and has character limitations. POST = something secure. It allows for more characters to be sent at one time. Hidden


        page = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>
        <form method="GET">
            <label>Name: </label><input type="text" name="user"/>
            <label>Email: </label><input type="text" name="email"/>
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
        '''
        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['user'] #must match the info from above
            email = self.request.GET['email']

        self.response.write(page) #prints our info out



#NEVER TOUCH THIS
app = webapp2.WSGIApplication([ #variable calling a method....NEVER TOUCH!!!!!!!
    ('/', MainHandler)
], debug=True)
