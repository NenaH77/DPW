__author__ = 'NenaH77'


#Array
disney = ["Mickey Mouse", "Donald Duck", "Goofy", "Pluto"]
d_villain = ["Pete", "Mortimer Mouse", "Phantom Blot", "Emil Eagle"]
machine_array = ["shrinking", "enlarging", "evaporating"]
body_array = ["hand", "foot", "back", "side"]

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


#used as dictionary object above. need to make into variables
name1 = string["name1"]
adj = string["adj"]
adj1 = string["adj1"]



#function
year = 2014
def willie_age(y, yb):
    age = ((y - int(yb)) + 10)/2
    return age
a = willie_age(year, year_born);

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


#loop 1
import random #http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python

for d in disney:
    random.choice(d)

#loop 2
for v in d_villain:
    random.choice(v)

story = '''
    Today, {name1} dreamt he/she was playing with {d} and his pals at Clubhouse Mickey.
    They were playing a fun game of superheros when all of a sudden an overcast appeared in mid air.
    There up in the sky a(n) {adj} ship flew over them and began {weapon} everything in sight. {name1} wondered
    who would do such a thing to her best friends. Suddenly he/she noticed {v_char[bad_guy]} in the ship. They needed
    to somehow take his {weapon} machine from him. Then they thought, what if they could ask Willie the Giant
    to come help. They ran to the Clubhouse and called him from the house phone. Willie the Giant was {a}
    years old and 50 ft tall. They ran over towards him to warn him about the ship, luckily the ships back
    was facing towards him. As he came down his farm house in the sky, he climbed down from the bean stalk
    and blocked the ships view with his {adj1} {b}. {name1} lassoed a rope around the ships nose and each
    friend grabbed a hold of the rope and pulled the it down until it crashed into a tree. The clubhouse
    was saved and all of {name1}'s friends cheered and danced to the Hot Dog Dance.
    The End
    '''
story = story.format(**locals())
print story