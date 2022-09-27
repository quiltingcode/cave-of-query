import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('indiana-diary')

def game_intro():
    """
    Introduction to the game, giving the user a brief
    description to set the scene, and ask for their 
    name to store in the explorers google sheet page.
    """
    print("Welcome intrepid explorer to the Cave of Query\n")
    print("What is your name?\n")

    explorer_name = input("Enter your name here: \n")
    print(explorer_name)

game_intro()