from pprint import pprint
import os
from art import *
from colorama import init
from colorama import Fore, Back, Style
init()


# Global Variables - Explorer Name and puzzle letters

letters_collected = []
explorer = []


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
            clear()
            print(f"Welcome to the Cave of Query, "
                  f"{explorer_name.capitalize()}.")
            print("In his last will and testament, Indiana Jones left")
            print("you his famous quest diary and a strange key.")
            print(f"Now it is down to you, {explorer_name.capitalize()}, to")
            print("complete his final quest, in the Caves of Query.\n")
            break
        else:
            print(Fore.RED + "That's not a name I know.")
            print(Style.RESET_ALL)
            continue

    return explorer_name
    explorer.append(explorer_name)


def puzzle_room_one():
    """
    Explorer enters first puzzle room and has to
    solve an algebraic equation to move on.
    Validation on user input:
    Check input is not a float
    Check input is not an alpha or special character
    Check input is not blank
    """
    key_one = 34
    key_two = 51
    key_three = 17
    key_four = 345117
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀            ⣠⡾⢻⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⣧                   ⠈⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿")
    print("⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ⠀⣿")
    print("⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 ⠀⠀⣿")
    print("⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀                        ⠀⣿")
    print("⣿⠟⠁⠀                         ⠀⠀⠀⠀⠀⠀⣿")
    print("⣿⠀⠀⠀⠀                               ⣿")
    print("⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣤⣤⣤⣿")
    print("You enter the cave and arrive at a large chamber with a locked"
          + " door ahead.")
    print("Solve the puzzles etched on the wall to unlock the door.\n")
    while True:
        print("3(0.5x + 12) = 87")
        try:
            user_answer_one = int(input("What is the value of X? \n"))
        except ValueError:
            print(Fore.RED + f"That's not a number\n")
            print(Style.RESET_ALL)
            continue
        if (user_answer_one) == key_one:
            print("You've got it!")
            break
        else:
            print(f"That's not right. Try again.\n")
    while True:
        print("4x - 12 = 192")
        try:
            user_answer_two = int(input("What is the value of X? \n"))
        except ValueError:
            print(Fore.RED + f"That's not a number\n")
            print(Style.RESET_ALL)
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
            print(Fore.RED + f"That's not a number\n")
            print(Style.RESET_ALL)
            continue
        if (user_answer_three) == key_three:
            print("You've got it!")
            break
        else:
            print(f"That's the wrong answer.Try again")
    print("All three puzzles complete but how do I open the door?\n")
    print("On closer inspection, the door is locked with a 6 digit "
          + "combination code...")
    while True:
        try:
            combination_lock = int(input("Enter the 6 digit combination: \n"))
        except ValueError:
            print(Fore.RED + f"That's not a number. It has to be 6 digits "
                  + "with no spaces")
            print(Style.RESET_ALL)
            continue
        if combination_lock == key_four:
            print("The door opens, and on you go...\n")
            break
        else:
            print("The door doesn't budge.")
            print(Fore.GREEN + "HINT: What about using the "
                  + "answers from the three number puzzles joined together.\n")
            print(Style.RESET_ALL)
            continue
    first_letter = 'H'
    print(f"As you pass through, you notice a big {first_letter} on the door.")
    print("But what does it mean?")
    return first_letter


def continue_or_quit():
    """
    Function to give user option to continue to
    next puzzle or end the game early.
    """
    print("Let's make a note of that letter in the diary.\n")
    show_collected_letters()
    while True:
        print("Do you want to continue or do you give up?\n")
        replay = (input("Type Continue (C) or Quit (Q): \n").lower())
        if replay == ("c"):
            clear()
            print(f"Let's keep going then!\n")
            break
        elif replay == ("q"):
            clear()
            reset_game()
            print("Safer back in the classroom huh?!")
            print(f"Goodbye then.")
            main()
            break
        else:
            print(Fore.RED + f"I don't understand what {replay} "
                  + "means. Can you please repeat?\n")
            print(Style.RESET_ALL)
            continue


