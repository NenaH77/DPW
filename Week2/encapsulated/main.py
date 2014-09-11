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
        #van.weekly = 2400
        #van.monthly = 9600
        #van.annually = 124800
        van.calc_total()
        self.response.write("<br /> Van's weekly earning <br /> $" + str(van.earn_weekly))
        self.response.write("<br /> Van's monthly earning <br /> $" + str(van.earn_month))
        self.response.write("<br /> Van's annual earning <br /> $" + str(van.earn_annual))
        self.response.write("<br /> Van's federal income <br /> $" + str(van.federal_income))
        self.response.write("<br /> Van's pension <br /> $" + str(van.pension_plan))
        self.response.write("<br /> Van's deductions <br /> $" + str(van.deductions))
        self.response.write("<br /> Van's Net Pay <br /> $" + str(van.net_pay))

        #lily's salary
        lily = Salary() #instance of my object
        lily.hr_worked = 40
        lily.hourly = 26
        lily.weekly = 1040
        lily.monthly = 4160
        lily.annually = 54080
        lily.calc_total()
        self.response.write("<br /> Lily's weekly earning <br /> $" + str(lily.earn_weekly))
        self.response.write("<br /> Lily's monthly earning <br /> $" + str(lily.earn_month))
        self.response.write("<br />Lily's annual earning <br /> $" + str(lily.earn_annual))
        self.response.write("<br /> Lily's federal income <br /> $" + str(lily.federal_income))
        self.response.write("<br /> Lily's pension <br /> $" + str(lily.pension_plan))
        self.response.write("<br /> Lily's deductions <br /> $" + str(lily.deductions))
        self.response.write("<br />Lily's Net Pay <br /> $" + str(lily.net_pay))

        #adriana's salary
        adriana = Salary() #instance of my object
        adriana.hr_worked = 40
        adriana.hourly = 20
        adriana.weekly = 800
        adriana.monthly = 3466
        adriana.annually = 41600
        adriana.calc_total()
        self.response.write("<br /> Adriana's weekly earning <br /> $" + str(adriana.earn_weekly))
        self.response.write("<br /> Adriana's monthly earning <br /> $" + str(adriana.earn_month))
        self.response.write("<br />Adriana's annual earning <br /> $" + str(adriana.earn_annual))
        self.response.write("<br /> Adriana's federal income <br /> $" + str(adriana.federal_income))
        self.response.write("<br /> Adriana's pension <br /> $" + str(adriana.pension_plan))
        self.response.write("<br /> Adriana's deductions <br /> $" + str(adriana.deductions))
        self.response.write("<br />Adriana's Net Pay <br /> $" + str(adriana.net_pay))


        #alexandra's salary
        alexandra = Salary() #instance of my object
        alexandra.hr_worked = 36
        alexandra.hourly = 16
        alexandra.weekly = 576
        alexandra.monthly = 2496
        alexandra.annually = 33280
        alexandra.calc_total()
        self.response.write("<br /> Alexandra's weekly earning <br /> $" + str(alexandra.earn_weekly))
        self.response.write("<br /> Alexandra's monthly earning <br /> $" + str(alexandra.earn_month))
        self.response.write("<br />Alexandra's annual earning <br /> $" + str(alexandra.earn_annual))
        self.response.write("<br /> Alexandra's federal income <br /> $" + str(alexandra.federal_income))
        self.response.write("<br /> Alexandra's pension <br /> $" + str(alexandra.pension_plan))
        self.response.write("<br /> Alexandra's deductions <br /> $" + str(alexandra.deductions))
        self.response.write("<br />Alexandra's Net Pay <br /> $" + str(alexandra.net_pay))


#html
    page_head = '''
<!DOCTYPE html>
	<html>
		<head>
			<title>Salary Calculator</title>
            <link rel="stylesheet" type="text/css" href="css/style.css">
		</head>
		<body>
    '''
    page_body = '''
        <div id="wrapper">
            <header>
            
            </header>
        </div>






    page_close = '''
    	</body>
    </html>
    '''


















class Salary(object):
    def __init__(self):
       self.hr_worked = 0 #public no underscores
       self.hourly = 0
       self.weekly = 0
       self.monthly = 0
       self.annually = 0
       self.__earn_weekly = 0 #private 2underscores
       self.__earn_month = 0
       self.__earn_annual = 0
       self.__federal_income = 0
       self.__pension_plan = 0
       self.__medical_ins = 0
       self.__deductions = 0
       self.__net_pay = 0


    #weekly pay
    @property #getters
    def earn_weekly(self): #defining my weekly function
        return self.__earn_weekly #getters are always returned

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
    def calc_total(self): #calculate earnings
        self.__earn_weekly = (self.hr_worked * self.hourly)
        self.__earn_month = ((self.hourly * self.hr_worked)* 52)/ 12
        self.__earn_annual = (self.hourly * 2080)
        self.__federal_income = (self.earn_weekly * .20)
        self.__pension_plan = (self.earn_weekly * .05)
        #self.__medical_ins = (75.00)
        self.__deductions = (self.federal_income - self.pension_plan - 75)
        self.__net_pay = (self.earn_weekly - self.deductions)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
