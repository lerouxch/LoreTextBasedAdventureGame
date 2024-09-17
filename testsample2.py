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
            There will be moments where the forest almost swallows you.
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
            This adds 15 points to your health.
                  """)
            if item == 'helm':
                self.health += 10
                print("""
            Holding it in you hand sends vibrations up your arms,
            some of it's legendary essence is still remains. 
            You are most fortunate, this legendary piece of armor was forged in the time of heros long since past.
            The blacksmiths of the days of old had special talents and techniques with shaping steel, these
            talents and techniques have long since been forgotten.
            Yes the items they forged were very beautiful but the real art was the abilities or traits 
            that the blacksmiths of old worked into the steel itself.
            The Helm of Vigour is one of these items. It adds 10 points onto your health. 
                  """) 
            if item == 'potion':
                self.health - 15
                print("""
            This fire potion is not one of the good kinds of potion.
            As you pour the mysterius liquid down your throat, you feel
            the sensation of burning, not a physical burning and as if you
            life force is burning up.
            This potion has taken away 5 health points.
            It would be wise to consider finding a way of finding
            some aid to bring your health back up or you won't last
            too much longer in this place.
                    """)
            if item == 'blue bottle':
                self.health += 20
                print("""
            You reach out with trembling hands and carefully grasp the blue bottle. 
            The sprite watches in silence, its emotionless gaze unwavering. 
            As you uncork the bottle, a faint, cool mist escapes, swirling briefly before vanishing into the air.
                      
            Hesitant but driven by hope, you bring the bottle to your lips and take a small sip. 
            The liquid is cool, refreshingly so, sliding down your throat like liquid moonlight. 
            Almost immediately, you feel a strange hum within your chest, a deep, resonant pulse that spreads through your veins.
                      
            Your body surges with renewed vitality. It begins slowly at first, but then, with every passing second, the sensation builds. 
            A warmth spreads through your limbs, a powerful, invigorating force that pushes away the exhaustion, 
            the aches, and the weariness that had weighed you down. Your breath steadies, your vision sharpens, and your muscles feel lighter, stronger.
                      
            As the energy courses through you, you realise the truth: your choice was indeed wise. 
            The bottle's gift is not only healing your body, but it seems to be restoring a small part of your spirit, 
            as though it is giving back what the forest has slowly been stealing from you. Every wound, every bruise, every ounce of fatigue melts away.
                      
            You feel a surge of life that you haven't felt in ages. 
            Rejuvenated, stronger, and clearer of mind, you stand taller, 
            knowing this small reprieve may be what you need to survive the trials ahead.
                      
            It has added 20 points to your health.
                    """)
            if item == 'green bottle':
                self.health - 15
                print("""
            Cautiously, you reach out for the green bottle, its glass unnaturally cold in your trembling hand.
            The still air around you feels thick with anticipation, as though the entire forest is holding its breath. 
            Slowly, you uncork the bottle, a faint hiss escaping as the seal breaks.
            The water sprite hovers in silence, watching, and the faces beneath the pond seem to grow more intense in their gaze, 
            their eyes locked onto you as if they already know your fate.
                      
            With your heart pounding, you raise the bottle to your lips, the liquid inside swirling with an unsettling energy. 
            The sour taste hits your tongue immediately, bitter and unpleasant. You swallow, and for a moment, nothing happens.
                      
            Then, without warning, a sharp, searing pain shoots through your chest, as though your heart itself is being clenched by an icy fist. 
            You gasp for breath as a strange green tinge begins to creep along your veins, spreading like poison beneath your skin. 
            Your whole body convulses, throbbing with unbearable pain as the venomous energy pulses through you. 
            Every muscle screams in agony, and your vision begins to blur.
                      
            You glance at the water sprite, your last hope for reprieve. But its once emotionless face now twists into a grotesque, mischievous grin. 
            Its eyes gleam with cruel satisfaction as it watches your suffering. You know, with chilling certainty, that you have made the wrong choice.
                      
            The drowned faces beneath the pond seem to mock you, their twisted expressions reflecting the fate that now awaits you. 
            The sprite's voice echoes in your mind, taunting, though it says nothing aloud. 
            Your body continues to betray you, wracked with pain and coursing with poison.
                      
            You have lost 15 health points.
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
        print(f"You attack {enemy.name} for {damage} damage!")

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
        print(f"{enemy.name} attacks you for {damage} damage!")
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
                           Your eyes slowly adjust to the dim, suffocating light. The path behind you slowly closes completely blocking any escape. 
                           Above, the canopy is dense, a ceiling of leaves so tightly woven that only the faintest slivers of sunlight manage to pierce its dark mantle.

                           As you glance down, your stomach churns. 
                           The forest floor and surrounding undergrowth are buried beneath a thick, suffocating layer of webs, 
                           the massive, intricate strands that glisten in the pale light. 
                           The webbing stretches far, too vast to be the work of any normal spider.
                           Many a skeleton lay desecrated and entombed in the dense webs.
                           Just barely you see a sliver of light breaking through the webbed wall...
                           Yes! It is a path to the "West" almost completely hidden by a curtain of silk.

                           Suddenly CLANK! your foot strikes something solid beneath the mass of webs. Heart racing, you crouch to investigate. 
                           Using your blade, you cut carefully through the sticky, stubborn strands, revealing what lies beneath. Your breath catches.

                           An ancient, steel "helm" emerges from the webbed shroud, its surface dull and tarnished with time, but unmistakable in design. 
                           The Helm of Vigour. Once a treasured artifact from the Age of Heroes, it vanished from all knowledge many ages ago. 
                           Legends whispered of its power, the ability to bestow unnatural endurance upon its wearer, strengthening both body and spirit. 
                           
                     """)
    clearing4 = Room("""
                           With much disgust, you tear your way through the webbed door that once blocked your path. 
                           A wave of warm air rushes past you as the clearing reveals itself, a perfect circle of scorched earth, the aftermath of some terrible firestorm. 
                           Yet the trees surrounding the clearing remain untouched, standing like silent sentinels around this blackened wasteland.
                           Once again the forest comsumes the path back, no where else to go but forward. 
                     
                           The ground beneath your feet is cracked and brittle, black as coal, and the air still carries the acrid scent of burnt wood.
                           Scattered across the clearing are the twisted remains of creatures reduced to ash and charred bone, 
                           their burnt shapes barely recognizable as once living creatures. 
                           A sense of profound desolation weighs heavily on you, as though the souls of those who perished here still linger in the air, watching.
                           At the centre of this destruction stands a single tree, strangely unharmed.
                           Its bark gleams unnaturally, smooth and untouched by the flames that ravaged everything around it.  
                           It seems to pulse with life, its presence both captivating and unsettling, as though it draws strength from the devastation at its feet.
                     
                           As you step closer, you feel an oppressive heat radiating from the tree, though no visible flames flicker across its surface. 
                           The heat grows more intense the nearer you draw, filling the air with a suffocating weight. 
                           Yet something compels you forward.
                           Upon closer inspection, you notice a narrow crevice in the tree's bark. Inside, partially hidden, rests a small vial—its glass warm to the touch. 
                           The liquid inside shimmers with a dangerous light, the substance within swirling with the vibrant hues of flame. 
                           This is no ordinary “potion”... it is pure fire, a concentrated essence of light or destruction. 
                           There is only one way to find out which it is...
                     
                           Beyond the tree, the path continues to the “North”, beckoning you onward.
                     """)
    clearing5 = Room(""" 
                           Exhausted, your mind teeters on the edge of collapse, the forest's relentless grip fraying your sanity with every passing step. 
                           You stumble into a clearing, and immediately, a strange stillness settles over you. 
                           The air is unnervingly calm, as though the entire world holds its breath. 
                           The ground beneath your feet is smooth, unnaturally solid stone, curving downward into a shallow depression at the centre.
                           
                           You glance back, but dread settles in your stomach. The path behind you is no more, swallowed whole by dense thorns and tangled vines. 
                           There is no turning back. The only way forward is a narrow path leading “East”, but before you can move, your eyes are drawn to the clearing's centre.
                           There, a perfectly still pond rests, it's dark and murky water reflecting the pale, sickly sky above. 
                           The surface is unnaturally calm, unnervingly so, like a mirror untouched by time or nature. 
                           As you step closer, something catches your eye. Faces, faint but distinct, just beneath the water's surface. 
                           Their ghostly forms are twisted and warped, some serene, others contorted in agony, their hollow eyes following your every movement. 
                           The air grows heavier as you stare back at them, your heart pounding in your chest.
                           The deeper you gaze, the more the pond pulls at you, as though it wishes to swallow you whole. 
                           But just as you feel the weight of the water drawing you closer, a soft glow begins to rise from the depths. 
                           The light grows brighter, moving swiftly upward, cutting through the dark water like a blade. Without so much as a ripple, a figure emerges.
                           
                           A water sprite.
                           
                           The ethereal creature hovers just above the pond, its pale blue skin shimmering in the dim light. 
                           Its eyes are dark, emotionless, staring through you as though you were nothing but a passing thought. 
                           The sprite's presence is unnerving, but it does not seem hostile. 
                           Instead, it moves with a haunting grace, its delicate form suspended between this world and the depths below.
                           Slowly, it raises its arms, revealing two clenched fists. 
                           The air around you seems to hum with unseen tension. 
                           
                           One by one, finger by finger, the sprite's hands open, revealing what lies within. 
                           In it's left hand rests a small, shimmering “blue bottle”, its surface glowing faintly like the light of a star. 
                           In it's right hand, a “green bottle”, equally small but swirling with an unsettling energy, as though something within it hungers.
                           
                           The sprite speaks, its voice soft but chilling, each word lingering in the air like a cold breath.
                           "You have a choice," it says in a slow, eerie, feminine whisper. 
                           "Choose wisely, for your very life depends on it. One can give... and one can take. Which will you pick up?"
                           
                           The bottles glimmer in the sprite's hands, and the weight of the decision presses down on you. 
                           The faces beneath the water continue to watch, their eyes pleading, warning, or mocking. 
                     
                           The wrong choice could seal your fate. 
                     """)

    clearing6 = Room("""
                           As you break into the clearing, a wave of unease washes over you. The first thing you notice is the absence of any visible paths. 
                           The forest seems to have abandoned this place entirely, leaving it to rot in isolation. 
                           The air is thick with the pungent scent of decay, heavy and suffocating, as if the clearing itself is steeped in death. 
                           No plants grow here, no animals stir, this is a place where life has long since withered away.
                      
                           At the heart of the clearing lies an enormous tree stump, leaning ominously toward the north. 
                           It's massive form is hollowed out, a dark cavity sinking into the earth. Glowing fungi cling to its surface, 
                           their eerie light pulsating like a sick heartbeat. 
                           The sickly glow casts unnatural shadows, flickering faintly, as if the stump itself still holds some twisted life force. 
                           The ground beneath your feet feels damp, almost spongy, with the rot that seems to seep from the stump into the earth around it.
                     
                           As you take a cautious step closer, your ears pick up the faint sounds from within the hollow, a scratching, rustling noise, 
                           like something lurking deep inside. The noise is unsettling, as though something unseen stirs within the decaying wood. 
                           Your gaze shifts, and you notice something even more disturbing: small, childlike handprints smeared along the edges of the hollow, 
                           dark and dried, their shapes faded but unmistakable. The prints are old, yet they cling to the stump as a warning or perhaps showing the path forward.
                     
                           The stump's interior spirals downward into the earth, a gaping maw leading into the unknown. 
                           The hollow appears large enough for you to descend into, though every instinct screams at you to turn back. 
                           Yet, there is no other path, the only way forward is “north”, into the underground darkness. 
                     
                           The noises from within grow louder, more insistent, as if calling to you. 
                           There is a strange, almost inviting pull in the air, coaxing you to step inside the stump's dark mouth and follow the descent into the depths below.
                           
                           Whatever lies within is waiting.
                     """)

    # Defined exits
    forest_entrance.set_exits({'north': 'cross_roads'})
    cross_roads.set_exits({'south': 'forest_entrance', 'west': 'clearing1', 'east': 'clearing2' })
    clearing1.set_exits({'east': 'cross_roads'})
    clearing2.set_exits({'west': 'cross_roads', 'north': 'clearing3'})
    clearing3.set_exits({'west': 'clearing4'})
    clearing4.set_exits({'north': 'clearing5'})
    clearing5.set_exits({'east': 'clearing6'})
    clearing6.set_exits({'north': 'clearing7'})



    # Items placed in rooms
    forest_entrance.set_items(['stick'])
    clearing1.set_items(['letter'])
    clearing2.set_items(['sword'])
    clearing3.set_items(['helm'])
    clearing4.set_items(['potion'])
    clearing5.set_items(['blue bottle', 'green bottle'])
    clearing6.set_items([])

    # Enemies in rooms(clearings)
    clearing3.set_enemy(Enemy("The Great Forest Spider", 54))
    clearing4.set_enemy(Enemy("The Fire atronach", 65))
    

    

    # Map creation
    forest_map = {
        'forest_entrance': forest_entrance,
        'cross_roads': cross_roads,
        'clearing1': clearing1,
        'clearing2': clearing2,
        'clearing3': clearing3,
        'clearing4': clearing4,
        'clearing5': clearing5,
        'clearing6': clearing6,
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

    if player.health <= 0:
        print("You have been defeated!")
        return True   #Player loses
    elif enemy.health <= 0:
        print(f"You have defeated {enemy.name}!")
        player.location.enemy = None
        return False  #Player Wins


def game_loop(player, forest_map):
    print(block_letters)
    print(f"WELCOME!, {player.name}. You find yourself standing at the edge of a big forest, in a world almost like ours.")
    print(f"A World riddled in fantasy and LORE, filled with creatures and monsters and more.")
    print(f"The forest is huge, stretching from horizon to horizon,")
    print(f"eventually you make your way to an opening into the dense brush.")
    print(f"The path ahead is dark and shadowed from the sunlight,")
    print(f"a cold breeze blows onto you, the road ahead isn't going to be easy.")
    print(f"For your sake I hope you are ready, the biggest challenge of your life awaits...")
    print(player.location.description)

    while player.health > 0:
        command = input("\nWhat do you want to do? (move, pick up, inventory, quit): ").lower()
        if command == 'move':
            direction = input("Which direction? (north, south, east, west): ").lower()
            enemy = player.move(direction, forest_map)
            if enemy:
                combat_over = combat_loop(player, enemy)
                if combat_over:
                    break  # Exit game loop if the player is defeated)
        elif command == 'pick up':
            item = input("What do you want to pick up? ").lower()
            player.pick_up_item(item)
        elif command == 'inventory':
            player.show_inventory()
        elif command == 'quit':
            print("No shame in quiting. Thanks for playing!")
            break
        else:
            print("Invalid command.")

# Initialized game
forest_map = create_forest()
player = Player(name="Adventurer")
player.location = forest_map['forest_entrance']

# Game loop start
game_loop(player, forest_map)
