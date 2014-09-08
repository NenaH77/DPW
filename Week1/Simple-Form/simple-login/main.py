'''
name: Angelica M. Dinh
date: Sept 6, 2014
class: DWP
assignment: Simple Form
'''

import webapp2  #use the webapp2 library

# GET = friendlier to work with, visible, part of the URL, and has character limitations.
# POST = something secure. It allows for more characters to be sent at one time. Hidden

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Catalyst (something that starts a reaction
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body> '''

        page_body = '''<form method="GET" action="">
        <label>Name: </label><input type="text" name="user"/>
        <label>Email: </label><input type="text" name="email"/>
        <input type="submit" value="Submit" />'''

        page_section = '''<br>
<a href="?email=mickey@disney.com&user=Mickey">Mickey</a><br/>
<a href="?email=donald@disney.com&user=Donald">Donald</a><br/>
<a href="?email=minnie@disney.com&user=Minnie">Minnie</a><br/>
<a href="?email=pluto@disney.com&user=Pluto">Pluto</a>
        '''

        page_close = '''
        </form>
    </body>
</html>'''

        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['user'] #must match the info from above
            # To access items
            #self.request.GET[]
            email = self.request.GET['email']
            # To print items
            #self.response.write()
            self.response.write(page_head + user + " " + email + page_body + page_section + page_close)
            #self.response.write(page_head + user + " " + email + page_close) #Will not display the input fields once names have been entered
        else:
            self.response.write(page_head + page_body + page_section + page_close)
            #self.response.write(page) #prints our info out



#NEVER TOUCH THIS
app = webapp2.WSGIApplication([ #variable calling a method....NEVER TOUCH!!!!!!!
    ('/', MainHandler)
], debug=True)
