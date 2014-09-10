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
        #van's salary
        van = Salary() #instance of my object
        van.hr_worked = 40
        van.hourly = 60.00
        van.monthly = 9600
        van.annually = 0
        van.calc_total()
        self.response.write(van.earn)

        #lily's salary
        lily = Salary() #instance of my object
        lily.hr_worked = 40
        lily.hourly = 26.00
        lily.monthly = 4160
        lily.annually = 0
        lily.calc_total()
        self.response.write(lily.earn)


class Salary(object):
    def __init__(self):
       self.hr_worked = 0 #public
       self.hourly = 0
       self.monthly = 0
       self.annually = 0
       self.__earn = 0 #private

    @property #getters
    def earn(self): #defining my function
        return self.__earn #getters are always returned

    @earn.setter #setter
    def earn(self, new_earn):
        self.__earn = new_earn



    def calc_total(self): #calculate earnings
        self.__earn = (((self.hourly * self.hr_worked)*52)/12)






















        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
