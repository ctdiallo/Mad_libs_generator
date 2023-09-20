## Assignment 3: Mad Lib Ibiza
"""
Inspired by Summer Son’s Mad Libs project with Javascript. 
The program will first prompt the user for a series of inputs a la Mad Libs. 
For example, a singular noun, an adjective, etc. Then, once all the 
information has been inputted, the program will take that data and 
place them into a premade story template. You’ll need prompts for 
user input, and to then print out the full story at the end with 
the input included.
"""

## Concepts to keep in mind: 
"""
Strings 
Variables 
Concatenation 
Print Deliverables
"""
"""
A pretty fun beginning project that gets you thinking about how to manipulate user inputted data. 
Compared to the prior projects, this project focuses far more on strings and concatenating. 
Have some fun coming up with some wacky stories for this!
"""

## Understating of the problem
"""
I should setup many inputs that will be placed at specific places in the story. 
These can be: Noun, place, number, adverb, food, adj, verb...
Inputs should look like this noun = , adj = input("enter an adjective: )
once inputs ready these should be inserted in the right place in the text.
"""

## 2 What's the plan?
"""
1/ Have the whole story ready
2/ Take bits and set them as inputs. inp1 = inp2....
3/ Create gaps in the text according to inputs
4/ Create the variables and inputs
4/ Start each sentence with print. 
5/ Set a cool closing sentence
"""


## 3 Declare inputs
"""
verb : went
adverb: pleasantly
noun: landscape
adjective: balmy
dj: Black Coffee
temperature (°C): 30
verb: create
"""
##########################################################################################

## 4 Implement the Code
"""
Our Mad Lib project incorporate the following data type and methods:
list
string
concatenation
f-string for print
for loop
"""
## story
## I went to Ibiza. 
# The moment I arrived, I was pleasantly surprised by the vibrant landscape that took my breath away.
# The weather is usually balmy, perfect for dancing at the cool beach parties.
# The temperature often reaches around 30°C, making it even more enjoyable.
# At times you even get the chance to see top DJs such as Black Coffee, or Kerri Chandler live on a set.
# It's the perfect place to unwind and create cool memories.

## greeting message
print("Welcome to Ibiza Mad Lib story")
print()

# Let's set the variables
verb1 = input("Enter a verb: ").strip().lower()
adverb = input("Enter an adverb: ").strip().lower()
noun = input("Enter a noun: ").strip().lower()
adjective = input("Enter an adjective: ").strip().lower()
dj = input("Name a DJ: ").strip().lower()
temperature = input("Enter a temperature (°C): ").strip().lower()
verb2 = input("Enter a verb: ").strip().lower()

## split the tasks line by line to isolate potential issues. Note line_2 has a f-string instead
# of concatenate. 

line_1 = "I " + verb1 + " to Ibiza. "
line_2 = f"The moment I arrived, I was {adverb} surprised by the vibrant {noun} that took my breath away. "
line_3 = "The weather is usually " + adjective + ", perfect for dancing at the cool beach parties. "
line_4 = "The temperature often reaches around " + temperature + "°C, making it even more enjoyable. "
line_5 = "At times, you even get the chance to see top DJs such as " + dj + ", or Kerri Chandler live on a set. "
line_6 = "It's the perfect place to unwind and " + verb2 +" cool memories. "


## Time to print the lines altogether
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(line_6)

print() ## will create an empty line

print("Thank you for playing with us! For any question about our Ibiza Mad Lib project please do not hesitate.")


## 5 Test
"""
Was fine
improvement ideas: loop to repeat the exercice, isdigit for the temperature, print all lines together
"""

##################################################################################
## VERSION 2 ADDED A LIST AND A FOR LOOP
## greeting message

## greeting message
while True:
    print("Welcome to Ibiza Mad Lib story\n")
    print("Game Instructions: Please fill in the blanks.")
    print() ## will create an empty line
    
    # Let's set the variables for all inputs
    transport_mode = input("How did you travel to Ibiza? ").strip().lower()
    adverb = input("Enter an adverb: ").strip().lower()
    noun = input("Enter a noun: ").strip().lower()
    adjective = input("How is the weather in Ibiza? ").strip().lower()
    temperature = input("Guess the temperature (°C): ").strip().lower()
    
    ## We ensure that a number is entered for the temperature
    while not temperature.isdigit():
        print("Please enter a number instead.")
        temperature = input("Guess the temperature (°C): ").strip().lower()
        
    dj = input("Name your favorite DJ: ").strip().lower()
    verb = input("Enter a verb: ").strip().lower()
        
    ## split the tasks line by line to isolate potential issues. Note line_2 has a f-string instea
    ## of concatenate. 
         
    line_1 = "I travelled to Ibiza by " + transport_mode + "."
    line_2 = f"The moment I arrived, I was {adverb} surprised by the vibrant {noun} that took my breath away. "
    line_3 = f"The weather is usually {adjective}, perfect for dancing at the cool beach parties. "
    line_4 = f"The temperature often reaches around {temperature}°C, making it even more enjoyable. "
    line_5 = f"At times, you even get the chance to see top DJs such as {dj}, or Kerri Chandler live on a set. "
    line_6 = f"It's the perfect place to unwind and {verb} cool memories. "

    print("\nNow let's put this altogether!\n")

    ## Time to gather all lines together inside a list and print the story
    Ibiza_mad_lib = [line_1, line_2, line_3, line_4, line_5, line_6]
    
    ## a for loop allows each item of the list to be printed
    for x in Ibiza_mad_lib:
        print(x)
    print() 
    
    ## finally we give the use the opportunity to try again
    repeat = input("Do you want to play again? (yes/no)").strip().lower()
    if repeat != "yes":
        print("\nThank you for playing with us! For any question about our Mad Lib project please do not hesitate.")
        break  ##Exit the loop