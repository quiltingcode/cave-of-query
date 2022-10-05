import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    print("You enter a large chamber")
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
    print("Door Y is locked with a 6 digit combination code...hmmmm") 
    while True:
        combination_lock = int(input("Type the 6 digit combination: \n"))
        if combination_lock == int(345117):
            print(f"The door opens, and on you go...\n")
            break
        else:
            print("The door doesn't budge. Try again.\n")
            continue
    
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
    letters = []
    for ind in range(1, 2):
        column = letters_worksheet.col_values(ind)
        letters.append(column)
    print(f"Letters Collected: ")
    pprint(letters_worksheet.get_all_values())


def puzzle_room_two():
    """
    Explorer enters second puzzle room and has to
    solve the substitution cypher to move on.
    """
    print("You move through to the second puzzle room.\n")
    print("Decode this ancient language to retrieve the next letter and move on.\n")
    while True:
        print("OAFO EJZSCMW VC F RDWJDR\n")
        decryption = (input("Type your decryption here:\n"))
        if decryption == ("that belongs in a museum"):
            print(f"You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            continue
    second_letter = 'N'
    print("You go through the next door marked with an 'N'.\n")
    
    return second_letter


def puzzle_room_three():
    """
    Explorer enters third puzzle room and has to
    complete the sequence to move on.
    """
    print("You move through to the third puzzle room.\n")
    print("Complete this mysterious sequence to collect the next letter and move on.\n")
    while True:
        print("1 2 3 6 9 8 7 __\n")
        next_num = int(input("Type the next number in the sequence here:\n"))
        if next_num == int(4):
            print(f"You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            continue
    third_letter = 'P'
    print("You go through the next door marked with a 'P'.\n")
    return third_letter


def puzzle_room_four():
    """
    Explorer enters fourth puzzle room and has to
    choose the correct library book to move on.
    """
    print("You move through to the fourth puzzle room.\n")
    print("You enter a library with books shelves covering all the walls.")
    print("One book contains a button to open the hidden doorway, but which one...")
    print("Which book would Grandpa Indiana have chosen?\n")
    print("You start scanning the titles...\n")

    library = SHEET.worksheet('library_books')
    books = []
    for ind in range(1,2):
        column = library.col_values(ind)
        books.append(column)

    pprint(books)

    while True:
        book = (input("Type the book title here:\n"))
        if book == ("Fortune and Glory Kid"):
            print(f"A hidden doorway opens with a creeeaaaaakkk.\n")
            break
        else:
            print("Nothing happens. Try again.\n")
            continue
    fourth_letter = 'O'
    print("You go through the next door marked with an 'O'.\n")
    
    return fourth_letter


def puzzle_room_five():
    """
    Explorer enters fifth puzzle room and has to
    solve an anagram puzzle to move on.
    """
    print("You move through to the fourth puzzle room.\n")
    print("You see a table in front of you with broken tiles all over it.")
    print("On closer inspection the tiles have letters on them.")
    print("Reaarange the tiles to reveal a word and unlock the door to move on.\n")
    print("The letters you can see are:\n")
    print(" P I V S J T C A R A ")

    while True:
        anagram = input("Type the correct word here: \n")
        anagram_answer = str(anagram)
        if validate_data(anagram_answer):
            print(f"That's the one! The door clicks open.")
            break

    fifth_letter = 'H'
    print("You go through the next door marked with a 'H'.\n")
    
    return fifth_letter


def validate_data(values):
    """
    Inside the try, converts all string values into lowercase.
    Raises ValueError if string values are not entered,
    or if there aren't exactly 10 characters entered.
    """
    
    try:
        [str(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"Exactly 10 letters are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"That won't work: {e}, please try again.\n")
        
    else:
        if str(values.lower()) == "javascript":
            return True

    return False


def main():
    """
    Run all program functions
    """
    # explorer_data = game_intro()
    # update_diary(explorer_data, 'explorers')

    # puzzle_one_letter = puzzle_room_one()
    # update_diary(puzzle_one_letter, 'letters')
    # letter_list = display_collected_letters(puzzle_one_letter)

    # puzzle_two_letter = puzzle_room_two()
    # update_diary(puzzle_two_letter, 'letters')
    # display_collected_letters(puzzle_two_letter)

    # puzzle_three_letter = puzzle_room_three()
    # update_diary(puzzle_three_letter, 'letters')
    # display_collected_letters(puzzle_three_letter)

    # puzzle_four_letter = puzzle_room_four()
    # update_diary(puzzle_four_letter, 'letters')
    # display_collected_letters(puzzle_four_letter)

    puzzle_five_letter = puzzle_room_five()
    update_diary(puzzle_five_letter, 'letters')
    display_collected_letters(puzzle_five_letter)


print("Welcome intrepid explorer to the Cave of Query\n")
main()