'''
__author__ = 'NenaH77'
Angelica M. Dinh
Assignment MadLib
Sept 3, 2014
DPW

'''


#input field string and dictionary
string = dict()
string = {
    "name1": raw_input("Enter a name "),
    "adj": raw_input("Enter an adjective "),
    "adj1": raw_input("Enter another adjective ")
}

#input field number
year_born = raw_input("Enter the year you were born ")
machine = raw_input("Enter a number from 0-2 ")
body = raw_input("Enter a number from 0-3 ")


#need to create dictionary objects as variables
name1 = string["name1"]
adj = string["adj"]
adj1 = string["adj1"]

#function
def height(inch, ft):
     tall = int(inch/ft)
     return tall
willie_tall = height(600, 12);

#function
year = 2014
def willie_age(y, yb):
    age = ((y - int(yb)) + 10)/2
    return age
a = willie_age(year, year_born);

#array 1
machine_array = ["shrinking", "enlarging", "evaporating"]

#conditional 1
def machine_select(num):
    if num == 0:
        return machine_array[0]
    elif num == 1:
        return machine_array[1]
    elif num == 2:
        return machine_array[2]
    else:
        return "machine gun"

weapon = machine_select(int(machine))

#array 2
body_array = ["hand", "foot", "backside", "stomach"]

#conditional 2
def body_part(num):
    if num == 0:
        return body_array[0]
    elif num == 1:
        return body_array[1]
    elif num == 2:
        return body_array[2]
    elif num == 3:
        return body_array[3]
    else:
        return "head"

b = body_part(int(body))



import random  #http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python

#array 3
disney = ["Mickey Mouse", "Donald Duck", "Goofy", "Pluto"]
#loop 1
random.shuffle(disney)
for d in disney:
    pass
#array 4
d_villain = ["Pete", "Mortimer Mouse", "Phantom Blot", "Emil Eagle"]
#loop 2
random.shuffle(d_villain)
for dv in d_villain:
    pass

story = '''
    Today, {name1} dreamt he/she was playing with {d} and all his pals. They were playing a fun game of tag
    at Clubhouse Mickey. Suddenly an overcast appeared and up in the sky a(n) {adj} ship flew over
    them. It began {weapon} everything in sight. {name1} wondered who would do such a thing to her best
    friends. He/She noticed that {dv} was inside the ship laughing at the horrible thing he was doing to
    her friends. They needed to somehow take his {weapon} machine from him. They decided to call Willie
    the Giant to come help. Willie the Giant was {a} years old and {willie_tall} ft tall. As they ran over
    towards him to warn him about the ship, he was coming down the bean stalk. Luckily the ships back was faced towards
    him and as he came down, he blocked the ships view with his {adj1} {b}. {name1} lassoed
    a rope around the ships nose and all his/her friends grabbed a hold of the rope and pulled down
    until the ship crashed into a tree. The clubhouse was saved and all of {name1}\'s friends cheered and danced to
    the Hot Dog Dance.
    The End
'''
story = story.format(**locals())
print story

