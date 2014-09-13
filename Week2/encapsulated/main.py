'''
name: Angelica Dinh
date: sept 10, 2014
class: dpw
assignment: encapsulated calculator

'''
import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        #create an instance of my Class Salary
        #van's salary
        self.van = Salary() #instance of my object
        self.van.name = "Van Chow"
        self.van.hr_worked = 40
        self.van.hourly = 60
        self.van.earn_weekly = 2400
        self.van.calc_total()

        #lily's salary
        self.lily = Salary() #instance of my object
        self.lily.name = "Lily Smith"
        self.lily.hr_worked = 40
        self.lily.hourly = 26
        self.lily.earn_weekly = 1040
        self.lily.calc_total()


        #adriana's salary
        self.adriana = Salary() #instance of my object
        self.adriana.name = "Adriana Gomez"
        self.adriana.hr_worked = 40
        self.adriana.hourly = 20
        self.adriana.earn_weekly = 800
        self.adriana.calc_total()



        #alexandra's salary
        self.alexandra = Salary() #instance of my object
        self.alexandra.name = "Alexandra White"
        self.alexandra.hr_worked = 36
        self.alexandra.hourly = 16
        self.alexandra.earn_weekly = 576
        self.alexandra.calc_total()



        #making array for person's salary link; when link is clicked info will display
        person = [self.van, self.lily, self.adriana, self.alexandra]
        print person

        #writes header, body and close onto the page
        self.response.write(p.page_header + p.page_body)

        #if info is received
        if self.request.GET:
           #this should call the person from page.py. example: link to <a href="?name=van">
            salary = int(self.request.GET['salary'])

            #gathering info on selected player
            name = person[salary].name
            hr_worked = person[salary].hr_worked
            hourly = person[salary].hourly
            earn_weekly = person[salary].earn_weekly
            net = person[salary].net_pay

            #results are displayed once person has been selected
            result = '''
            <div class="content">
            <h2>{name}</h2>
                <section class="labels">
                    <p class="info">Hours Worked: {hr_worked}</p>
                    <p class="info">Hourly Pay: {hourly}</p>
                    <p class="info">Gross Income: ${earn_weekly}</p>
                    <p class="info">Net Pay: ${net}</p>
                </section>
            </div>'''

            #formats local variable (which is my result)
            result = result.format(**locals())

            #writes my result and closing page
            self.response.write(result)
            print result
        self.response.write(p.page_close)


#public no underscores
#private 2underscores
class Salary(object):
    def __init__(self):
        self.name = ""
        self.hr_worked = 0
        self.hourly = 0
        self.annually = 0
        self.monthly = 0
        self.__earn_weekly = 0
        self.__earn_month = 0
        self.__earn_annual = 0
        self.__federal_income = 0
        self.__pension_plan = 0
        self.__medical_ins = 0
        self.__deductions = 0
        self.__net_pay = 0



    #weekly pay
    @property #getters
    #defining my weekly function
    def earn_weekly(self):
        #getters are always returned
        return self.__earn_weekly

    @earn_weekly.setter #setter
    def earn_weekly(self, new_earn_weekly):
        self.__earn_weekly = new_earn_weekly

    #monthly pay
    @property #getters
    def earn_month(self):
        return self.__earn_month

    @earn_month.setter #setter
    def earn_month(self, new_earn_month):
        self.__earn_month = new_earn_month

    #annual pay
    @property #getters
    def earn_annual(self):
        return self.__earn_annual

    @earn_annual.setter #setter
    def earn_annual(self, new_earn_annual):
        self.__earn_annual = new_earn_annual

    #federal income
    @property
    def federal_income(self):
        return self.__federal_income

    @federal_income.setter
    def federal_income(self, new_federal_income):
        self.__federal_income = new_federal_income


    #pension plan
    @property
    def pension_plan(self):
        return self.__pension_plan

    @pension_plan.setter
    def pension_plan(self, new_pension_plan):
        self.__pension_plan = new_pension_plan

    #deductions
    @property
    def deductions(self):
        return self.__deductions

    @deductions.setter
    def deductions(self, new_deductions):
        self.__deductions = new_deductions

    #net pay
    @property
    def net_pay(self):
        return self.__net_pay

    @net_pay.setter
    def net_pay(self, new_net_pay):
        self.__net_pay = new_net_pay


    #total
    #calculate earnings
    def calc_total(self):
        gross = self.hr_worked * self.hourly
        self.__earn_weekly = gross

        deduction = self.federal_income - self.pension_plan - 75
        self.__deductions = deduction

        total = self.earn_weekly - self.deductions
        self.net_pay = total


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
