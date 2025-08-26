from AbstractQuizGame import AbstractQuizGame
from Question import Question
from Player import Player
import os
import random
import string

class QuizGame(AbstractQuizGame):
    '''
    This class handles the quiz game logic.
    '''
    def __init__(self, questions, player):
        ''' 
        This initializes the quiz game class. It will make a list of questions and the player's score variable.
        '''
        self.__question_bank = questions
        self.__score = 0
        self.__curent_questions_index = 0
        self.__player = player
        self.check_player_saves(player)

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
        print("X - Exit and Save Progress")
        user_answer = input("Enter your answer: ")
        self.check_answer(user_answer,  current_question)

    def check_answer(self, user_answer, current_question):
        ''' 
        This checks if the user chose the correct answer for a selected question.
        '''
        if user_answer.lower() == "x":
            self.save_player_progress()
            return
        elif user_answer.lower() == current_question.get_correct_answer().lower():
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
        player_name = self.get_player().get_name()
        self.save_score(player_name, self.get_score())
        self.reset_game()
        input("")
    
    def get_player(self):
        '''
        Returns the Player object associated with the current game.
        '''
        return self.__player
    
    def save_score(self,name,score):
        '''
        Save a score to the text file.
        '''
        existing_scores = self.load_scores()
        score_exists = None
        for scores in existing_scores:
            if scores[0] == name:
                score_exists = scores
                break
        if score_exists != None:
            if score > score_exists[1]:
                existing_scores.remove(score_exists)
                existing_scores.append([name, score])
        else:
            existing_scores.append([name, score])
        
        with open("save_data.txt", 'w') as file:
                for score in existing_scores:
                    for i in score:
                        file.write(str(i) + "\n")

    def load_scores(self):
        '''
        Load all scores from the text file and return as dictionary.
        Creates empty file if it doesn't exist.
        '''
        scores = []
        save_data_file = "save_data.txt"
        
        if not os.path.exists(save_data_file):
            with open(save_data_file, 'w') as save_file:
                pass
        else:
            with open(save_data_file, 'r') as save_file:
                line_count = 0
                player_name = ""
                for line in save_file:
                    line = line.strip()
                    if line_count % 2 == 0:
                        player_name = line
                    else:
                        score = int(line)
                        scores.append([player_name, score])
                    line_count += 1
        return scores

    def check_player_saves(self, player):
        '''
        Checks for a saved game for the current player.

        This function checks if a save file exists for the given player name.
        If a file exists, it asks the user if they want to continue their saved game or start a new one.
        If no file exists or the user chooses a new game, the questions are shuffled and the game begins.
        '''
        player_name = player.get_name()
        if not os.path.exists(player_name + ".txt"):
            self.shuffle_question_bank()
            self.display_question()
        else:
            print("We have found that you have saved progress. Would you like to continue?")
            print("A - Continue")
            print("X - New Game")
            answer = input("")
            if answer.lower() == "a":
                self.load_player_progress(player_name)
            else:
                os.remove(player_name + ".txt")
                self.shuffle_question_bank()
                self.display_question()

    def load_player_progress(self, player_name):
        '''
        Loads a saved game state for the player from a text file.

        The function reads the player's score and the list of remaining questions from the save file.
        It then updates the game state with the loaded data.
        '''
        questions = []
        with open(player_name + ".txt", 'r', encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            
            # First line is the score
            self.__score = int(lines[0])
            
            # Process remaining lines starting from index 1
            line_counter = 1
            question_text = ""
            question_options = []
            question_answer = ""
            
            for i in range(1, len(lines)):
                line = lines[i]
                if line_counter == 1:
                    question_text = line
                    line_counter += 1
                elif line_counter == 2:
                    question_options = eval(line)  # Fixed: was question_text = eval(line)
                    line_counter += 1
                else:
                    question_answer = line
                    line_counter = 1
                    question = Question(question_text, question_options, question_answer)
                    questions.append(question)
        self.__question_bank = questions
        self.display_question()
        
    def save_player_progress(self):
        '''
        Saves the current player's game progress to a text file.

        The function stores the player's current score and the remaining questions
        in a file named after the player. This allows the user to continue their game
        at a later time.
        '''
        player_name = self.get_player().get_name()
        with open(player_name + ".txt", 'w', encoding="utf-8") as file:
                file.write(str(self.get_score()) + "\n")
                for i in self.__question_bank[self.__curent_questions_index:]:
                    file.write(i.get_question_text() + "\n")
                    file.write(str(i.get_answers()) + "\n")
                    file.write(i.get_correct_answer() + "\n")    
