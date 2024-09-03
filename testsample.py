class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def set_exits(self, exits):
        """Set possible exits from the room."""
        self.exits = exits

    def add_item(self, item):
        """Add an item to the room."""
        self.items.append(item)

    def remove_item(self, item):
        """Remove an item from the room."""
        self.items.remove(item)

    def get_description(self):
        """Get a description of the room, including items and exits."""
        description = f"{self.description}\n"
        if self.items:
            description += "You see the following items: " + ", ".join(item.name for item in self.items) + ".\n"
        description += "Exits: " + ", ".join(self.exits.keys()) + "."
        return description


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        """Move the player to a different room, if possible."""
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You move {direction} to the {self.current_room.name}.")
        else:
            print("You can't go that way!")

    def take(self, item_name):
        """Take an item from the room and add it to the inventory."""
        item = next((item for item in self.current_room.items if item.name == item_name), None)
        if item:
            self.current_room.remove_item(item)
            self.inventory.append(item)
            print(f"You have taken the {item.name}.")
        else:
            print("That item is not here.")

    def show_inventory(self):
        """Display the player's inventory."""
        if self.inventory:
            print("You are carrying: " + ", ".join(item.name for item in self.inventory))
        else:
            print("Your inventory is empty.")


class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.player = Player(self.rooms['hall'])

    def create_rooms(self):
        """Create the rooms and link them together."""
        hall = Room("Hall", "You are in a large hall with a marble floor.")
        kitchen = Room("Kitchen", "You are in a kitchen. There is a disturbing smell.")
        dining_room = Room("Dining Room", "You are in a dining room with a long table.")

        # Linking rooms
        hall.set_exits({"north": kitchen, "east": dining_room})
        kitchen.set_exits({"south": hall})
        dining_room.set_exits({"west": hall})

        # Adding items
        knife = Item("knife", "A sharp-looking kitchen knife.")
        kitchen.add_item(knife)

        return {'hall': hall, 'kitchen': kitchen, 'dining_room': dining_room}

    def start(self):
        """Start the game loop."""
        while True:
            print(self.player.current_room.get_description())
            command = input("\nWhat do you want to do? ").strip().lower().split()

            if command[0] in ["go", "move"]:
                if len(command) > 1:
                    self.player.move(command[1])
                else:
                    print("Go where?")
            elif command[0] in ["take", "get"]:
                if len(command) > 1:
                    self.player.take(command[1])
                else:
                    print("Take what?")
            elif command[0] == "inventory":
                self.player.show_inventory()
            elif command[0] in ["quit", "exit"]:
                print("Thanks for playing!")
                break
            else:
                print("I don't understand that command.")

# To play the game, create a Game instance and start it
# game = Game()
# game.start()
