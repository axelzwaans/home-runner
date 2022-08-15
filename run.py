import sys, random, time
from time import gmtime, strftime
clock = strftime("%a, %d %b %Y and the time is %H:%M:%S", gmtime())
from random import randrange
from constants import *


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)


quiz_questions = [
    "What is the collective noun for a group of pandas?\n(a) A group\n(b) A bunch \n(c) An embarrassment\n\n",
    "Which country do kiwifruit originate from?\n(a) New Zealand\n(b) China\n(c) Australia\n\n",
    "What is a Rocky Mountain oyster?\n(a) Bull testicles\n(b) An oyster from Rocky Mountain\n(c) A fish\n\n",
    "What is the correct term for a question mark combined with an exclamation mark?\n(a) An exlamuestion mark\n(b) An interrobang\n(c) An interrogamation\n\n",
    "What is the highest-grossing Broadway show of all time?\n(a) The Lion King\n(b) Wicked\n(c) Hamilton\n\n",
    "On average, how many seeds are located on the outside of a strawberry?\n(a) 100\n(b) 200\n(c) 500\n\n",
    "In what country do more than half of people believe in elves?\n(a) Norway\n(b) Russia\n(c) Iceland\n\n",
    "What is yellowtail fish called in Japanese?\n(a) Ahi\n(b) Ikura\n(c) Hamachi\n\n",
    "Who was the first Disney Princess?\n(a) Snow White\n(b) Cinderella\n(c) Jasmine\n\n",
    "What’s the heaviest organ in the human body?\n(a) Brain\n(b) Skin\n(c) Liver\n\n",
]


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(quiz_questions[0], "c"),
    Question(quiz_questions[1], "b"),
    Question(quiz_questions[2], "a"),
    Question(quiz_questions[3], "b"),
    Question(quiz_questions[4], "a"),
    Question(quiz_questions[5], "b"),
    Question(quiz_questions[6], "c"),
    Question(quiz_questions[7], "c"),
    Question(quiz_questions[8], "a"),
    Question(quiz_questions[9], "c"),
]


def intro():
    """
    Intro to the game, presents player with first choice
    """
    global player
    print_slow(INTRO_TEXT)
    player = input()
    print_slow(f"\nHello {player}, are you ready to start your journey? (y/n) ")
    answer = input().lower()

    while answer == "y" or "n":
        if answer == "y":
            print_slow(TEXT_1 % clock)
            first_choice = input().lower()

            while first_choice == "bus" or "taxi":
                if first_choice == "bus":
                    take_bus()
                    break
                elif first_choice == "taxi":
                    take_taxi()
                    break
                else:
                    print("Please choose 'bus' or 'taxi' ")
                    first_choice = input("You better hurry up, how do you want to get to the airport, bus or taxi? ").lower()
            break
        elif answer == "n":
            print("That's understandable, travelling isn't what it used to be anyway")
            quit()
        else:
            print("Please type 'y' or 'n'")
            answer = input(f"Hello {player}, are you ready to start your journey? (y/n) ").lower()
    
        
def take_bus():
    """
    Runs if player chooses the bus path.
    """ 
    print_slow(TAKE_BUS_TEXT.format(player))
    quiz_game(questions)


def take_taxi():
    """
    Runs if player chooses the taxi path.
    """
    print_slow(TAKE_TAXI_TEXT.format(player))
    numbers_game()


def validate_answer(answer):
    options = ["a", "b", "c"]
    try:
        if answer not in options:
            raise ValueError()
    except ValueError:
        print("\n")
        print("Please type 'a', 'b' or 'c'")
        print("\n")
        return False
    return True
        

def quiz_game(questions):
    """
    Runs the quiz game when player chooses the bus path.
    """
    score = 0
    random_questions = random.sample(questions, 3)
    for question in random_questions:
        while True:
            answer = input(question.prompt)
            if validate_answer(answer):
                if answer == question.answer:
                    score += 1
                break
    print("\n")
    print_slow(f"You got {score} out of {len(random_questions)} right!")
    if int(score) == 2 or 3:
        print_slow(QUIZ_GAME_WIN)
        battle_game()
    else:
        print_slow(QUIZ_GAME_LOSE)
        game_over()


