'''
name: Angelica Dinh
date: sept 9, 2014
class: dpw
lab: encapsulation

'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #create 2 instances of the Transcript class

        #Tommy's grade
        t = Transcript() #instance of our object
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        t.final_grade = 99 #to use the setter BUT notice we need to add another class so we already have a getter/setter for final grade. We want the new calculations to take effect to tommy's grade and therefore the class calc_grade is necessary to add the new calculations.
        #print t.final_grade    #**REMEMBER** print displays on log console. self.response.write displays on browser
        self.response.write(t.final_grade) #access our getter. Needs to match function name

        #Sally's grade
        s = Transcript() #instance2 of our object
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76
        s.calc_grade()
        #print "Sally's final grade is " + str(s.final_grade)   #**Remember** final grade is a number so we need to concatenate final_grade with a string.
        self.response.write("<br />Sally's final grade is " + str(s.final_grade))


class Transcript(object):
    def __init__(self):
        self.grade1 = 0 #no underscores = public
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0 #2underscroes = private


#since __final grade is private, what do we do if we want to read & write to it, we need to create @decorator(getter & setter) for it

    @property #getter
    def final_grade(self): #define our function
        return self.__final_grade #getters are always returned

    @final_grade.setter #setter
    def final_grade(self, new_final_grade): #function needs 2 parameters for its argument
        self.__final_grade = new_final_grade #value

    def calc_grade(self): #class
        #calculate final grade BUT because we removed __final.grade calculation from the getter, we need to add calc_grade()method for sally
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
