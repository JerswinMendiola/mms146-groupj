from QuizGame import QuizGame, Question, Player, os

def get_questions(self):
    '''
    Returns the question bank.
    '''
    return self.__question_bank

def send_to_option(option):
    '''
    Directs the user to the selected menu option.

    This function clears the console and executes the logic corresponding to the user's menu choice.
    - Option 1: Starts the quiz game.
    - Option 2: Displays game instructions.
    - Option 3: Shows the highscores.
    - Any other option: Exits the program.
    '''
    os.system('cls')
    if option == 1:
        start_game()
        return
    elif option == 2:
        print("INSTRUCTIONS:")
        print("1. To start the game, enter your name.")
        print("2. Answer a series of random multiple-choice or true/false questions on a variety of topics.")
        print("3. Type the letter of your answer (A, B, C, or D) and press Enter to submit.")
        print("4. Earn one point for each correct answer.")
        print("5. The goal is to get the highest score you can!")
        print("6. You can view the highscores from the Main Menu.")
        print("Press Enter to go back to Main Menu...")
    elif option == 3:
        print("HIGHSCORES:")
        scores = load_scores()
        if len(scores) > 0:
            for i in scores:
                print(i[0])
                print(i[1])
        else:
            print("There are no scores!")
    else:
        exit()
    input()
    on_main_menu = True
    main_menu(on_main_menu)

on_main_menu = True
def main_menu(main_menu):
    '''
    Displays the main menu of the quiz game.

    This function clears the console, presents the user with a list of options (Start, Instructions, Highscores, Quit),
    and prompts for a selection. It then validates the input and calls `send_to_option` with the user's choice.
    '''
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
    '''
    Initializes and returns a list of Question objects.
    This function creates a static list of questions, each with a question string, a list of answer options, and the correct answer.
    '''
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
        Question("In what year did the Titanic sink?", ["1912","1920","1905","1899"], "A"),
        Question("What is the capital of the Philippines?", ["Quezon City","Cebu","Manila","Davao"], "C"),
        Question("Which philosopher is known for the famous statement, 'I think, therefore I am'?", ["Socrates","René Descartes","Aristotle","Plato"], "B"),
        Question("What does DSLR stand for?", ["Digital Single-Lens Reflex","Dual Shutter Lens Range","Digital Shutter Light Recorder","Dynamic Single-Lens Render"], "A"),
        Question("Which online game became a hit during the pandemic where players are 'crewmates' or 'impostors'?", ["Roblox","Among Us","Genshin Impact","Valorant"], "B"),
        Question("Where is Kilometer Zero located in the Philippines?", ["Malacañang Palace","Quezon Memorial Circle, Quezon City","Magellan’s Cross, Cebu City","Rizal Park, Manila"], "D"),
        Question("What is the chemical symbol for Sodium?", ["Na","So","Sn","Sd"], "A"),
        Question("Which number is the Roman numeral 'X'?", ["5","10","50","100"], "B"),
        Question("What is the largest planet in our solar system?", ["Earth","Jupiter","Saturn","Neptune"], "B"),
        Question("Which company created the video game franchise 'Pokémon'?", ["Nintendo","Sony","Microsoft","Sega"], "A"),
        Question("Emilio Aguinaldo was the first President of the Philippines.", ["True","False"], "A"),

    ]
    return questions

def load_scores():
    '''
    Load all scores from the text file and return as dictionary.
    Creates empty file if it doesn't exist.
    '''
    scores = []
    save_data_file = "save_data.txt"
    
    if not os.path.exists(save_data_file):
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
    
def start_game():
    '''
    Initiates the quiz game.
    This function prompts the user to enter their name, creates a `Player` instance, and then
    starts a `QuizGame` with the loaded questions and the new player.
    '''
    while True:
        os.system('cls')
        player_name = input("Enter your name: ")
        if player_name:
            break
    current_player = Player(player_name)
    quiz_game = QuizGame(load_questions(), current_player)

if __name__ == "__main__":
    while True:
        main_menu(on_main_menu)