def puzzle_room_two():
    """
    Explorer enters second puzzle room and has to
    solve the substitution cypher to move on.
    Dictionary Decoder provided to user.
    Validation against numbers, special characters, and blank
    entries
    """
    puzzle_two_dict = {
                        'A': 'F',
                        'B': 'E',
                        'C': 'N',
                        'D': 'U',
                        'E': 'J',
                        'F': 'Y',
                        'G': 'M',
                        'H': 'A',
                        'I': 'V',
                        'J': 'P',
                        'K': 'H',
                        'L': 'Z',
                        'M': 'R',
                        'N': 'C',
                        'O': 'S',
                        'P': 'K',
                        'Q': 'G',
                        'R': 'T',
                        'S': 'W',
                        'T': 'O',
                        'U': 'D',
                        'V': 'X',
                        'W': 'I',
                        'X': 'B',
                        'Y': 'L',
                        'Z': 'Q',
                        '1': '1'
    }
    print("PUZZLE ROOM TWO")
    print("---------------\n")
    print("Decode this ancient language on the wall to retrieve the next")
    print("letter and move on.\n")
    print("OAFO EJZSCMW VC F RDWJDR\n")
    print("Wait a minute, I think I remember seeing a page in Grandpa")
    print("Indiana's diary which translated ancient alphabets.")
    print("Let me find the right page....")
    for i in range(13):
        decoder = (f'{chr(65+i)} : {puzzle_two_dict[chr(65 + i)]}   '
                   f'||   {chr(78 + i)} : {puzzle_two_dict[chr(78 + i)]}')
        print(decoder)
    while True:
        decryption = (input("Type your decryption here:\n")).lower()
        if decryption == ("that belongs in a museum"):
            print("You've got it.\n")
            break
        else:
            print("Nothing happens.")
            print(Fore.GREEN + "HINT: Use the ancient dictionary decoder")
            print(" in your diary to help decipher the letters.\n")
            print(Style.RESET_ALL)
            continue
    second_letter = 'I'
    print("You go through a huge door marked with an 'I'.\n")
    return second_letter


