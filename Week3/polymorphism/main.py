'''
name: Angelica Dinh
date: sept 15, 2014
class: dpw
lab: polymorphism

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [ ['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit'] ]
        self.response.write(p.print_out_form())

class Page(object):#borrowing stuff from the object class
    def __init__(self): #constructor
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body> '''

        self._body = 'Filler'
        self._close = '''
    </body>
</html> '''

    def print_out(self):
        return self._head + self._body + self._close


#in order to create a class in the same doc that inherits from Page, it has to be after Page

#inherits from Page This is the class that is the superclass for FormPage. FormPage gets to use any public and protected attributes and methods of the parent class
class FormPage(Page):
    def __init__(self):
        #2 ways to write:
        #1. Page.__init__()    or   2. super(FormPage, self).__init__()
        super(FormPage, self).__init__()#constructor function for the super class
        #create attributes for FormPage.
        self._form_open = '<form method = "GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        #<input type="text" value="" name="first_name" placeholder="First Name" />
        #['first_name', 'text', 'First Name']
        #<input type="text" value="" name="last_name" placeholder="Last Name" />
        #<input type="submit" value="" name="Submit" />



    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        #sort through the mega array and create HTML inputs based on the info there
        #print arr
        for item in arr:
            #print item
            self._form_inputs += '<input type="' +item[1]+ '"name="' + item[0]
            #if there is a 3rd item.. add it in....
            if len(item) >2:
                self._form_inputs += '"placeholder="' + item[2]+'" />'
            #otherwise.. end the tag
            else:
                self._form_inputs += '" />'

        print self._form_inputs


    def print_out_form(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
