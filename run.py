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
            print("In his last will and testament, Indiana Jones left")
            print("you his explorer diary and a key. Now it is down to")
            print(f"you, {explorer_name.capitalize()}, to complete his final quest.\n")
            break
        else:
            print(f"That's not a name I know./n")
            continue

    return explorer_name


def update_diary(data, worksheet):
    """
    Update worksheet specified in the parameter, add a new row with the 
    data provided.
    """
    explorer_list_worksheet = SHEET.worksheet(worksheet)
    explorer_list_worksheet.append_row([data])


def puzzle_room_one():
    """
    Explorer enters first puzzle room and has to
    solve an algebraic equation to move on.
    """
    print("You enter a large entrance chamber ")
    print("surrounded by two locked doors. Above")
    print("each doorway, you can see engraved in the stone an")
    print("X, and a Y.\n")
    print("Solve the puzzle on the table to open the correct door.\n")
    while True:
        print(f"3(0.5x + 12) = 87")

        answer_one = int(input("What is the value of x? \n"))
        if answer_one == int(34):
            print(f"You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            continue

    while True:
        print(f"4x - 12 = 192")
        
        answer_two = int(input("What is the value of x? \n"))
        if answer_two == int(51):
            print(f"You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            continue

    while True:
        print(f"85/x + 5x - 19 = 71")
        
        answer_three = int(input("What is the value of x? \n"))
        if answer_three == int(17):
            print(f"You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            continue
    print("All three puzzles complete but how do I open the door?\n")
    print("As Grandpa Indy always used to say, X never, ever marks the spot.")
    print("so let's try door Y. It contains a combination lock with 6 digits...hmmmm")
    print(f"If I use the answers from all the puzzles, the combination would be {answer_one}{answer_two}{answer_three}.")
    print("It works! The door unlocks and on you go...")
    
    first_letter = 'Y'
    
    print(f"But what's the significance of the letter {first_letter} on the door? you ask yourself.")
    print("Best to write it down in the diary just in case.\n")

    return first_letter
    

def display_collected_letters(letter):
    """
    After solving each puzzle room, the explorer receives a letter. These are 
    collected and displayed as the game goes along.
    """
    letters_worksheet = SHEET.worksheet('letters')
    print(letters_worksheet.get_all_values())


def puzzle_room_two():
    """
    Explorer enters second puzzle room and has to
    solve the substitution cypher to move on.
    """


    


explorer_data = game_intro()
update_diary(explorer_data, 'explorers')
puzzle_one_letter = puzzle_room_one()
update_diary(puzzle_one_letter, 'letters')
letter_list = display_collected_letters(puzzle_one_letter)
puzzle_room_two()