import sys, random, time
from time import gmtime, strftime
clock = strftime("%a, %d %b %Y and the time is %H:%M:%S", gmtime())
from random import randrange
from constants import TEXT_1, TAKE_BUS_TEXT, TAKE_TAXI_TEXT, QUIZ_GAME_WIN, NUMBERS_GAME_WIN, NUMBERS_GAME_LOSE


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
    print("\n")
    global player
    print_slow("Welcome to...\n")
    print("\n")
    print_slow("====================\n")
    print_slow("    HOME RUNNER\n")
    print_slow("====================\n")
    print("\n")
    print_slow("What is your name, traveller? ")
    player = input()
    print_slow(f"Hello {player}, are you ready to start your journey? (y/n) ")
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
    print_slow(TAKE_BUS_TEXT % player)
    quiz_game(questions)


def take_taxi():
    """
    Runs if player chooses the taxi path.
    """
    print_slow(TAKE_TAXI_TEXT % player)
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
    if int(score) != 3:
        print("\n")
        print_slow('Man: "You fool! Thanks to you I have been locked out of my Disney+ account forever!"\n')
        print_slow('Man: "As punishment, you shall never leave this bus!"\n')
        print("\n")
        print_slow("The man quickly grabs some cable ties from under his tall hat!\n")
        print_slow("He ties you to the seat in front of you!\n")
        print_slow("You realise you're stuck to the bus!\n")
        print_slow("You're now doomed to ride this bus for eternity...\n")
        print_slow("And you'll never make it to your family meeting...\n")
        game_over()
    else:
        print_slow(QUIZ_GAME_WIN)
        battle_game()


def numbers_game():
    print("\n")
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
    print_slow("Which line will you choose? (left/right) ")
    which_line = input().lower()
    while which_line == 'left' or 'right':
        if which_line == 'left':
            print_slow("You chose left\n")
            battle_game()
            break
        elif which_line == 'right':
            print_slow("You chose right\n")
            break
        else:
            print("\nPlease type 'left' or 'right'\n")
            which_line = input().lower()


def battle_game():
    class Player():
        def Karatechop(self):
            kchop = random.randint(0, 15)
            return kchop

        def Judokick(self):
            jkick = random.randint(20, 40)
            return jkick

        def heal(self):
            healing = random.randint(5, 25)
            return healing

    def first_go():
        go = random.randint(0, 2)
        if go == 0:
            return 'Comp'
        else:
            return player


    player_hp = 100
    player_energy = 0
    comp_hp = 100
    comp_energy = 0

    turn = first_go()

    playermove = Player()
    comp = Player()


    while player_hp > 0 and comp_hp > 0:
        print(f"\n{turn}'s turn")
        if turn != 'Comp':
            action = int(input(f'{player}, please choose an action:\n1) Karatechop\n2) Judokick\n3) Heal\n'))
            if action == 1:
                player_kchop = playermove.Karatechop()
                comp_hp = comp_hp - player_kchop
                player_energy += 10
                time.sleep(1)
                print(f'\n{player} just did {player_kchop} damage!')
                print(f'{player} now has {player_hp} health and {player_energy} energy')
                time.sleep(1)
                print(f'The computer now has {comp_hp} health and {comp_energy} energy')
                turn = 'Comp'
            elif action == 2 and player_energy >= 20:
                player_jkick = playermove.Judokick()
                comp_hp = comp_hp - player_jkick
                player_energy -= 20
                time.sleep(1)
                print(f'\n{player} just did {player_jkick} damage!')
                print(f'{player} now has {player_hp} health and {player_energy} energy')
                time.sleep(1)
                print(f'The computer now has {comp_hp} health and {comp_energy} energy')
                turn = 'Comp'
            elif action == 3 and player_energy >= 15:
                player_heal = playermove.heal()
                player_hp += player_heal
                player_energy -= 15
                time.sleep(1)
                print(f'\n{player} just healed themselves for {player_heal}')
                print(f'{player} has {player_hp} health and {player_energy} energy')
                turn = 'Comp'
            elif action == 2 or action == 3 and player_energy < 15:
                print(f'\n{player} you have {player_hp} and {player_energy} energy')
                print(f'{player} your energy is too low, please choose 1) Normal attack: ')
            else:
                print("Please enter a correct action")
        else:
            if comp_energy >= 20:
                comp_jkick = comp.Judokick()
                player_hp = player_hp - comp_jkick
                comp_energy -= 20
                time.sleep(1)
                print(f'\nThe computer just did {comp_jkick} damage')
                print(f'{player} now has {player_hp} health and {player_energy} energy')
                time.sleep(1)
                print(f'The computer now has {comp_hp} health and {comp_energy} energy')
                turn = player
            elif comp_hp < 50 and comp_energy >= 15:
                comp_healing = comp.heal()
                comp_hp += comp_healing
                comp_energy -= 15 
                time.sleep(1)
                print(f'\nThe comp has healed themselves for {comp_healing}')
                print(f'{player} now has {player_hp} health and {player_energy} energy')
                time.sleep(1)
                print(f'The computer now has {comp_hp} health and {comp_energy} energy')
                turn = player
            else:
                comp_norm_attack = comp.Karatechop()
                player_hp = player_hp - comp_norm_attack
                comp_energy += 10
                time.sleep(1)
                print(f'\nComp just did {comp_norm_attack} damage!')
                print(f'\n{player} now has {player_hp} health and {player_energy} energy')
                print(f'The computer now has {comp_hp} health and {comp_energy} energy')
                turn = player

    if player_hp <= 0:
        print('The computer has won this round!')
    elif comp_hp <= 0:
        print(f'\n{player} has won this round!')    


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

intro()