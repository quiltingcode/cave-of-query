import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import os
from art import *

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('indiana-diary')


class Error(Exception):
    """This is base class for other exceptions"""
    pass


class NumbersOnlyError(Error):
    """Exception due to Value is too small"""
    pass


class WholeNumbersOnlyError(Error):
    """Exception due to Value is too small"""
    pass


class WrongAnswerError(Error):
    """Exception due to Value is too small"""
    pass


def game_intro():
    """
    Introduction to the game, giving the user a brief
    description to set the scene, and ask for their 
    name to store in the explorers google sheet page.
    """
    os.system("clear")
    tprint("  The  Cave", font="epic")
    tprint("  of  Query", font="epic")
    while True:
        explorer_name = input("What is your name intrepid explorer? \n")
        if explorer_name.isalpha():
            print(f"Welcome to the Cave of Query, {explorer_name.capitalize()}.")
            print("In his last will and testament, Indiana Jones left")
            print("you his famous quest diary and a strange key.")
            print(f"Now it is down to you, {explorer_name.capitalize()}, to")
            print("complete his final quest, in the Caves of Query.\n")
            break
        else:
            print("That's not a name I know./n")
            continue

    return explorer_name


def update_diary(data, worksheet):
    """
    Update worksheet specified in the parameter, add a new row with the
    data provided.
    Update explorer worksheet to record players, and use their name
    throughout the game.
    Update the letters worksheet after each puzzle when a letter clue
    is collected.
    """
    diary_worksheet = SHEET.worksheet(worksheet)
    diary_worksheet.append_row([data])


def puzzle_room_one():
    """
    Explorer enters first puzzle room and has to
    solve an algebraic equation to move on.
    """
    key_one = 34
    key_two = 51
    key_three = 17
    key_four = 345117
    print("You enter a large chamber with a locked door ahead.")
    print("Solve the puzzles etched on the table to unlock the door.\n")
    while True:
        print("3(0.5x + 12) = 87")
        try:
            user_answer_one = int(input("What is the value of X? \n"))
        except ValueError:
            print(f"That's not a number")
            continue
    
        if (user_answer_one) == key_one:
            print("You've got it!")
            break
        else:
            print(f"That's the wrong answer.Try again")
    while True:
        print("4x - 12 = 192")
        try:
            user_answer_two = int(input("What is the value of X? \n"))
        except ValueError:
            print(f"That's not a number")
            continue
    
        if (user_answer_two) == key_two:
            print("You've got it!")
            break
        else:
            print(f"That's the wrong answer.Try again")
    while True:
        print("85/x + 5x - 19 = 71")   
        try:
            user_answer_three = int(input("What is the value of X? \n"))
        except ValueError:
            print(f"That's not a number")
            continue
    
        if (user_answer_three) == key_three:
            print("You've got it!")
            break
        else:
            print(f"That's the wrong answer.Try again")

    while True:
        print("All three puzzles complete but how do I open the door?\n")
        print("On closer inspection, the door is locked with a 6 digit combination" 
              + "code...") 
        try:
            combination_lock = int(input("Enter the 6 digit combination: \n"))
        except ValueError:
            print(f"That's not a number. It has to be 6 digits with no spaces")
            continue
        if combination_lock == key_four:
            print("The door opens, and on you go...\n")
            break
        else:
            print("The door doesn't budge. What about using the"
                  + "answers from the three number puzzles joined together.\n")
            continue
    first_letter = 'H'
    print(f"As you pass through, you notice a big {first_letter} on the door.")
    print("But what does it mean?")
    print("Best to write it down in the diary just in case.\n")
    return first_letter


