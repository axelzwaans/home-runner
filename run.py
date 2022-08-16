from constants import *

import sys
import random
import time
from time import gmtime, strftime

clock = strftime("%a, %d %b %Y and the time is %H:%M:%S", gmtime())


def print_slow(str):
    """
    Prints text slowly for a more speech like effect.
    """
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)


class Question:
    """
    Stores questions and answers information needed for quiz game.
    """

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
    Intro of the game, prints INTRO_TEXT and
    presents player with their first choice.
    """
    global player
    print_slow(INTRO_TEXT)
    player = input()
    while len(player) == 0:
        print_slow("Please enter a name")
        print("\n")
        player = input()
    if len(player) != 0:
        print_slow(
            f"\nHello {player}, are you ready to " +
            "start your journey? (y/n) "
        )
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
                        print("\nPlease choose 'bus' or 'taxi'\n")
                        first_choice = input().lower()
                break
            elif answer == "n":
                print_slow(
                    "\nThat's understandable, travelling isn't "
                    + "what it used to be anyway\n"
                )
                quit()
            else:
                print("\nPlease type 'y' or 'n'")
                answer = input(
                    f"\nHello {player}, are you ready to "
                    + "start your journey? (y/n) \n"
                ).lower()


def take_bus():
    """
    Runs if player chooses the bus path,
    prints TAKE_BUS_TEXT and then calls the quiz game function.
    """
    print_slow(TAKE_BUS_TEXT.format(player))
    quiz_game(questions)


def take_taxi():
    """
    Runs if player chooses the taxi path,
    prints TAKE_TAXI_TEXT and then calls the numbers game function.
    """
    print_slow(TAKE_TAXI_TEXT.format(player))
    numbers_game()


def validate_answer(answer):
    """
    Checks for input validation in quiz game function.
    """
    options = ["a", "b", "c"]
    try:
        if answer not in options:
            raise ValueError()
    except ValueError:
        print("\nPlease type 'a', 'b' or 'c'")
        return False
    return True


def quiz_game(questions):
    """
    Runs the quiz game after player chooses the bus path.
    If quiz is won, it will then call the battle game function.
    If quiz is lost, it will call the game over function.
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
    print_slow(f"You got {score} out of {len(random_questions)} right!\n")
    if int(score) == 2:
        print_slow(QUIZ_GAME_WIN)
        battle_game()
    elif int(score) == 3:
        print_slow(QUIZ_GAME_WIN)
        battle_game()
    else:
        print_slow(QUIZ_GAME_LOSE)
        game_over()


def numbers_game():
    """
    Runs a numbers game after player chooses the taxi path.
    If game is won, it will then call the battle game function.
    If game is lost, it will call the game over function.
    """
    random_number = random.randint(0, 4)
    guesses = 0

    while True:
        guesses += 1
        player_guess = input("Guess a number: \n")
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
    """
    Prints BATTLE_GAME_TEXT and runs a battle game.
    If game is won, finishes full game.
    If game is lost, it will call game over function
    """
    print_slow(BATTLE_GAME_TEXT.format(player))

    class BattleMove:
        def Karatechop(self):
            kchop = random.randint(30, 40)
            return kchop

        def Judokick(self):
            jkick = random.randint(15, 60)
            return jkick

        def hpboost(self):
            health_boost = random.randint(10, 30)
            return health_boost

    def first_go():
        go = random.randint(0, 1)
        if go == 0:
            return "Security officer"
        else:
            return player

    player_hp = 100
    comp_hp = 100

    turn = first_go()

    playermove = BattleMove()
    compmove = BattleMove()

    while player_hp > 0 and comp_hp > 0:
        print_slow(f"\n{turn}'s turn\n")
        if turn != "Security officer":
            action = input(
                f"\n{player}, Pick a move:\na) Karate-chop\n"
                + "b) Judo-kick\nc) HP Boost\n"
            )
            if action == "a":
                player_kchop = playermove.Karatechop()
                comp_hp = comp_hp - player_kchop
                print_slow(f"\n{player} just did {player_kchop} damage!\n")
                print_slow(f"\n{player} HP: {player_hp}")
                print_slow(f"\nSecurity officer HP: {comp_hp}\n")
                turn = "Security officer"
            elif action == "b":
                player_jkick = playermove.Judokick()
                comp_hp = comp_hp - player_jkick
                print_slow(f"\n{player} just did {player_jkick} damage!\n")
                print_slow(f"\n{player} HP: {player_hp}")
                print_slow(f"\nSecurity officer HP: {comp_hp}\n")
                turn = "Security officer"
            elif action == "c":
                player_health_boost = playermove.hpboost()
                player_hp += player_health_boost
                print_slow(
                    f"\n{player} boosted their HP by {player_health_boost}\n"
                )
                print_slow(f"\n{player} has {player_hp} health")
                turn = "Security officer"
            else:
                print("Please enter a correct action")

        else:
            computer_turn = random.randint(0, 2)
            if computer_turn == 0:
                comp_jkick = compmove.Judokick()
                player_hp = player_hp - comp_jkick
                print_slow(
                    '\nSecurity officer just did ' +
                    f'{comp_jkick} damage\n'
                )
                print_slow(f"\n{player} HP: {player_hp}")
                print_slow(f"\nSecurity officer HP: {comp_hp}\n")
                turn = player
            elif computer_turn == 1:
                comp_health_boost = compmove.hpboost()
                comp_hp += comp_health_boost
                print_slow(
                    "\nSecurity officer boosted their HP" +
                    f' by {comp_health_boost}\n'
                )
                print_slow(f"\n{player} HP: {player_hp}")
                print_slow(f"\nSecurity officer HP: {comp_hp}\n")
                turn = player
            elif computer_turn == 2:
                comp_norm_attack = compmove.Karatechop()
                player_hp = player_hp - comp_norm_attack
                print_slow(
                    '\nSecurity officer just did ' +
                    f'{comp_norm_attack} damage!\n'
                )
                print_slow(f"\n{player} HP: {player_hp}")
                print_slow(f"\nSecurity officer HP: {comp_hp}\n")
                turn = player

    if player_hp <= 0:
        print_slow("\nYou lose!")
        game_over()
    elif comp_hp <= 0:
        print_slow(f"\n{player} has defeated the security officer!")
        print_slow(GAME_WIN_TEXT)


def game_over():
    """
    Runs whenever the player has lost a game,
    and asks the player if they want to play again.
    """
    print("\n")
    print_slow("====================\n")
    print_slow("      GAME OVER     \n")
    print_slow("====================")
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