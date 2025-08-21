from abc import ABC, abstractmethod

class AbstractQuizGame(ABC):
    @abstractmethod
    def display_question(self):
        """Display the current question to the user."""
        pass

    @abstractmethod
    def check_answer(self, user_answer, current_question):
        """Check if the user's answer is correct."""
        pass

    @abstractmethod
    def get_score(self):
        """Retrieve the current score of the player."""
        pass

    @abstractmethod
    def shuffle_question_bank(self):
        """Randomize the order of the questions."""
        pass

    @abstractmethod
    def reset_game(self):
        """Reset the current game state."""
        pass

    @abstractmethod
    def display_final_results(self):
        """Display the final results of the quiz."""
        pass

    @abstractmethod
    def save_score(self):
        """Save the player's score."""
        pass

