

# Functions go here...
def yes_no ( question ):
    valid = False
    while not valid: 
        response = input(question).lower()
    
        if response == "yes" or response == "y": 
             response = "yes"
             return response
            
        elif response == "no" or response == "n":
            response = "no"
            return response 
        else:
         print("Please answer yes / no")



def instructions():
    print("**** How to Play ****")
    print()
    print("Choose a starting amount (minimum $1, maximum $10. "
           
           "Then press <enter> to play."
           "You will get either a horse, a zebra, a donkey or a unicorn. "
            
            "It costs $1 per round.  Depending on your prize you might win"
            "some money back. Here's the payout amounts... "
             "Unicorn: $5.00 (Balance increases by $4)"
             "Horse: $0.50 (balance decreases by $0.50)"
             "Zebra: $0.50 (balance decreases by $0.50)"
             "Donkey: $0.00 (balance decreases by $1")


    return ""

# Main routine goes here...
Played_before = yes_no("Have you played this game before?")


if Played_before == "no":
    instructions()
    
print("Program continues")