# def validate_whole_number(answer, input):
#     """
#     Validation on user input
#     Check input is not a float
#     Check input is not an alpha or special character
#     Check input is not blank
#     """
#     try:  
#         if type(input) != int:
#             raise WholeNumbersOnlyError(
#                 f"Whole numbers required. You wrote {input}"
#             )
#         elif type(input) == int and input != answer:
#             raise WrongAnswerError(
#                 f"But it is an integer."
#             )
#         elif type(input) == int and input == answer:
#             print("correct") 
#             return True
#     except NumbersOnlyError as e:
#         print(f"Invalid data: {e}, try again\n")
#         return False
#     except WholeNumbersOnlyError as e:
#         print(f"Invalid data: {e}, try again\n")
#         return False
#     except WrongAnswerError as e:
#         print(f"Wrong answer: {e}, try again\n")
#         return False


def puzzle_room_two():
    """
    Explorer enters second puzzle room and has to
    solve the substitution cypher to move on.
    """
    print("You move through to the second puzzle room.\n")
    print("Decode this ancient language on the wall to retrieve the next")
    print("letter and move on.\n")
    print("OAFO EJZSCMW VC F RDWJDR\n")
    print("Wait a minute, I think I remember seeing a page in Granpy")
    print("Indiana's diary which translated ancient alphabets.")
    print("Let me find the right page....")
    diary_code = SHEET.worksheet('alphabet')
    modern_alphabet = list(diary_code.col_values(1))
    ancient_alphabet = list(diary_code.col_values(2))
    decoder = {modern_alphabet[i]: ancient_alphabet[i] for i in range(len(modern_alphabet))}
    
    for i in range(13):
        printable = f'{chr(65+i)} : {decoder[chr(65 + i)]}   ||   {chr(78 + i)} : {decoder[chr(78 + i)]}'
        print(printable)
    
    while True:
        decryption = (input("Type your decryption here:\n")).lower()
        if decryption == ("that belongs in a museum"):
            print("You've got it.\n")
            break
        else:
            print("Nothing happens. Try again.\n")
            continue
    second_letter = 'I'
    print("You go through a huge door marked with an 'I'.\n")
    return second_letter


def long_string_validation(alpha_string):
    """
    Validate if sentence entered is only alpha characters
    """
    if answer.isalpha() and answer.lower() == "museum":
        print("Correct")
    elif answer.isalpha() and answer.lower() != "museum":
        print("Thats not right")
    elif not answer.isalpha():
        print("The answer must be letters not numbers or characters")


