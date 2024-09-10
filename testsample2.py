import random

block_letters = r"""
L         OOOOO   RRRRRR    EEEEEEE
L        O     O  R     R   E
L        O     O  R     R   E
L        O     O  RRRRRR    EEEEE
L        O     O  R    R    E
L        O     O  R     R   E
LLLLLLL   OOOOO   R      R  EEEEEEE   
"""

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []
        self.location = None

    def move(self, direction, forest_map):
        if direction in self.location.exits:
            self.location = forest_map[self.location.exits[direction]]
            print(f"\n{self.location.description}")
            if self.location.enemy:
                print(f"A {self.location.enemy.name} appears!")
                return self.location.enemy #Triggers combat

        else:
            print("The forest is too dense. You can't go that way!")


    def pick_up_item(self, item):
        if item in self.location.items:
            self.inventory.append(item)
            self.location.items.remove(item)
            print(f"You picked up {item}.")
            if item == 'letter':
                print("""
                  To the reader of this letter, 
                  If you are reading this then that means I am dead.
                  You have made a grave mistake coming into this forest.
                  I lost all of my companions one by one trying to navigate and then escape this leafy tomb.
                  We began to lose our minds with each step we took.
                  There is something you should know,
                  this forest is plagued by a witch,  her ancient, terrible power and influence haunts every leaf and twig.
                  It is said that long ago a mage attempted to discover and defeat the witch but failed to withstand her magic.
                  There is hope however, the mage's staff is said to be the only item able to defeat her,
                  but the staff is long lost along with the mage deep in the forest.
                  Find the staff and defeat the witch, that is your only hope of leaving this terrible place.
                """)
            if item == 'sword':
                self.health += 15
                print("""
                  The inscription reads Aicamacil, which when translated means sharp sword. 
                  This is a truly good find, the perfectly forged ancient blade sits well in your hand.
                  This sword will definity come in handy if you run into unfriendly creatures.
                  """)
            if item == 'helm':
                self.health += 10
                print("""
                  You are most fortunate, this legendary piece of armor was forged in the time of heros long since past.
                  The blacksmiths of the days of old had special talents and techniques with shaping steel, these
                  talents and techniques have long since been forgotten.
                  Yes the items they forged were very beautiful but the real art was the abilities that the blacksmiths
                  of old working into the steel itself.
                  The Helm of Vigour is one of these items. It adds 10 points onto your health. 
                  """)    
        else:
            print(f"{item} is not here.")

    def show_inventory(self):
        if self.inventory:
            print("You have the following items:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

    def attack(self, enemy):
        damage = random.randint(10, 30)
        enemy.health -= damage
        print(f"You attack the {enemy.name} for {damage} damage!")

    def combat(self, enemy):
        print(f"A {enemy.name} appears!")
        while enemy.health > 0 and self.health > 0:
            action = input("\nWhat do you want to do? (attack, flee): ").lower()
            if action == 'attack':
                self.attack(enemy)
                if enemy.health > 0:
                    self.defend(enemy)
            elif action == 'flee':
                print("You flee down the path to the previous clearing!")
                self.move('south', forest_map)  # Assumes there's a way back
                return
            else:
                print("Command not valid.")

            if self.health <= 0:
                print("You have been defeated! The forest claims another soul...")
            elif enemy.health <= 0:
                print(f"You have defeated the {enemy.name}!")
                self.location.enemy = None
        
    
    def defend(self, enemy):
        damage = random.randint(5, 20)
        self.health -= damage
        print(f"The {enemy.name} attacks you for {damage} damage!")
        if self.health > 0:
            print(f"Your health: {self.health}")
        else:
            print("You have been defeated!")

class Enemy:
    def __init__(self, name, health=50):
        self.name = name
        self.health = health


class Room:
    def __init__(self, description):
        self.description = description
        self.exits = {}
        self.items = []
        self.enemy = None

    def set_exits(self, exits):
        self.exits = exits

    def set_items(self, items):
        self.items = items

    def set_enemy(self, enemy):
        self.enemy = enemy

def create_forest():
    # Defined Rooms(Clearings)
    forest_entrance = Room("""
                           You step into the forest, surrounded by tall dark trees and strange noises.
                           You turn around to find dense bushes and thorns where the forest entrance just was.
                           You are trapped, nowhere else to go but forward. 
                           You look ahead and see that there is a dark and seemingly un-ending path leading "North".
                           """)
    cross_roads = Room("""
                           You are eventually at a cross roads. The path splits into two. There appears to be clearings both to the "East" and "West" of you.
                       """)
    clearing1 = Room("""
                           You find yourself in what looks to be a long since abandoned camp of sorts.
                           Something bad happened here, upon closer inspection you don't see anywhere else to go but the way you came.
                           But what's that? You spot a glimmer of faded white from underneath some leaves next to old skeleton.
                           It's a mysterious "letter".
                     """)
    clearing2 = Room("""
                           You walk into another clearing, You notice that there are paths leading "North" and "West" the way you came.
                           You see some what apears to be ancient ruins ahead of you.
                           You step a bit closer and notice that the ruins are elvish.
                           This must have been a watch tower in the days of old.
                           They are now covered in vines and shrubs, but if you look closely you can still see 
                           some marble peeking through. Just a small glimmer of the elegant Elvish architecture.
                           After looking around for a bit, you find an old, long and flat crate,
                           the wood now rot with age.
                           Inside the long forgotten crate you see an elvish "sword".  
                     """)
    clearing3 = Room("""
                           Crouching down you break through the overgrown path, giving your eyes some time to adjust to the dim
                           light.
                           You look up and see the canopy is very dense, only allowing the smallest of sun beams to penetrate it's
                           mantle.
                           Looking down you see the undergrowth and surrounding brush entirely covered by webs.
                           Clank! Your foot hits something on the floor, carefully you cut away at the thick carpet of web,
                           revealing an old steel helmet. The "Helm" of Vigour. This treasure of the age of heros went missing 
                           many rotations ago, legends say that as the helmets name suggests, increases the helt of the one who wears it.
                           Disgusted you look cautiously around as to avoid touching the interlacing webbing at all costs.
                           The only visible way forward is a path to the "West" almost completely covered in webs.
                           You see a number of desecrated skeletons on the floor and stuck in the webs that now surround you.
                           This seems to be the final resting space for many poor souls.
                     """)
    clearing4 = Room(""" """)

    clearing5 = Room(""" """)

    clearing6 = Room(""" """)

    # Defined exits
    forest_entrance.set_exits({'north': 'cross_roads'})
    cross_roads.set_exits({'south': 'forest_entrance', 'west': 'clearing1', 'east': 'clearing2' })
    clearing1.set_exits({'east': 'cross_roads'})
    clearing2.set_exits({'west': 'cross_roads', 'north': 'clearing3'})
    clearing3.set_exits({'south': 'clearing2', 'west': 'clearing4'})
    clearing4.set_exits({'east': 'clearing3', 'north': 'clearing5'})
    clearing5.set_exits({'south': 'clearing4', 'east': 'clearing6'})


    # Items placed in rooms
    forest_entrance.set_items(['stick'])
    clearing1.set_items(['letter'])
    clearing2.set_items(['sword'])
    clearing3.set_items(['helm'])
    clearing4.set_items([])
    clearing5.set_items([])
    clearing6.set_items([])

    # Enemies in rooms(clearings)
    clearing3.set_enemy(Enemy("Spider", 30))
    clearing5.set_enemy(Enemy(None))
    clearing6.set_enemy(Enemy(None))

    

    # Map creation
    forest_map = {
        'forest_entrance': forest_entrance,
        'cross_roads': cross_roads,
        'clearing1': clearing1,
        'clearing2': clearing2,
        'clearing3': clearing3,
        'clearing4': clearing4,
        'clearing5': clearing5,
    }

    return forest_map

def combat_loop(player, enemy):
    """Handles combat between player and enemy."""
    while enemy.health > 0 and player.health > 0:
        action = input("\nWhat do you want to do? (attack, flee): ").lower()
        if action == 'attack':
            player.attack(enemy)
            if enemy.health > 0:
                player.defend(enemy)
        elif action == 'flee':
            print("You flee to the previous room!")
            return False  # The player fled, so return False
        else:
            print("Invalid command.")

def game_loop(player, forest_map):
    print(block_letters)
    print(f"WELCOME!, {player.name}. You find yourself standing at the edge of a big forest, in a world almost like ours.")
    print("A World riddled in fantasy and LORE, filled with creatures and monsters and more.")
    print("The forest is huge, stretching from horizon to horizon,")
    print("eventually you make your way to an opening into the dense brush.")
    print("The path ahead is dark and shadowed from the sunlight,")
    print("a cold breeze blows onto you, the road ahead isn't going to be easy.")
    print("For your sake I hope you are ready, the biggest challenge of your life awaits...")
    print(player.location.description)

    while player.health > 0:
        command = input("\nWhat do you want to do? (move, pick up, inventory, quit): ").lower()
        if command == 'move':
            direction = input("Which direction? (north, south, east, west): ").lower()
            enemy = player.move(direction, forest_map)
            if enemy:
                combat_over = combat_loop(player, enemy)
                if combat_over:
                    break  # Exit game loop if the player is defeatedp)
        elif command == 'pick up':
            item = input("What do you want to pick up? ").lower()
            player.pick_up_item(item)
        elif command == 'inventory':
            player.show_inventory()
        elif command == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")

# Initialized game
forest_map = create_forest()
player = Player(name="Adventurer")
player.location = forest_map['forest_entrance']

# Game loop start
game_loop(player, forest_map)
