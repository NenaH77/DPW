'''
name: Angelica Dinh
date: sept 10, 2014
class: dpw
assignment: encapsulated calculator

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

#create an instance of my Class Salary
        van = Salary() #instance of my object
        van.hr_worked = 40
        van.hourly = 26.00
        van.monthly = 0
        van.annually = 0
        self.response.write()


class Salary(object):
    def __init__(self):
       self.hr_worked = 0
       self.hourly = 0
       self.monthly = 0
       self.annually = 0
       self.__pay_check = 0

    def calc_pay(self): #calculate pay
        self.__pay_check = ()






















        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
