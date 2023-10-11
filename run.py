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