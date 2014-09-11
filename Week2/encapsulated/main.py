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
        van.hourly = 60
        van.weekly = 2400
        van.monthly = 9600
        van.annually = 124800
        van.calc_gross_total()
        self.response.write("<br /> Van's weekly earning $" + str(van.earn_weekly))
        self.response.write("<br /> Van's monthly earning $" + str(van.earn_month))
        self.response.write("<br /> Van's annual earning $" + str(van.earn_annual))
        self.response.write("<br /> Van's Net Pay $" + str(van.net_pay))

        #lily's salary
        lily = Salary() #instance of my object
        lily.hr_worked = 40
        lily.hourly = 26
        lily.weekly = 1040
        lily.monthly = 4160
        lily.annually = 54080
        lily.calc_gross_total()
        self.response.write("<br /> Lily's weekly earning $" + str(lily.earn_weekly))
        self.response.write("<br /> Lily's monthly earning $" + str(lily.earn_month))
        self.response.write("<br />Lily's annual earning $" + str(lily.earn_annual))
        self.response.write("<br />Lily's Net Pay $" + str(lily.net_pay))

class Salary(object):
    def __init__(self):
       self.hr_worked = 0 #public
       self.hourly = 0
       self.weekly = 0
       self.monthly = 0
       self.annually = 0
       self.earn_weekly = 0
       self.__earn_month = 0 #private
       self.__earn_annual = 0 #private

    #weekly pay
    @property #getters
    def earn_weekly(self): #defining my weekly function
        return self.__earn_weekly #getters are always returned

    @earn_weekly.setter #setter
    def earn_weekly(self, new_earn_weekly):
        self.__earn_weekly = new_earn_weekly

    #monthly pay
    @property #getters
    def earn_month(self): #defining my monthly function
        return self.__earn_month #getters are always returned

    @earn_month.setter #setter
    def earn_month(self, new_earn_month):
        self.__earn_month = new_earn_month

    #annual pay
    @property #getters
    def earn_annual(self): #defining my annual function
        return self.__earn_annual #getters are always returned

    @earn_annual.setter #setter
    def earn_annual(self, new_earn_annual):
        self.__earn_annual = new_earn_annual

    #net pay
    @property
    def net_pay(self):
        return self.__net_pay

    @net_pay.setter
    def net_pay(self, new_net_pay):
        self.__net_pay = new_net_pay

    # gross total
    def calc_gross_total(self): #calculate earnings
        self.__earn_weekly = (self.hr_worked * self.hourly)
        self.__earn_month = ((self.hourly * self.hr_worked)* 52)/ 12
        self.__earn_annual = (self.hourly * 2080)
        self.__net_pay = ((self.earn_weekly * .20) - (.05 * self.earn_weekly) - (75 - self.earn_weekly))























app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
