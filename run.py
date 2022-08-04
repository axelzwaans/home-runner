import sys, random, time
from time import gmtime, strftime
clock = strftime("%a, %d %b %Y and the time is %H:%M:%S", gmtime())


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)


quiz_questions = [
    "What is the collective noun for a group of pandas?\n(a) A group\n(b) A bunch \n(c) An embarrassment\n\n",
    "Which country do kiwifruit originate from?\n(a) New Zealand\n(b) China\n(c) Australia\n\n",
    "What is a Rocky Mountain oyster?\n(a) Bull testicles\n(b) An oyster from Rocky Mountain\n(c) A fish\n\n",
    "What is the correct term for a question mark combined with an exclamation mark?\n(a) An exlamuestion mark\n(b) An interrobang\n(c) An interrogamation\n\n"
]


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
            print("\n")
            print_slow(f"It's {clock}, you just woke up in your bedroom somewhere in Europe\n")
            print_slow("As you slowly get up, you realise something...\n")
            print_slow("You were supposed to be in Dublin for a family event!\n")
            print_slow("Which starts in 7 hours!\n")
            print_slow("If you don't make it, you'll be in heeps of trouble...\n")
            print("\n")
            print_slow("You better hurry up, how do you want to get to the airport, bus or taxi? ")
            first_choice = input().lower()

            while first_choice == "bus" or "taxi":
                if first_choice == "bus":
                    take_bus()
                    break
                elif first_choice == "taxi":
                    take_taxi()
                    break
                else:
                    print("Please choose 'bus' or 'taxi'")
                    first_choice = input("You better hurry up, how do you want to get to the airport, bus or taxi? ").lower()
            break
        elif answer == "n":
            print("That's understandable, flying isn't what it used to be anyway")
            quit()
        else:
            print("Please type 'y' or 'n'")
            answer = input(f"Hello {player}, are you ready to start your journey? (y/n) ")
    
        
def take_bus():
    """
    Runs if player chooses the bus path.
    """
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
    print_slow('Man: "I forgot the security questions I entered for this website, and now I cannot log in "\n')
    print_slow(f"{player}: We've all been there...\n")
    print_slow('Man: "Would you mind helping me out?"\n')
    print_slow(f'{player}: *reluctantly takes headphones out of ears* "sure..."\n')
    print_slow('Man: "Thanks! Here are the questions!...')
    print("\n")
    quiz_game(questions)


def take_taxi():
    """
    Runs if player chooses the taxi path.
    """
    print("\n")
    print("You took a taxi")
    print("\n")
    print_slow(f'{player}: "To the airport please, and step on it!"\n')
    print_slow('Taxi driver: "Speed limit is 55mph..."\n')
    print_slow(f'{player}: "Yeah okay never mind..."\n')
    print("\n")
    print_slow("As you make your way to the airport\n")
    print_slow("The driver seems to be a chatty one!\n")
    print_slow("So you smile and nod and look out the window\n")
    print_slow("As the city landscape passes you by...\n")
    print("\n")
    print_slow('Taxi driver: "Here we are!"\n')
    print_slow(f'{player}: "Great, how much will that be?"\n')
    print_slow('Taxi driver: "55 euros please"\n')
    print("\n")
    print_slow("You slide your credit card into the machine\n")
    print_slow("And you realise you forgot the last digit of your pin code\n")
    print_slow("You start to sweat\n")
    print_slow("If you guess wrong, the taxi driver will probably drive you to a police station\n")
    print_slow("You have 3 guesses before your card gets blocked!\n")
    print("\n")
    print_slow(f'{player}: "Here goes nothing, I am sure that it is a number between 0 and 5..."\n')
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
    for question in questions:
        while True:
            answer = input(question.prompt)
            if validate_answer(answer):
                if answer == question.answer:
                    score += 1
                break
    print("\n")
    print_slow(f"You got {score} out of {len(questions)} right!")
    if int(score) != 4:
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
        print("\n")
        print_slow("The man is grateful that he's now able to log into his Disney+ account\n")
        print("\n")
        print_slow('Man: "Now I can catch up on my favorite cartoons! Thank you!"\n')
        print("\n")
        print_slow("As the bus pulls into the airport, the man quickly runs to the door and runs away\n")
        print_slow("You leave the bus and make your way to the ticket desk\n")
        print("\n")
        battle_game()


def numbers_game():
    print("\n")
    random_number = random.randint(0, 5)
    guesses = 0

    while True:
        guesses += 1
        player_guess = input("Guess a number: ")
        if guesses == 3:
            print("\n")
            print_slow("Your card is blocked!")
            print("\n")
            print_slow("You slowly look up to the taxi driver\n")
            print_slow("He knows you can't pay the fare\n")
            print("\n")
            print_slow('Taxi driver: "I am taking you to the cops!"\n')
            print_slow('Taxi driver: "They will know what to with you"\n')
            print("\n")
            print_slow("As the driver speeds away\n")
            print_slow("You look back towards the airport\n")
            print_slow("And realise you won't see your family for a while...\n")
            print_slow("You think to yourself...\n")
            print_slow("...\n")
            print_slow("...\n")
            print_slow("...\n")
            print_slow("This sucks but at least it's a good excuse to get out of a family event!\n")
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
    print_slow("PIN CORRECT\n")
    print_slow(f"You can't believe it, you got it in {guesses} guesses!\n")
    print_slow("You say goodbye to the chatty taxi driver\n")
    print_slow("And you make your way into the airport...\n")
    print_slow("Luckily, you booked a ticket during the taxi ride,\n")
    print_slow("So you go straight through to your gate.\n")
    print_slow("But first you need to get through security!\n")
    print_slow("You check to see which line might be quicker.\n")
    print_slow("The line on the left seems to be going quicker...\n")
    print_slow("But the line on the right seems to have less people in it...\n")
    print("\n")
    
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
    quit()


intro()