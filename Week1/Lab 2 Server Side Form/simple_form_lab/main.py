'''
name: Angelica M. Dinh
date: Sept 8, 2014
class: DWP
assignment: Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_open = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Orlando Singles</title>
    </head>
    <body> '''

        page_content = '''<form method="GET" action="" >
        <label for="first_name">First Name </label>
        <label for="last_name">Last Name </label>
        <label for="email">Email </label>

        <input class="input" type="text" name="first_name" placeholder="Enter your First Name" required />
        <input class="input" type="text" name="last_name" placeholder="Enter your Last Name"  required />
        <input class="input" type="email" name="email" placeholder="johndoe@yahoo.com" required />






























        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
