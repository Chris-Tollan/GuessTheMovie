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