def numbers_game():
    random_number = random.randint(0, 4)
    guesses = 0

    while True:
        guesses += 1
        player_guess = input("Guess a number: ")
        if guesses == 3:
            print_slow(NUMBERS_GAME_LOSE)
            game_over()
        else:
            if player_guess.isdigit(): 
                player_guess = int(player_guess)
            else:
                print("Please type a number")
                continue

            if player_guess == random_number:
                break
            elif player_guess > 5:
                print("Please type a number between 0 and 5")
            else:
                print("Incorrect pincode, please try again!")
                continue
    print_slow(NUMBERS_GAME_WIN % guesses)
    battle_game()


def battle_game():
    player = 'Axel'
    print_slow(BATTLE_GAME_TEXT.format(player))
    class BattleMove():
        def Karatechop(self):
            kchop = random.randint(30, 40)
            return kchop

        def Judokick(self):
            jkick = random.randint(20, 60)
            return jkick

        def hpboost(self):
            health_boost = random.randint(10, 30)
            return health_boost

    def first_go():
        go = random.randint(0, 1)
        if go == 0:
            return 'Security officer'
        else:
            return player

    player_hp = 100
    comp_hp = 100

    turn = first_go()

    playermove = BattleMove()
    compmove = BattleMove()


    while player_hp > 0 and comp_hp > 0:
        print_slow(f"\n{turn}'s turn\n")
        if turn != 'Security officer':
            action = input(f'\n{player}, Pick a move:\na) Karatechop\nb) Judokick\nc) HP Boost\n')
            if action == 'a':
                player_kchop = playermove.Karatechop()
                comp_hp = comp_hp - player_kchop
                print_slow(f'\n{player} just did {player_kchop} damage!\n')
                print_slow(f'\n{player} HP: {player_hp}')
                print_slow(f'\nSecurity officer HP: {comp_hp}\n')
                turn = 'Security officer'
            elif action == 'b':
                player_jkick = playermove.Judokick()
                comp_hp = comp_hp - player_jkick
                print_slow(f'\n{player} just did {player_jkick} damage!\n')
                print_slow(f'\n{player} HP: {player_hp}')
                print_slow(f'\nSecurity officer HP: {comp_hp}\n')
                turn = 'Security officer'
            elif action == 'c':
                player_health_boost = playermove.hpboost()
                player_hp += player_health_boost
                print_slow(f'\n{player} boosted their HP by {player_health_boost}\n')
                print_slow(f'\n{player} has {player_hp} health')
                turn = 'Security officer'
            else:
                print("Please enter a correct action")

        else:
            computer_turn = random.randint(0, 2)
            if computer_turn == 0:
                comp_jkick = compmove.Judokick()
                player_hp = player_hp - comp_jkick
                print_slow(f'\nSecurity officer just did {comp_jkick} damage\n')
                print_slow(f'\n{player} HP: {player_hp}')
                print_slow(f'\nSecurity officer HP: {comp_hp}\n')
                turn = player
            elif computer_turn == 1:
                comp_health_boost = compmove.hpboost()
                comp_hp += comp_health_boost
                print_slow(f'\nSecurity officer boosted their HP by {comp_health_boost}\n')
                print_slow(f'\n{player} HP: {player_hp}')
                print_slow(f'\nSecurity officer HP: {comp_hp}\n')
                turn = player
            elif computer_turn == 2:
                comp_norm_attack = compmove.Karatechop()
                player_hp = player_hp - comp_norm_attack
                print_slow(f'\nSecurity officer just did {comp_norm_attack} damage!')
                print_slow(f'\n{player} HP: {player_hp}')
                print_slow(f'\nSecurity officer HP: {comp_hp}\n')
                turn = player

    if player_hp <= 0:
        print_slow('Security officer has won this round!')
    elif comp_hp <= 0:
        print_slow(f'\n{player} has won this round!')    


def game_over():
    print("\n")
    print_slow("==========================GAME OVER==========================")
    print("\n")
    print_slow("PLAY AGAIN? (y/n) ")
    play_again = input().lower()

    while play_again == "y" or "n":
        if play_again == "y":
            intro()
            break
        elif play_again == "n":
            quit()
        else:
            print_slow("Please type 'y' or 'n' ")
            play_again = input().lower()
    quit()

battle_game()