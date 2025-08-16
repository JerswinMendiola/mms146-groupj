from Question import Question
from Player import Player
import os
import random
import string

class QuizGame:
    '''
    This class handles the quiz game logic.
    '''
    def __init__(self, questions):
        ''' 
        This initializes the quiz game class. It will make a list of questions and the player's score variable.
        '''
        self.__question_bank = questions
        self.__score = 0
        self.__curent_questions_index = 0

    def display_question(self):
        ''' 
        This displays a selected question to the user.
        '''
        os.system('cls')
        current_question = self.__question_bank[self.__curent_questions_index]
        print(current_question.get_question_text())
        current_answer = 0
        for answer in current_question.get_answers():
            letter_beside_answer = string.ascii_uppercase[current_answer]
            current_answer += 1
            print(letter_beside_answer + " - " + answer)
        user_answer = input("Enter your answer: ")
        self.check_answer(user_answer,  current_question)

    def check_answer(self, user_answer, current_question):
        ''' 
        This checks if the user chose the correct answer for a selected question.
        '''
        if user_answer.lower() == current_question.get_correct_answer().lower():
            os.system('cls')
            print("Correct!")
            self.__score += 1
        else:
            os.system('cls')
            print("Incorrect!")
        
        input("Press Enter to continue...") # Pause so user can read "Correct!" or "Incorrect!"

        self.__curent_questions_index += 1 # Always advance to the next question

        if self.__curent_questions_index < len(self.__question_bank):
            self.display_question() # Display next question if available
        else:
            self.display_final_results() # End game if all questions answered

    def get_score(self):
        ''' 
        This retrieves the score of the player in the current game.
        '''
        return self.__score

    def shuffle_question_bank(self):
        ''' 
        This randomizes the questions order.
        '''
        random.shuffle(self.__question_bank)

    def reset_game(self):
        ''' 
        This resets the current game.
        '''
        self.__score = 0
        self.__current_question_index = 0

    def display_final_results(self):
        '''
        Displays the final results of the quiz
        '''
        os.system('cls')
        print("Your Final Score: " + str(self.get_score()))
        self.save_score()
        self.reset_game()
        input("")
    
    def save_score(self):
        pass

    def get_questions(self):
        '''
        Returns the question bank.
        '''
        return self.__question_bank

def send_to_option(option):
    os.system('cls')
    if option == 1:
        start_game()
        return
    elif option == 2:
        print("HELP MENU GOES HERE")
    elif option == 3:
        print("HIGHSCORES:")
    else:
        exit()
    input()
    on_main_menu = True
    main_menu(on_main_menu)

on_main_menu = True
def main_menu(main_menu):
    os.system('cls')
    print("Welcome to the Smartest Byte!")
    print("1 - Start the game")
    print("2 - Instructions")
    print("3 - Highscores")
    print("4 - Quit game")
    option = int(input("Select an option: "))
    if option < 0 or option > 4:
        os.system('cls')
        pass
    else:
        main_menu = False
        send_to_option(option)

def load_questions():
    questions = [
        Question("The sky is blue.",["True","False"],"A"),
        Question("The Philippine flag has four colors.",["True","False"],"A"),
        Question("Which of the following is the smallest continent?",["North America","South America","Africa","Australia"],"D"),
        Question("Which company developed the Android Operating system?", ["Apple", "Microsoft", "Amazon", "Google"], "D"),
        Question("Which of the following is a type of Malware?", ["Firewall", "Antivirus", "Trojan Horse", "Kaspersky"], "C"),
        Question("What does HTTP stand for?", ["HyperText Transfer Protocool", "HyperText Transfer Protocol", "HyperText Transmision Protocol", "HyperText Transmission Protocol"], "B"),
        Question("What does OOP stand for?", ["Oriented-Object Programming", "Object-Oriented Programming", "Object-Oriented Program", "Organize-Object Programming"], "B"),
        Question("Which gas do plants absorb from the atmosphere during photosynthesis?", ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "A"),
        Question("Which planet is known as the Red Planet?", ["Venus","Mars","Jupiter","Saturn"], "B"),
        Question("Who wrote the play Romeo and Juliet?", ["William Shakespeare","Charles Dickens","Mark Twain","Leo Tolstoy"], "A"),
        Question("What is the capital city of Japan?", ["Seoul","Beijing","Tokyo","Bangkok"], "C"),
        Question("Which element has the chemical symbol O?", ["Gold","Oxygen","Osmium","Ozone"], "B"),
        Question("In what year did the Titanic sink?", ["1912","1920","1905","1899"], "A")
    ]
    return questions

def start_game():
    while True:
        os.system('cls')
        player_name = input("Enter your name: ")
        if player_name:
            break
    current_player = Player(player_name)
    quiz_game = QuizGame(load_questions())
    quiz_game.shuffle_question_bank()
    quiz_game.display_question()

if __name__ == "__main__":
    while True:
        main_menu(on_main_menu)