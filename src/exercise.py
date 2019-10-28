#=================Strings=====================#
hello_string = "Hello String yo i am the hello string"
""" I am a long string """
#F strings
name= "Bryce"
age= 19
f"Hello, {name}"
#EOL === End of line
f"Hello, i am {name} and i am {int(age)} "

rent = 439
per_day = rent / 30
print(per_day)
print(f"My name is {name} and i am {int(age)}")
name
f"Hello, my name is {name}. I pay ${rent/30} per pay in rent"
dir(int)

#================Functions========================#
"""Functions in python """
def foonction():
        print(f"Hello!")
    

foonction()

def meaning_of_life():
    return 42;
    
meaning_of_life()

def add_numbers(x,y):
    return x + y

add_numbers(2,4)

def greeting(person):
    greeting = "Hello "
    return greeting + person

greeting("Cutie <3")

#function arguments

def say_greeting(name,greeting="Hello"):
    return greeting + name


say_greeting("Bryce")

#Default args can be overwritten and always come last


say_greeting("Bryce",greeting="yeet")


#positional arguments are always required


def create_query(language="JS",num_stars=50, sort="desc"):
    return f"Language: {language}, Number of stars : {num_stars},{sort}"


create_query(language="Python")

#if you label your args position doesn't matter


#never use Default types as args

def twitter_info():
    account = "Bryce"
    print(f"Account inside of scope  {account}")
    

def try_change_name(name="Yeet"):
    name="max"
    print(f"Name inside Function {name}")
    
try_change_name(name="bryce")


#dont put empty lists as a parameter it causes bugs

def foo(a,b=None):
    if b is None:
        b = []
    b.append(a)
    return b

