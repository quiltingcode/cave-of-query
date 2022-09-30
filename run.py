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
        explorer_name = input("What is your name? \n")
        if explorer_name.strip() != '':
            print(f"Welcome to the Cave of Query, {explorer_name.capitalize()}.")
            break
        else:
            print('wrong values')
            continue

    return explorer_name


def update_diary(data):
    """
    Update explorer worksheet, add a new row with the 
    explorer name provided.
    """
    explorer_list_worksheet = SHEET.worksheet('explorers')
    explorer_list_worksheet.append_row([data])
    print("In his last will and testament, Indiana Jones left")
    print("you his explorer diary and a key. Now it is down to")
    print(f"you, {data.capitalize()}, to complete his final quest.\n")
    puzzle_room_one()


def puzzle_room_one():
    """
    Explorer enters first puzzle room and has to
    solve an algebraic equation to move on.
    """
    print("You enter a large entrance chamber ")
    print("surrounded by three locked doors. Above")
    print("each doorway, you can see engraved in the stone an")
    print("X, a Y, and a Z.\n")

    while True:    
        print("Solve the puzzle on the table to open the correct door.\n")
        print(f"3(0.5x + 12) = 87")

        answer_one = int(input("What is the value of x? \n"))
        if answer_one == int(34):
            print("correct")
            break
        else:
            print("That doesn't seem right to me. Try again")
            continue
    return answer_one

explorer_data = game_intro()
update_diary(explorer_data)