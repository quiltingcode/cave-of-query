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

    while True:
        print("What is your name?\n")

        explorer_name = input("Enter your name here: \n")

        if explorer_name.strip() != '':
            print(f"Welcome to the Cave of Query, {explorer_name}.")
            break
        else:
            raise ValueError(
            f"Please enter a valid response, intrepid explorer!")   
    
    return explorer_name


def update_explorer_list(data):
    """
    Update explorer worksheet, add a new row with the 
    explorer name provided.
    """
    print("Updating explorer database...\n")
    explorer_list_worksheet = SHEET.worksheet('explorers')
    explorer_list_worksheet.append_row([data])
    print("Explorer List updated successfully.\n")


def puzzle_room_one():
    """
    Explorer enters first puzzle room and has to
    solve an algebraic equation to move on.
    """
    print("You have entered a large chamber")


explorer_data = game_intro()
update_explorer_list(explorer_data)