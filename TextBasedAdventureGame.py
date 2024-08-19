block_letters = r"""
   sss      eeeeee  rrrrr   iiiiiii         a        l
ss     ss   e       r    r     I           a a       l
ss          e       r    r     I          a   a      l
  sssss     eeee    rrrrr      I         aaaaaaa     l
       ss   e       r   r      I        a       a    l
ss     ss   e       r    r     I       a         a   l
   sss      eeeeee  r     r iiiiiii   a           a  lllllll   
"""

color_red = "\03391m"
color_reset = "\0330m"



class Game:
    def __init__(self):
        self.state = "start"  # Initial game state
        # You can add more attributes (e.g., player inventory, current location, etc.)

    def start(self):
        print(block_letters)
        print("Welcome to a suspicious and haunting cabin!")
        print("It's one of those cabins you would normally not go in,")
        print("but for the sake of the game, we are going to go in anyway.")
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
