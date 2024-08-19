block_letters = r"""
L         OOOOO   RRRRRR    EEEEEEE
L        O     O  R     R   E
L        O     O  R     R   E
L        O     O  RRRRRR    EEEEE
L        O     O  R    R    E
L        O     O  R     R   E
LLLLLLL   OOOOO   R      R  EEEEEEE   
"""

color_red = "\03391m"
color_reset = "\0330m"



class Game:
    def __init__(self):
        self.state = "start"  # Initial game state
        # You can add more attributes (e.g., player inventory, current location, etc.)

    def start(self):
        print(block_letters)
        print("WELCOME! You find yourself standing at the edge of a big forest, in a world almost like ours.")
        print("A World riddled in fantasy and LORE, filled with creatures and monsters and more.")
        print("The forest is huge, stretching from horizon to horizon,")
        print("eventually you make your way to an opening into the dense brush.")
        print("The path ahead is dark and shadowed from the sunlight,")
        print("a cold breeze blows onto you, the road ahead isn't going to be easy.")
        print("Do you dare to enter the forest??")
        
        
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
