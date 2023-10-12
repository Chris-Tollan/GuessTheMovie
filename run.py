import logging
import os
import random
from pathlib import Path

import gspread
import requests
from google.oauth2.service_account import Credentials
from pyfiglet import Figlet

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import warnings

logger = logging.getLogger(__name__)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

if Path("creds.json").exists():
    CREDS = Credentials.from_service_account_file("creds.json")
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("guess_the_movie_leaderboard")
else:
    # load all variable from environment
    logger.warning("Loading Google Import from environment")

f = Figlet(font="slant")

"""
list of movies to be scrambled
"""
movies = [
          'rocky',
          'jaws',
          'spotlight',
          'rambo',
          'tangled',
          'casino',
          'scream',
          'goodfellas',
          'thor',
          'jobs'
          ]

"""
GLOBALS
"""
count = 0
user_name = ''
walk_of_fame = SHEET.worksheet("walk_of_fame")


def end_game():
    print(f.renderText("Thats a Wrap!"))
    print(f'Thanks for playing {Fore.CYAN}{user_name}')
    print('Goodbye')
    quit()


def validate_back_to_menu(back_to_menu):
    """
    Validate that user has entered m
    Raise ValueError if any other character used
    """
    if back_to_menu.lower() != "m":
        raise ValueError("Please enter m")

    return True


def back_to_menu():
    """
    Provide option to exit current screen and
    Return to menu
    """

    while True:
        try:
            back_to_menu = input("Type m to display main menu \n")

            if back_to_menu.lower() == "m":
                os.system("clear")
                menu()
                break
        except ValueError as e:
            print("Try again:", str(e))
            print()


def leaderboard():
    """
    Display top scorers from leaderboard google sheet
    """
    os.system('clear')

    print(f.renderText("Walk of Fame"))
    print('')
    print('Top 10 Scores')
    print('')
    leaderboard = walk_of_fame.get_all_values()

    for rank, item in enumerate(leaderboard[:10], start=1):
        username, count = item
        print(f"{Fore.YELLOW}Rank {rank}: {username} - {count}")

    print()
    back_to_menu()


def how_to_play():
    """
    Explain the game to user then start game
    """
    os.system("clear")

    instructions = """

    During this game you will be presented with 10 movie titles
    which have been scrambled to make them unreadable.
    In order to progress through the game you must enter the unscrambled
    movie title.

    Example
    Movie - YOCKR
    Unscrambled Movie - ROCKY

    When typing your answer make sure to only use lowercase letters.
    At the end you will be shown your score...but will it make our
    Walk of Fame...?
    To begin, select the Start Game option from the menu. 
    """
    print(f.renderText("How To Play"))
    print(f'{Fore.CYAN}{user_name},')
    print(instructions)
    back_to_menu()


#def validate_user_input(user_input):
 #   """
  #  Validate that user has entered m
   # Raise ValueError if any other character used
    #"""
    #if not user_input.lower():
     #   raise ValueError("Please only use lowercase")

    #return True


def begin_game_play():
    """
    Get movie name from list
    Scramble movie name and display to user
    Ask user to enter their answer
    Check answer
    Calculate score
    update leaderboard
    """

    os.system('clear')

    global count

    print(f.renderText("Guess the Movie"))

    for movie in range(len(movies)):
        scrambled = ''.join(random.sample(movies[movie], len(movies[movie])))

        print(f'Unscramble this Movie: {scrambled} ')
        user_input = input('Enter the Movie here: \n')
        #validate_user_input(user_input)

        if user_input == movies[movie]:
            print(f'{Fore.GREEN}That is correct, Well Done!')
            print('')
            count += 1
        else:
            print(f'{Fore.RED}Sorry but thats incorrect!')
            print('')
     
    os.system('clear')
    print(f.renderText("How did you do?"))
    print('')
    print(f'You scored {count}!')
    if count <= len(movies)/2:
        print('Thats such a Z-Lister score!')
        print(f'Better luck next time {Fore.CYAN}{user_name}')
    else:
        print(f'Congratulations, your an A-Lister, Great Score {Fore.CYAN}{user_name}!')

    username = user_name
    data = []
    data.append(username)
    data.append(count)
    walk_of_fame.append_row(data)
    data_list = walk_of_fame.get_all_values()
    sorted_list = sorted(data_list, key=lambda x: int(x[1]), reverse=True)
    warnings.filterwarnings('ignore')
    walk_of_fame.update(sorted_list, "A:B")

    if count > int(sorted_list[9][1]):
        input('Press any key to continue: \n')
        os.system('clear')
        print(f"{Fore.CYAN}{user_name}, you have a top score!")
        print("Get ready to see your star on the walk of fame...")
        print()
        leaderboard()
    else:
        leaderboard()

    back_to_menu()


def validate_selected_option(option):
    """
    Validate that a valid option has been selected
    Raise ValueError if invalid option selected
    """
    if option != "1" and option != "2" and option != "3" and option != "x":
        raise ValueError("Sorry not an option, please enter 1, 2, 3 or x")

    return True


def menu():
    """
        Display options to
    -	Explain how to play
    -	Access leaderboard
    -	Start game
    -   Quit game
    """

    while True:
        try:
            print(f.renderText("Menu"))
            print('')
            print(f"{Fore.YELLOW}Lights...")
            print("Camera...")
            print(f"{Fore.GREEN}Action!")
            print("")
            print(f'Hey {Fore.CYAN}{user_name}, {Fore.WHITE}choose an option from the following')
            print('')
            print(f"{Fore.MAGENTA}[1] How to Play")
            print(f"{Fore.BLUE}[2] Leaderboard")
            print(f"{Fore.GREEN}[3] Start Game")
            print(f'{Fore.RED}[x] Quit')
            print("")
            option = input(f"Enter {Fore.MAGENTA}1, {Fore.BLUE}2, {Fore.GREEN}3 or {Fore.RED}x {Fore.WHITE} \n")
            validate_selected_option(option)

            if option == "1":
                how_to_play()
                break
            elif option == "2":
                leaderboard()
                break
            elif option == "3":
                begin_game_play()
                break
            else:
                os.system("clear")
                end_game()
                break
        except ValueError as e:
            print("Try again:", str(e))
            print()


def validate_user_name(user_name):
    """
    Check username entry for special characters
    Raise ValueError if special  characters are used
    """
    invalid_chars = ["/", "(", ")", "{", "}", "[", "]", "<", ">"]

    if any(char in user_name for char in invalid_chars):
        raise ValueError("Username can't contain /(){}[]<>\n")

    return True


def load_game():
    """
    Figlet banner
    Welcome message
    Request username
    Update global variable name
    """
    global user_name

    print(f.renderText("Guess the Movie"))
    print('')
    print(f"{Fore.YELLOW}Welcome to Guess the Movie")
    print('')
    print(f"{Fore.YELLOW}How well can you recognise these scrambled blockbuster titles?")
    print(f"{Fore.YELLOW}Lets find out…")
    print('')

    while True:
        try:
            user_name = input("Enter your username here: \n")
            if validate_user_name(user_name):
                print()
                print(f"Hello {Fore.CYAN}{user_name} {Fore.WHITE}welcome to Guess the Movie! \n")
                os.system("clear")
                menu()
                break
        except ValueError as e:
            print(f"{Fore.RED}Username is invalid:", str(e))

    return user_name


if __name__ == "__main__":
    load_game()
