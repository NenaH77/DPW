'''

name: Angelica M. Dinh
date: Sept 4, 2014
class: dpw
lab: classes

'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button() #create button variable. about_button is an instance of the Button() class
        #about_button.click() #call click outside of the class enviornment
        about_button.label = "About Us"
        about_button.show_label()

        contact_button = Button() #Button() class will create the button class below and also call the constructor method 'def _init_(self)' below
        contact_button.label = "Contact Us"
        contact_button.show_label()

class Button(object): #(object)holds information about what this class inheritance from
    def _init_(self): #constructor method
        #print "constructor method of button ran"
        #self.click() #remember cuz self in 'def click(self)' is the only parameter in there we don't need to send any arguments

        self.label = " "     #public attribute uses . dot
        self.__size = 60 #private attribute uses  __ two underscores
        self._color = "0x00000" #protected attribute  _ one underscore

        #self.on_roll_over("Hello!!")   #if we wanted to call 'on_roll_over', and we wanted to pass a message. We need to add
                                        #message to the bottom method as a parameter and add an argument for that.
                                        #***REMEMBER*** we don't need to worry about passing an argument for 'self' cuz it takes care of itself

        #height = 40 #will not work when we use in show_label method because it needs to be 'self.height'

    def click(self): #self is equivalent of "this" in JS. Self represents the instance of 'this' button class
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over my button" + message

    def show_label(self):
        print "My label is " + self.label #we use 'self' because it represents all instances of this class; # + "height" + height We need to have self.height for it to work as well as above in 'def _init_'

''' in this example we have 3 methods: 1. constructor method def_init_self 2. click method 3. roll_over method
    To access our methods, type self.click(), self.on_roll_over under constructor method "def _init_(self): '''



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
