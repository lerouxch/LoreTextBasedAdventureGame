block_letters = r"""
  ____   _____  _____  _    _  ____  
 |  _ \ |_   _||_   _|| |  | ||  _ \ 
 | |_) |  | |    | |  | |  | || |_) |
 |  __/   | |    | |  | |  | ||  __/ 
 |_|      |_|    |_|  |  \__/ |_|    
"""

color_red = "\03391m"
color_reset = "\0330m"



class Game:
    def __init__(self):
        self.state = "start"  # Initial game state
        # You can add more attributes (e.g., player inventory, current location, etc.)

    def start(self):
        print(block_letters)
        print("Welcome to the Enchanted Forest!")
        # Initialize game logic here

    def process_input(self, user_input):
        # Parse user input and update game state
        # Implement logic for different commands (e.g., 'go', 'inspect', 'take', etc.)
        pass

    def play(self):
        self.start()
        while self.state != "end":
            user_input = input("What will you do? ").lower()
            self.process_input(user_input)
        print("Thanks for playing!")

# Instantiate the game
my_game = Game()
my_game.play()
