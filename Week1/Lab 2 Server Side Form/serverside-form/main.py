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
        <label for="first_name">First Name: </label>
        <input class="input" type="text" name="first_name" placeholder="Enter your First Name" required />
        <label for="last_name">Last Name: </label>
        <input class="input" type="text" name="last_name" placeholder="Enter your Last Name"  required /><br>
        <label for="email">Email Address: </label>
        <input class="input" type="email" name="email" placeholder="johndoe@yahoo.com" required /><br>

        <label for="aboutyou">About You: </label><br>
        <textarea class="input" name="about-you"></textarea><br>
        <label for=religion">Religion:</label>
        <select class="input">
            <option value="non">Non Believer</option>
            <option value="catholic">Catholic</option>
            <option value="baptist">Baptist</option>
            <option value="nond">Non Denominational</option>
        </select><br>
        <label for="gender">Gender:</label><br>
        <input type="radio" name="gender" value="male">Male<br>
        <input type="radio" name="gender" value="female">Female










        '''










        self.response.write(page_open + page_content)















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
