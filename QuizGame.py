class QuizGame:
    '''
    This class handles the quiz game logic.
    '''
    def __init__(self, questions):
        ''' 
        This initializes the quiz game class. It will make a list of questions and the player's score variable.
        '''
        self.__question_bank = questions            #List of question(list)
        self.__score = 0                            #Current player score(int)
        self.__curent_questions_index = 0           #Index of the current question (int)

    def display_question(self):
        ''' 
        This displays a selected question to the user.
        '''
       if self.__current_question_index < len(self.__question_bank):
           question = self.__question_bank[self.__current_question_index]
           print(f"\nQuestions {self.__current_question_index + 1}/{len(self.__question_bank)}")
           print(question.text)
           for i, option in enumerate(question.options, 1):
               print(f"{i}. {option}")
            return question.text, question.options
        else:
            print("No more questions available.")
        
    def check_answer(self, user_answer):
        ''' 
        This checks if the user chose the correct answer for a selected question.
        '''
        if self.__current_question_index < len(self.__question_bank):
            question = self.__question_bank[self.__current_question_index]
            is_correct = user_answer.lower() == question.correct_answer.lower()
        if is_correct:
            self.__score =+ 1
            print("Correct!")
        else:
            print(f"Wrong! The Correct answer is: {question.correct_answer}")

    def get_score(self):
         ''' 
        This retrieves the score of the player in the current game.
        '''
        return self.__score, len(self.__question_bank)

    def shuffle_question_bank(self):
        ''' 
        This randomizes the questions order.
        '''
        random.shuffle(self.__question_bank)
        print("Questions have been shuffled.")

    def reset_game(self):
        ''' 
        This resets the current game.
        '''
        self.__score = 0
        self.__current_question_index = 0

    def is_game_over (self):
        '''
        Checks if all questions have been answered.
        '''
        return self.__current_question_index >= len(self.__questions_bank)

    def display_final_results(self):
        '''
        Displays the final results of the quiz
        '''
        total_score = self.get_score()
        print("/n" + "="*40)
        print("Quiz Completed!")
        print(f"Your Final Score: {score}/{total}')
