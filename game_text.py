import settings
import sys, random, time


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)


def init():
    global player
    global take_bus_text()


def take_bus_text():
    print("\n")
    print_slow("You took a bus!\n")
    print("\n")
    print_slow("You sit down next to a peculiar looking gentleman\n")
    print_slow("You notice the man is staring at you, but you don't respond...\n")
    print_slow("As the bus makes its way to the airport, you continue to ignore the staring man...\n")
    print_slow("Finally, you decided you've had enough, and you confront him!\n")
    print("\n")
    print_slow(f'{player}: "Can I help you???"\n')
    print_slow('Man: "..."\n')
    print_slow('Man: "..."\n')
    print_slow('Man: "Are you talking to me?"\n')
    print_slow(f'{player}: "Yes obviously I am talking to you! You are staring at me!"\n')
    print_slow('Man: "Oh yes, I was, but I was really just wondering something..."\n')
    print_slow(f'{player}: "Wondering what?"\n')
    print_slow('Man: "Well, you look very smart, and I need help with something"\n')
    print_slow('Man: "I forgot the security questions for my Disney+ account, and now I cannot log in "\n')
    print_slow(f"{player}: We've all been there...\n")
    print_slow('Man: "Would you mind helping me out?"\n')
    print_slow(f'{player}: *reluctantly takes headphones out of ears* "sure..."\n')
    print_slow('Man: "Thanks! Here are the questions!...\n')
    print_slow('Man: "You will need to get at least 2 out of 4 right!"\n')
    print("\n")