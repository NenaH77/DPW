__author__ = 'NenaH77'

#print "hello world!"

#one lined commnets
'''
multiple line commnets

Doc strings
'''

'''http://legacy.pythong.org/dev/peps/pop-0008/'''
#no camel case. Use underscores
first_name = "Kermit"
last_name = "de Frog"
print first_name

response = raw_input("Enter you name  ")
print "Hello there, " , response


#expressions
birth_year = 1923
current_year = 2014
age = current_year - birth_year
print age


birth_year = 1923
current_year = 2014
age = current_year - birth_year
print "You are " + str(age) + " years old" # You can not concatenate strings and Integers. Will need to fix using str()
# strings to numbers: int(variable)

#condition
'''if condition:
    #stuff to do'''


'''
budget = 200

if budget > 100:
    brand = "nike"
    print "Yay! we can buy cool " +brand+ " shoes!"
else:
    print "No cool shoes for me."
'''

'''
budget = 90

if budget > 100:
    brand = "nike"
    print "Yay! We can buy cool " +brand+ " shoes!"
elif budget > 50:
    print "We can at least get some generic sneakers"
else:
    print "No cool shoes for me."
'''

'''
budget = 90

if budget > 100:
    brand = "nike"
    print "Yay! We can buy cool " +brand+ " shoes!"
elif budget > 50:
    print "We can at least get some generic sneakers"
else:
    pass   #pass allows you to move on

print "hi"
'''


#Arrays
'''
characters = ["leia", "luke", "chewy", "lando"]
print characters
'''

'''
characters = ["leia", "luke", "chewy", "lando"]
characters.append("obi won")
print characters
'''


characters = ["leia", "luke", "chewy", "lando"]
characters.append("obi won")
print characters[0]

#Dictionary object
movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
print movies["Star Wars"]

#While Loops -----
'''
i = 0
while i<9:
    print "The while loop count is", i
    i = i+1
'''


#for Loop ------
'''
for i in range(0,10):
    print "The for loop count is", i
    i = i + 1
'''

# for each loop -----
rappers = ["Tupac", "Nas", "Biggie Smalls"]
for r in rappers:
    print "One of the best rappers is " + r
    pass

#functions ------
'''
def calcArea(h, w):
    area = h * w
    print area
    return area

calcArea(20, 40);
'''

'''
def calcArea(h, w):
    area = h * w
    return area

a = calcArea(20, 40);
print "My area is " + str(a) + "sq ft"
'''

#scope
x = 2

def calcArea(h, w):
    area = h * w
    return area + x

a = calcArea(20, 40);
print a


weight = 200
height = 63
message = '''
Your height is {height} and your weight is {weight}
'''

message = message.format(**locals())
print message



title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''

message = message.format(**locals())
print message































