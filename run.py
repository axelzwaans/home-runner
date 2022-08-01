from time import gmtime, strftime

clock = strftime ("%a, %d %b %Y and the time is %H:%M:%S", gmtime())

def intro():
    answer = input(f"It's {clock}, you're in Amsterdam and you just realised you were supposed to be in Dublin for a family event by the evening")


character = input("What is your name, traveller? ")
answer = input(f'Hello {character}, are you ready for your journey to London? (Y/N) ')


if answer.lower().strip() == "y":
    intro()
    

else:
    print("That's understandable, flying isn't what it used to be anyway")
        

