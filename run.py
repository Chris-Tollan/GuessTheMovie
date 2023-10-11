import logging
import os
import random
from pathlib import Path

import gspread
import requests
from google.oauth2.service_account import Credentials
from pyfiglet import Figlet

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
user_name = ''
walk_of_fame = SHEET.worksheet("walk_of_fame")


def menu():
    """
        Display options to
    -	Explain how to play
    -	Access leaderboard
    -	Start game
    """

    while True:
        try:
            print(f.renderText("Menu"))
            print('')
            print("Lights...")
            print("Camera...")
            print("Action!")
            print("")
            print(f'Hey {user_name}, choose an option from the following')
            print('')
            print("[1] How to Play")
            print("[2] Leaderboard")
            print("[3] Start Game")
            print("")
            option = input("Enter 1, 2 or 3 \n")

            if option == "1":
                how_to_play()
                break
            elif option == "2":
                leaderboard()
                break
            else:
                os.system("clear")
                begin_game_play()
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
    print("Welcome to Guess the Movie")
    print('')
    print("How well can you recognise these scrambled blockbuster titles?")
    print("Lets find out…")
    print('')

    while True:
        try:
            user_name = input("Enter your username here: \n")
            if validate_user_name(user_name):
                print()
                print(f"Hello {user_name} welcome to Guess the Movie! \n")
                os.system("clear")
                menu()
                break
        except ValueError as e:
            print("Username is invalid:", str(e))

    return user_name


if __name__ == "__main__":
    load_game()