def puzzle_room_three():
    """
    Explorer enters third puzzle room and has to
    complete the sequence to move on.
    """
    print("You move through to the third puzzle room.\n")
    print("Complete this familiar sequence to collect the next" 
          + "letter and move on.\n")
    while True:
        print("1 1 2 3 5 8 13 21 34 55 __\n")
        next_num = int(input("Type the next number in the sequence here:\n"))
        if next_num == int(89):
            print("You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            continue
    third_letter = 'C'
    print("You go through the next door marked with an 'C'.\n")
    return third_letter


def puzzle_room_four():
    """
    Explorer enters fourth puzzle room and has to
    choose the correct library book to move on.
    """
    print("You move through to the fourth puzzle room.\n")
    print("You enter a library with books shelves covering all the walls.")
    print("One book contains a button to open the hidden"
          + "doorway, but which one...")
    print("Which book would Grandpa Indiana have chosen?\n")
    print("You start scanning the titles...\n")
    library = SHEET.worksheet('library_books')
    books = []
    for ind in range(1, 2):
        column = library.col_values(ind)
        books.append(column)
    pprint(books)
    while True:
        book = (input("Type the correct book title here:\n")).lower()
        if book == ("fortune and glory kid"):
            print("Of course! The bookshelf slides away and a hidden"
                  + "tunnel is revealed.\n")
            break
        else:
            print("Nothing happens. Try again.\n")
            continue
    fourth_letter = 'O'
    print("You go through the tunnel and notice 'O's all over the walls.\n")
    return fourth_letter


def puzzle_room_five():
    """
    Explorer enters fifth puzzle room and has to
    solve an anagram puzzle to move on. Answer inputted is passed
    through a data validation function.
    """
    print("You run through the tunnel and arrive at another puzzle room.\n")
    print("You see a table in front of you with broken tiles all over it.")
    print("On closer inspection the tiles have letters on them.")
    print("Rearrange the tiles to reveal a word and unlock the door.\n")
    print("The letters you can see are:\n")
    print(" P I V S J T C A R A ")
    while True:
        anagram = input("Type the correct word here: \n")
        user_guess = str(anagram)
        answer = "javascript"     
        if user_guess.isalpha() and user_guess.lower() == key:
            print("That's the one! The door clicks open.\n")
            break
        if user_guess.isalpha() and user_guess.lower() != "museum":
            print("Thats not right")
            continue
        elif not answer.isalpha():
            print("The answer must be letters not numbers or characters")
            continue
    fifth_letter = 'P'
    print("You go through the next door marked with an 'P'.\n")
    return fifth_letter


def validate_data(answer, input):
    """
    Inside the try, converts all string values into lowercase.
    Raises ValueError if string values are not entered,
    or if there aren't exactly 10 characters entered.
    """
           
    if input.isalpha() == True and input.lower() != answer:
        print("Thats not right")
        return False
    elif answer.isalpha() == False:
        print("The answer doesn't contain numbers or special characters")
        return False
    elif input.isalpha() == True and input.lower() == answer:
        return True 
    else:
        return False


def puzzle_room_six():
    """
    Explorer enters sixth puzzle room and has to
    solve the morse code word to move on.
    """
    print("You move through to the sixth puzzle room.\n")
    print("Decode this ancient language to retrieve the next letter"
          + "and move on.\n")
    print(".. - ... / .- / .-.. . .- .--. / --- ..-. / ..-. .- .. - ....\n")
    print("Wait a minute, this looks like old Morse Code")
    print("I think I saw something in the diary like this....")
    print("Let me find the right page....") 
    morse_code = SHEET.worksheet('morse_code')
    abc_alphabet = list(morse_code.col_values(1))
    morse_alphabet = list(morse_code.col_values(2))
    code_dict = {abc_alphabet[i]: morse_alphabet[i] for i in range(len(abc_alphabet))}
    for i in range(13):
        printable = f'{chr(65+i)} : {code_dict[chr(65 + i)]}     ||     {chr(78 + i)} : {code_dict[chr(78 + i)]}'
        print(printable)
    while True:
        decryption = (input("Type your decryption here:\n")).lower()
        if decryption == ("its a leap of faith"):
            print("You've got it. The door unlocks.\n")
            break
        else:
            print("Nothing happens. Try again.\n")
            continue
    sixth_letter = 'N'
    print("You go through the next door marked with a 'N'.\n")
    return sixth_letter


def puzzle_room_seven():
    """
    Explorer enters seventh puzzle room and has to
    solve the riddle to move on. I use a sort method to 
    make sure that whatever order they type in the four 
    answers, they are sorted into the order that is recognised
    as the right answer if they have guessed the four words 
    correctly but may have an alternative order to me. 
    """
    print("You move through to the seventh puzzle room.\n")
    print("Decipher this riddle to retrieve the next letter and move on.\n")
    while True:
        print("Can you name four days of the week that begin with the"
              + "letter 'T'\n")
        days = (input("Type the fours days here:\n"))
        if days == ("thursday, today, tomorrow, tuesday"):
            print("You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            continue
    seventh_letter = 'T'
    print("You go through the next door marked with a 'T' and"
          + "head off down a long tunnel.\n")
    return seventh_letter


def treasure_room():
    """
    Explorer reaches the treasure room and has to solve a puzzle
    to access the treasure chest
    """
    print("The tunnel widens and opens out into a great chamber"
          + "with golden disks set into the floor.")
    print("Each disk has a letter engraved on it.")
    print("On the wall ahead, you can see another puzzle: \n")
    print("1 1 1 1 = R")
    print("2 2 2 2 = T")
    print("3 3 3 3 = E")
    print("4 4 4 4 = N")
    print("5 5 5 5 = ?")
    while True:
        tile = (input("What is the missing letter? \n"))
        if tile.capitalize() == ("Y"):
            print(f"you stand on the golden disk with a {tile} on it.\n")
            print("The disk sinks deeper into the floor and you hear"
                  + "a rumble.\n")
            break    
        else:
            game_over()
    treasure_letter = tile
    return treasure_letter
    display_collected_letters(treasure_letter)


def treasure_chest():
    """
    The treasure chest is revealed. The user must decode the letters
    collected and the key to open the chest
    """
    print("A treasure chest rises out of the floor but it won't open.")
    print("Embedded in the lid is a crpytex, with eight alphabet dials")
    while True:
        cryptex = str((input("Enter eight letters here: \n")).upper())
        if cryptex == str("PYTHONIC"):
            print("You've got it! A small door opens on the front of")
            print("the chest to reveal a key hole...\n")
            break
        else:
            print("Nothing happens. Are the letters in the right order? \n")
            continue
    print("You get out Grandpa Indy's old key and it's a perfect fit.")
    print("The treasure chest opens and you look inside...")
    print("Jewels of all shapes and sizes surround an old book.")
    print("It looks like it contains some sort of treasure map\n")
    print("Have you had enough treasure hunting for one lifetime")
    print(", or are you ready for more?")
    while True:
        replay = (input("Type Yes (Y) or No (N): \n"))
        if replay == ("Y"):
            print("Good luck on your next adventure. Goodbye")
            clear()
            reset_game()
            main()
            break
        elif replay == ("N"):
            clear()
            reset_game()
            print("Good luck on your next adventure. Goodbye")
            break
        else:
            print(f"I don't understand what {replay} means. Can you"
                  + "please repeat?\n")
            continue


def clear():
    """
    Clears all the previous text output in the user terminal 
    """
    os.system("clear")


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
    print("Letters Collected: ")
    for new_lst in letters: 
        no_brackets_lst = (','.join(new_lst))
        print(no_brackets_lst)


def game_over():
    """
    If user makes a wrong choice in the treasure room, they die 
    and the game over function is called.
    User is asked if they would like to play again or not.
    """
    clear()
    print("you stand on the golden disk, and it falls away down a black hole.\n")
    print("You died a tragic death.")
    print("Would you like to play again?\n")
    while True:
        replay = (input("Type Y / N: \n"))
        if replay == ("Y"):
            clear()
            reset_game()
            main()
            break
        elif replay == ("N"):
            clear()
            reset_game()
            print("Good luck on your next adventure. Goodbye")
            break
        else:
            print(f"I don't understand what {replay} means. Can you please repeat?\n")
            continue


def reset_game():
    """
    Reset the figures in the google worksheet, and start the game 
    again from the beginning. 
    """
    clear()
    clear_collected_letters()


def clear_collected_letters():
    """
    Whenever a new game is started, all the data in 
    the worksheet containing the collected puzzle letters
    is deleted.
    """
    clear_worksheet = SHEET.worksheet('letters')
    clear_worksheet.clear()


def main():
    """
    Run all program functions
    """
    explorer_data = game_intro()
    update_diary(explorer_data, 'explorers')

    clear_collected_letters()

    puzzle_one_letter = puzzle_room_one()
    update_diary(puzzle_one_letter, 'letters')
    display_collected_letters(puzzle_one_letter)

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
    
    puzzle_six_letter = puzzle_room_six()
    update_diary(puzzle_six_letter, 'letters')
    display_collected_letters(puzzle_six_letter)

    puzzle_seven_letter = puzzle_room_seven()
    update_diary(puzzle_seven_letter, 'letters')
    display_collected_letters(puzzle_seven_letter)
    
    final_letter = treasure_room()
    update_diary(final_letter, 'letters')
    display_collected_letters(final_letter)
    treasure_chest()
  

main()