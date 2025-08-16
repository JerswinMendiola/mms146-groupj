class Question:
    def __init__(self, question_text: str, answers: list, correct_answer: str):
        '''
        Initialization of a new Question object
        '''
        self.__question_text = question_text        # The text of the question (string)
        self.__answers = answers                    # List of the possible answers/choices (list)
        self.__correct_answer = correct_answer      # The correct answer among the 'answers' (string)
        
    def get_question_text(self):
        '''
        Returns the text of the question
        '''
        return self.__question_text
    
    def get_answers(self):
        '''
        Returns the list of the possible answers/choices
        '''
        return self.__answers
    
    def get_correct_answer(self):
        '''
        Returns the correct answer
        '''
        return self.__correct_answer