import random
from time import gmtime, strftime
clock = strftime("%a, %d %b %Y and the time is %H:%M:%S", gmtime())


quiz_questions = [
    "What is the collective noun for a group of pandas?\n(a) A group\n(b) A bunch \n(c) An embarrassment\n\n",
    "Which country do kiwifruit originate from?\n(a) New Zealand\n(b) China\n(c) Australia\n\n",
    "What is a Rocky Mountain oyster?\n(a) Bull testicles\n(b) An oyster from Rocky Mountain\n(c) A fish\n\n",
    "What is the correct term for a question mark combined with an exclamation mark?\n(a) An exlamuestion mark\n(b) An interrobang\n(c) An interrogamation\n\n"
]


def guess_number():
    print("number game")


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(quiz_questions[0], "c"),
    Question(quiz_questions[1], "b"),
    Question(quiz_questions[2], "a"),
    Question(quiz_questions[3], "b")
]


def run_quiz(questions):
    """
    Runs the quiz game when player chooses the bus path.
    """
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)}")


def take_bus():
    """
    Runs if player chooses the bus path.
    """
    print("You took a bus")
    run_quiz(questions)
    print("Well done, take this free hand sanitizer and enjoy your trip!")
    guess_number()


def take_taxi():
    """
    Runs if player chooses the taxi path.
    """
    print("You took a taxi")
    guess_number()


def intro():
    """
    Intro to the game, presents player with first choice
    """
    print(f"It's {clock}, you're in Amsterdam")
    print("you just realised you were supposed to be in Dublin")
    print("for a family event in 8 hours! \n")
    FirstChoice = input("You better hurry up, how do you want to get to the airport, bus or taxi? ").lower()
    if FirstChoice == 'bus':
        take_bus()
    else:
        take_taxi()


player = input("What is your name, traveller? ")
answer = input(f"Hello {player}, are you ready to start your journey? (Y/N) ")

while answer == "y" or "n":
    if answer == "y":
        intro()
    elif answer == "n":
        print("That's understandable, flying isn't what it used to be anyway")
        quit()
    else:
        print("Please type 'y' or 'n'")
        answer = input(f"Hello {player}, are you ready to start your journey? (Y/N) ")

