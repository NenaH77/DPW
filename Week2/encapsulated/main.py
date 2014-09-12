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
        #self.van.weekly = 2400
        self.van.calc_total()

        #lily's salary
        self.lily = Salary() #instance of my object
        self.lily.name = "Lily Smith"
        self.lily.hr_worked = 40
        self.lily.hourly = 26
        #self.lily.weekly = 1040
        self.lily.calc_total()


        #adriana's salary
        self.adriana = Salary() #instance of my object
        self.adriana.name = "Adriana Gomez"
        self.adriana.hr_worked = 40
        self.adriana.hourly = 20
        #self.adriana.weekly = 800
        self.adriana.calc_total()



        #alexandra's salary
        self.alexandra = Salary() #instance of my object
        self.alexandra.name = "Alexandra White"
        self.alexandra.hr_worked = 36
        self.alexandra.hourly = 16
        #self.alexandra.weekly = 576
        self.alexandra.calc_total()


        #making array for person's salary link; when link is clicked info will display
        person = [self.van, self.lily, self.adriana, self.alexandra]

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

            #results are displayed once person has been selected
            result = '''
            <div class="content">
            <h2>{name}</h2>
                <section class="labels">
                    <p class="info">Hours Worked:</p>
                    <p class="info">Hourly Pay:</p>
                    <p class="info">Gross Check:</p>
                </section>

                <section class="labels">
                    <p class="info">{hr_worked}</p>
                    <p class="info">{hourly}</p>
                    <p class="info">{earn_weekly}</p>
                </section>
            </div>'''

            #formats local variable (which is my result)
            result = result.format(**locals())

            #writes my closing page
            self.response.write(result)
            self.response.write(p.page_close)


class Salary(object):
    def __init__(self):
        self.name = ""
        self.hr_worked = 0 #public no underscores
        self.hourly = 0
        self.__earn_weekly = 0 #private 2underscores


    #weekly pay
    @property #getters
    def earn_weekly(self): #defining my weekly function
        return self.__earn_weekly #getters are always returned

    @earn_weekly.setter #setter
    def earn_weekly(self, new_earn_weekly):
        self.__earn_weekly = new_earn_weekly

    #total
    def calc_total(self): #calculate earnings
        total = self.hr_worked * self.hourly
        self.__earn_weekly = total



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