def puzzle_room_three():
    """
    Explorer enters third puzzle room and has to
    complete the sequence to move on.
    Validation on user input:
    Check input is not a float
    Check input is not an alpha or special character
    Check input is not blank
    """
    sequence_answer = 89
    print("PUZZLE ROOM THREE")
    print("-----------------\n")
    print("Complete this familiar sequence to collect the next "
          + "letter and move on.\n")
    while True:
        print("1 1 2 3 5 8 13 21 34 55 __\n")
        try:
            next_num = int(input("Type the next number in the"
                                 " sequence here:\n"))
        except ValueError:
            print(Fore.RED + f"That's not a number.\n")
            print(Style.RESET_ALL)
            continue
        if next_num == sequence_answer:
            print("You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            print(Fore.GREEN + "HINT: Try adding the numbers together.\n ")
            print(Style.RESET_ALL)
            continue
    third_letter = 'C'
    print("You go through the next door marked with as 'C'.\n")
    return third_letter


def puzzle_room_four():
    """
    Explorer enters fourth puzzle room and has to
    type the correct library book title to move on.
    List of books printed to user.
    Validation against numbers, special characters, and blank
    entries
    """
    book_list = [
                'The Hobbit',
                'Don Quixote',
                'Treasure Island',
                'Moby Dick',
                'The Castle',
                "Gulliver's Travels",
                'Great Expectations',
                "The Pilgrim's Process",
                'The Count of Monte Cristo',
                'The Scarlet Letter',
                'A Tale of Two Cities',
                'Brave New World',
                'Fortune and Glory Kid',
                'War and Peace',
                'The Secret Garden',
                'The Last of the Mohicans',
                'The Call of the Wild',
                'Ulysses',
                'The Trial',
                'The Stranger',
                'A Farewell to Arms',
                'The Jungle',
                'Persuasion',
                'Utopia',
                'A Wrinkle in Time',
                'On the Road',
                'The Good Earth',
                'The Alchemist',
                'The Last Battle']
    columns = 3
    hidden_button_book = 'fortune and glory kid'
    print("PUZZLE ROOM FOUR")
    print("----------------\n")
    print("You enter a library with books shelves covering all the walls.")
    print("One book contains a button to open the hidden "
          + "doorway, but which one...")
    print("Which book would Grandpa Indiana have chosen?\n")
    print("You start scanning the titles...\n")
    for first, second, third in zip(book_list[::columns],
                                    book_list[1::columns],
                                    book_list[2::columns]):
        print(f'{first: <25}  {second: <25}  {third}')
    while True:
        book = (input("Type the correct book title here:\n")).lower()
        if book == hidden_button_book:
            print("Of course!\n")
            break
        else:
            print("No hidden buttons there. Try again.\n")
            print(Fore.GREEN + "HINT: What was that phrase Grandpa Indiana"
                  + " always used to say to me when I was a kid...\n")
            print(Style.RESET_ALL)
            continue
    fourth_letter = 'O'
    print("There's a hidden button! The bookshelf slides away and a "
          + "tunnel is revealed.\n")
    print("You go through the tunnel and notice 'O's all over the walls.\n")
    return fourth_letter


def puzzle_room_five():
    """
    Explorer enters fifth puzzle room and has to
    solve an anagram puzzle to move on.
    Validation against numbers, special characters, and blank
    entries
    """
    anagram_key = "javascript"
    print("You run through the tunnel and arrive at another puzzle room.\n")
    print("PUZZLE ROOM FIVE")
    print("----------------\n")
    print("You see a table in front of you with broken tiles all over it.")
    print("On closer inspection the tiles have letters on them.")
    print("Rearrange the tiles to reveal a word and unlock the door.\n")
    print("The letters you can see are:\n")
    anagram_key = "javascript"
    print(" P I V S J T C A R A ")
    while True:
        anagram = (input("Type the correct word here:\n")).lower()
        if anagram == anagram_key:
            print(f"That's the one!")
            break
        else:
            print("Only use a combination of the ten letters"
                  + " provided")
            print(Fore.GREEN + "HINT: It's a language...")
            print(Style.RESET_ALL)
            continue
    fifth_letter = 'P'
    print(f"The door clicks open.")
    print("You go through the next door marked with a 'P'.\n")
    return fifth_letter


def puzzle_room_six():
    """
    Explorer enters sixth puzzle room and has to
    solve the morse code word to move on.
    Validation against numbers, special characters, and blank
    entries
    """
    morse_code_dict = {
                    'A': '.-  ',
                    'B': '-...',
                    'C': '-.-.',
                    'D': '-.. ',
                    'E': '.   ',
                    'F': '..-.',
                    'G': '--. ',
                    'H': '....',
                    'I': '..  ',
                    'J': '.---',
                    'K': '-.- ',
                    'L': '.-..',
                    'M': '--  ',
                    'N': '-.  ',
                    'O': '--- ',
                    'P': '.--.',
                    'Q': '--.-',
                    'R': '.-. ',
                    'S': '... ',
                    'T': '-   ',
                    'U': '..- ',
                    'V': '...-',
                    'W': '.-- ',
                    'X': '-..-',
                    'Y': '-.--',
                    'Z': '--..'
                    }
    print("PUZZLE ROOM SIX")
    print("---------------\n")
    print("Decode this ancient language to retrieve the next letter"
          + " and move on.\n")
    print(".. - ... (space) .- (space) .-.. . .- .--. (space) --- ..-. "
          + "(space) ..-. .- .. - ....\n")
    print("Wait a minute, this looks like old Morse Code.")
    print("I think I saw something in the diary like this.")
    print("Let me find the right page....")
    for i in range(13):
        morse_diary = (f'{chr(65+i)} : {morse_code_dict[chr(65 + i)]}     ||  '
                       f'  {chr(78 + i)} : {morse_code_dict[chr(78 + i)]}')
        print(morse_diary)
    while True:
        decryption = (input("Type your decryption here:\n")).lower()
        if decryption == ("its a leap of faith"):
            print("You've got it.")
            break
        else:
            print("Nothing happens.")
            print(Fore.GREEN + "HINT: Use the morse code decoder"
                  + " in your diary to help decipher the letters.\n")
            print(Style.RESET_ALL)
            continue
    sixth_letter = 'N'
    print("The door unlocks.")
    print("You go through the next door marked with an 'N'.\n")
    return sixth_letter


def puzzle_room_seven():
    """
    Explorer enters seventh puzzle room and has to
    solve the riddle to move on.
    The user input is converted into a set, so that if they type the four
    correct answer in a different order, it is still accepted as correct,
    when compare with the correct answer set.
    """
    riddle_key = {'thursday', 'today', 'tomorrow', 'tuesday'}
    print("PUZZLE ROOM SEVEN")
    print("-----------------\n")
    print("Decipher this riddle to retrieve the next letter and move on.\n")
    while True:
        print("Can you name four days of the week that begin with the"
              + " letter 'T'\n")
        days = set(input("Type the four days here:\n").split())
        if riddle_key == days:
            print("You've got it.\n")
            break
        else:
            print("That doesn't seem right to me. Try again.\n")
            print(Fore.GREEN + "HINT: Just type the four words with spaces"
                  + " between them.\n")
            print(Style.RESET_ALL)
            continue
    seventh_letter = 'T'
    print("You go through the next door marked with a 'T' and"
          + " head off down a long tunnel.\n")
    return seventh_letter


def treasure_room():
    """
    Explorer reaches the treasure room and has to solve a puzzle
    to access the treasure chests
    Validation against numbers, special characters, and blank
    entries.
    """
    correct_disk = "Y"
    print("TREASURE CHAMBER")
    print("-------------\n")
    print("The tunnel widens and opens out into a great chamber")
    print("with golden disks set into the floor.")
    print("Each disk has a letter engraved on it.")
    print("On the wall ahead, you can see another puzzle: \n")
    print("1 1 1 1 = R")
    print("2 2 2 2 = T")
    print("3 3 3 3 = E")
    print("4 4 4 4 = N")
    print("5 5 5 5 = ?")
    while True:
        disk_picked = (input("What is the missing letter? \n"))
        if disk_picked.capitalize() == correct_disk:
            print(f"you stand on the golden disk with a {correct_disk} on"
                  + " it.\n")
            print("Something is happening...wait! What's that?")
            break
        else:
            print("You only need to choose one letter here")
            print(Fore.GREEN + "HINT: You have to add the four numbers"
                  + " together each time...")
            print(Style.RESET_ALL)
            continue
    treasure_letter = correct_disk
    return treasure_letter
    print(f"The {correct_disk} disk sinks deeper into the floor and you hear"
          + " a rumbling noise")


def treasure_chest():
    """
    The treasure chest is revealed. The user must re-order the letters
    collected to open the chest.
    """
    print("An enormous treasure chest rises out of the floor"
          + " but it won't open.")
    print("Embedded in the lid is a crpytex, with eight alphabet dials.\n")
    show_collected_letters()
    while True:
        cryptex = str((input("Enter your collected letters here: \n")).upper())
        if cryptex == str("PYTHONIC"):
            print("You've got it!")
            break
        else:
            print("Nothing happens. Are the letters in the right order?")
            print(Fore.GREEN + "HINT: Maybe they form a word...a language"
                  + " perhaps.\n ")
            print(Style.RESET_ALL)
            continue


def win_treasure():
    clear()
    print("        ⣤⣤⣤⣤⣤⣤⣤⣤⣤")
    print("        ⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("       ⠀⣿⣿⣿⣿⠉⠉⠉⠉⠉")
    print("        ⣿⣿⣿⣿⣤⣤⣤")
    print("        ⣿⣿⣿⣿⣿⣿⣿")
    print("        ⣿⣿⣿⣿")
    print("        ⣿⣿⣿⣿⣿⣿")
    print("     ⢀⣀⣿⣿⣿⣿⣀⡀")
    print("  ⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄")
    print("⢰⣿⣿⣿⡿⠋⠉⠉⠙⢿⣿⣿⣿⡆")
    print("⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿")
    print("⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿")
    print("⠸⣿⣿⣿⣷⣄⣀⣀⣠⣾⣿⣿⣿⠇")
    print("  ⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃")
    print("   ⠀⠈⠉⠛⠛⠛⠛⠉⠁")
    print("You've got it! A small door opens on the front of")
    print("the chest to reveal a key hole...\n")
    print("You get out Grandpa Indy's old key and it's a perfect fit.")
    print("The treasure chest opens and you look inside...")
    print("Jewels of all shapes and sizes surround an old book.")
    print("It looks like it contains some sort of treasure map.\n")
    print("Have you had enough treasure hunting for one lifetime,")
    print(" or are you ready for more?")
    while True:
        replay = (input("Type Enough (E) or More (M): \n").upper())
        if replay == ("M"):
            clear()
            print(f"Good luck with that next treasure map then!")
            print("You are a born explorer!")
            reset_game()
            main()
            break
        elif replay == ("E"):
            clear()
            reset_game()
            print("Safer back in the classroom huh?!")
            print(f"Goodbye then.")
            break
        else:
            print(f"I don't understand what {replay} means. Can you"
                  + " please repeat?\n")
            continue


def clear():
    """
    Clears all the previous text output in the user terminal
    """
    os.system("clear")


def add_collected_letters(letter):
    """
    After solving each puzzle, the explorer receives a letter. These
    are collected and the user display updated after each game.
    """
    letters_collected.append(letter)


def show_collected_letters():
    """
    After solving each puzzle, the explorer receives a letter. These
    are collected and the user display updated after each game.
    """
    print(Fore.YELLOW + "Letters Collected: ")
    for new_lst in letters_collected:
        no_brackets_lst = (','.join(new_lst))
        print(Fore.YELLOW + no_brackets_lst)
    print(Style.RESET_ALL)


def reset_game():
    """
    Reset the figures in the google worksheet, and start the game
    again from the beginning.
    """
    clear()
    clear_collected_game_data()


def clear_collected_game_data():
    """
    Whenever a new game is started, all the data in
    the worksheet containing the collected puzzle letters
    is deleted.
    """
    letters_collected.clear()
    explorer.clear()


def main():
    """
    Run all program functions
    """
    explorer_data = game_intro()
    clear_collected_game_data()
    puzzle_one_letter = puzzle_room_one()
    add_collected_letters(puzzle_one_letter)
    continue_or_quit()
    puzzle_two_letter = puzzle_room_two()
    add_collected_letters(puzzle_two_letter)
    continue_or_quit()
    puzzle_three_letter = puzzle_room_three()
    add_collected_letters(puzzle_three_letter)
    continue_or_quit()
    puzzle_four_letter = puzzle_room_four()
    add_collected_letters(puzzle_four_letter)
    continue_or_quit()
    puzzle_five_letter = puzzle_room_five()
    add_collected_letters(puzzle_five_letter)
    continue_or_quit()
    puzzle_six_letter = puzzle_room_six()
    add_collected_letters(puzzle_six_letter)
    continue_or_quit()
    puzzle_seven_letter = puzzle_room_seven()
    add_collected_letters(puzzle_seven_letter)
    continue_or_quit()
    puzzle_eight_letter = treasure_room()
    add_collected_letters(puzzle_eight_letter)
    continue_or_quit()
    treasure_chest()
    win_treasure()


main()
