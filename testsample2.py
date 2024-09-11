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
            To the unfortunate soul who reads this,
            
            If these words have reached your eyes, then my fate is sealed, and I am no more. 
            I would beg you, turn back now, but it is already too late. 
            You have wandered into a place where no living being belongs.
            
            This forest… it consumes.
            I watched my companions fall, one by one, swallowed by the darkness that lives here. 
            The deeper we ventured, the more the air itself twisted our minds, whispering promises and threats in voices we could not see. 
            By the end, we were nothing but shadows of who we once were, stumbling through a maze of madness.
            But it is not the forest you should fear. No… something far worse lurks here. 
            An ancient witch, a creature of pure malice, dwells within these cursed woods. 
            Her presence is everywhere, an unseen force guiding every snapped twig, every rustling leaf. 
            Her power is old, far older than any mortal can comprehend, and her curse lingers over this place like a disease.
            Long ago, a mage, foolish and brave, tried to challenge her, to free this forest from her grasp. 
            But he failed. His magic was no match for her dark arts, and now his bones lie forgotten, tangled in roots and vines. 
            Only his staff, imbued with the last of his power, holds any hope of banishing her… 
            but it too is lost to the forest, buried with him somewhere in this endless green hell.
            If you wish to survive, if you wish to escape, you must find the staff. It is the only thing that can destroy her, the only way out. 
            But be warned: the forest will not give it up easily, and neither will she.

            Godspeed, and may fortune favour thee, for naught else will.
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
                          You step cautiously into the forest, the towering trees looming overhead, 
                          their gnarled branches twisting like skeletal hands reaching for you. 
                          The air is thick with the weight of shadows, and strange, unearthly noises echo through the trees, setting your nerves on edge.

                          When you turn to glance back, your blood runs cold. The entrance you came through is gone, 
                          replaced by an impenetrable wall of thorn-covered bushes, the vines twisting in ways that seem unnatural, as if alive. 
                          There is no way back.

                          You are trapped.

                          With no choice but to press onward, your eyes fix on the only path before you a narrow trail that stretches endlessly into the darkness, 
                          disappearing into the unknown. The wind whispers as it moves through the trees, carrying with it a name you do not recognize, 
                          and you realize that the only way is "north".
                           """)
    cross_roads = Room("""
                           After what feels like hours of wandering through the oppressive darkness, you find yourself standing at a crossroads. 
                           The narrow path you have been following splinters into two directions, each more unsettling than the last. 
                           The forest seems to hold its breath as if watching, waiting for your next move.

                           To the "East", the trees thin slightly, revealing a small, dim clearing bathed in an eerie, unnatural light. 
                           The ground there is oddly disturbed, as if something has been recently unearthed. 
                           Faint whispers ride the wind, too low to comprehend, but their presence sends a chill crawling down your spine.

                           To the "West", another clearing beckons, though it is darker, the air there heavier. 
                           The shadows cling thickly to the ground, and you can feel an oppressive weight pressing on your chest the closer you get. 
                           A distant, rhythmic sound like the very faint beating of drums or a pulse, echoes from that direction.

                           Both paths feel wrong, and yet, there is no turning back. 

                           You must choose...
                       """)
    clearing1 = Room("""
                           You stumble into what appears to be the remnants of a long-forgotten camp. 
                           The air is thick with the scent of decay, and the once-lively space now stands silent, frozen in time. 
                           Tattered tents sag under the weight of age, and rusted tools lie scattered across the ground, untouched for what feels like centuries. 
                           The ground is strewn with broken bones—silent witnesses to something terrible that happened here.

                           As you cautiously step further, you realize with growing dread that there is no path forward but only the way you just came. 
                           But just as you begin to turn, something catches your eye. 
                           Beneath a pile of rotting leaves and dirt, near the remains of a long-dead skeleton, you spot a faint glimmer. 
                           A piece of something… white.

                           Kneeling down, your fingers brush away the leaves, revealing an ancient, crumbling "letter" clutched in the bony hand of the corpse. 
                           The paper is yellowed with age, the ink almost faded, yet somehow it feels… important.

                           The wind stills. The forest grows eerily quiet.
                     """)
    clearing2 = Room("""
                           You emerge into another clearing, the dense trees parting to reveal a strange and quiet scene before you. 
                           To the "North", the path stretches further into the forest's shadowy heart, while to the West lies the way you came.
                           But it is what stands ahead that captures your gaze.

                           Ancient ruins, half swallowed by nature, loom silently before you. As you step closer, the unmistakable craftsmanship is clear. 
                           These are Elvish ruins, once a proud watchtower from a forgotten age. 
                           The once-glorious structure is now crumbling, overtaken by vines and dense shrubbery, the stone weathered by time. 
                           Yet, if you look closely, you can see the smooth marble beneath the wild overgrowth, 
                           its elegant curves and intricate designs still whispering of the craftsmanship that shaped it.

                           The wind stirs softly, as if the ruins themselves breathe with the memory of those who once guarded this place.

                           After a time of searching, your eyes fall upon an old crate, long and flat, tucked away beneath layers of moss and leaves. 
                           The wood is fragile, rotted from age, and creaks softly as you pry it open. 
                           Inside, you find something remarkable, a forgotten Elvish "sword", lying untouched by time. 
                           It's hilt is engraved with ancient symbols, and though the blade is dulled by the years, it still carries the grace of its Elvish makers, 
                           glinting faintly in the dim light.

                           This blade was forged for a purpose. You can feel it.
                     """)
    clearing3 = Room("""
                           Crouching low, you push through the overgrown path, branches and vines catching at your clothing as the air grows thick with dampness.
                           Your eyes slowly adjust to the dim, suffocating light. 
                           Above, the canopy is dense, a ceiling of leaves so tightly woven that only the faintest slivers of sunlight manage to pierce its dark mantle.

                           As you glance down, your stomach churns. 
                           The forest floor and surrounding undergrowth are buried beneath a thick, suffocating layer of webs, 
                           the massive, intricate strands that glisten in the pale light. 
                           The webbing stretches far, too vast to be the work of any normal spider.
                           Many a skeleton lay desecrated and entombed in the dense webs.

                           Suddenly CLANK! your foot strikes something solid beneath the mass of webs. Heart racing, you crouch to investigate. 
                           Using your blade, you cut carefully through the sticky, stubborn strands, revealing what lies beneath. Your breath catches.

                           An ancient, steel "helm" emerges from the webbed shroud, its surface dull and tarnished with time, but unmistakable in design. 
                           The Helm of Vigour. Once a treasured artifact from the Age of Heroes, it vanished from all knowledge many ages ago. 
                           Legends whispered of its power, the ability to bestow unnatural endurance upon its wearer, strengthening both body and spirit. 
                           
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
            return False  
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
