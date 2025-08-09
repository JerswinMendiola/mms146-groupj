class QuizGame:
    '''
    This class handles the quiz game logic.
    '''
    def __init__(self,questions):
        ''' 
        This initializes the quiz game class. It will make a list of questions and the player's score variable.
        '''
        self.__question_bank = questions
        self.__score = 0

    def display_question(self):
        ''' 
        This displays a selected question to the user.
        '''
        pass

    def check_answer(self):
        ''' 
        This checks if the user chose the correct answer for a selected question.
        '''
        pass

    def get_score(self):
         ''' 
        This retrieves the score of the player in the current game.
        '''
        pass

    def shuffle_question_bank(self):
        ''' 
        This randomizes the questions order.
        '''
        pass

    def reset_game(self):
        ''' 
        This resets the current game.
        '''
        pass