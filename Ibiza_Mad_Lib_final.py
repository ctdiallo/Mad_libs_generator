## Victoria, Saqif, Tidiane 
# story
# I travelled to Ibiza by .... 
# The moment I arrived, I was ... surprised by the vibrant ... that took my breath away.
# The weather is usually ..., perfect for dancing at the cool beach parties.
# The temperature often reaches around ...°C, making it even more enjoyable.
# At times, you even get the chance to see top DJs such as ..., or Kerri Chandler live on a set.
# It's the perfect place to unwind and ... cool memories.

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