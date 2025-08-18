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