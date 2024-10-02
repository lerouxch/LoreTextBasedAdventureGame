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

    #Item pick up loop and Item descriptions
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
            if item == 'hat':
                self.health += 5
                print("""
            You carefully pick up the mage's hat, its fabric fragile and worn with age. As your fingers brush against it, you feel an odd sensation,
            a faint pulse of warmth, like the dying embers of a once mighty fire. The hat, though delicate and frayed, 
            still holds a faint glimmer of the mage's ancient power. 
            It's subtle, but undeniable, a small, yet powerful reminder that hope remains, even in this forsaken place.
                      
            Clutching the hat, you feel a sense of purpose wash over you. It's as if a fragment of the mage's will has been passed onto you, 
            guiding you toward your goal.
            Though the witch's dark influence looms heavy in the air, this hat represents a shred of resistance, 
            a piece of the puzzle that may yet lead you to the staff, the only weapon capable of defeating her and breaking free from this cursed forest.
                      
            The road ahead is treacherous, the horrors of the cave and the forest still lurking, but the hat's faint magic hums in your hands. 
            It strengthens your resolve. You know now that the mage came this way, and though their fate remains unknown, 
            they left behind this small beacon, urging you onward.
            
            You clutch the mage's hat tightly, knowing it may be your only link to survival. 
            With renewed determination, you press forward, the path toward the north beckoning you deeper into the unknown. 
            Somewhere ahead, the staff awaits, and with it, the slim chance of defeating the witch and escaping this nightmare.
            
            The hat gives you 5 health points.
                    """)
            if item == 'robe':
                self.health += 10
                print("""
            This is indeed the mage's robe. You are clearly on the right path. Long ago, the mage passed through this very spot, 
            leaving this piece of their journey behind. The fabric is ancient, worn and weathered by time, 
            but surprisingly well preserved despite the harsh elements of the forest. 
            Its deep, faded colour still holds a faint shimmer of its once great magic.
            
            As you drape it around your shoulders, an unexpected warmth envelops you, almost like a gentle embrace. 
            The robe clings to you, its warmth sinking deep into your bones, soothing your aching body with each passing second. 
            A sense of comfort and protection washes over you, as though the mage's power lingers within the fabric, 
            offering you the strength to continue your perilous journey.
            
            You feel a renewed surge of energy, your mind sharpens, and for the first time in a while, a small flicker of hope stirs within. 
            The robe seems to hum with a quiet, ancient magic, a promise of guidance as you press forward. 
            
            It adds 10 health points.
                      """)
            if item == 'white':
                self.health += 5
                print("""
            You carefully pick up the white mushroom with red spots on its cap, its vibrant colour standing out unnaturally in the eerie clearing. 
            Hesitantly, you bring it to your lips, the smooth texture feeling strange in your hand. With a small breath, you bite down. The taste is peculiar, 
            not entirely unpleasant, though there's a bitter edge that lingers on your tongue.
            
            At first, nothing happened. Then, slowly, you feel a subtle change. Your muscles relax, and the weight of 
            exhaustion you've carried for so long seems to lift just a little.
            A small calmness spreads through your body, as though some of the ever present tension has released its grip.
            Your hunger, gnawing at you for hours, is a little diminished, and you realise with relief that the mushroom, against all odds, was not poisonous.
            
            A strange sense of ease settles over you, your mind feels clearer, and though the forest still presses in from all sides, 
            the danger of this moment seems less immediate.
                      
            5 health points are added.
                      """)
            if item == 'golden':
                self.health += 15
                print("""
            You cautiously pick up the golden mushroom, its delicate white spots almost glowing in the sickly, dim light of the clearing. 
            The deep golden sheen reflects the surrounding gloom, creating an eerie but captivating contrast. 
            You hesitate for a moment, but the allure of its shimmering surface is too tempting to resist. Slowly, you bring it to your lips and bite down.

            The taste surprises you. It's sweet, far sweeter than you expected, with an oddly delightful flavour that melts across your tongue, 
            completely unlike any mushroom you've ever encountered. For a moment, the bizarre world around you fades as the richness of the mushroom fills your senses.

            Then, suddenly, an intense sensation surges through your body. It feels as though a great weight has been lifted from your tired, aching shoulders. 
            The fatigue that had clung to you for so long dissipates, and a powerful sense of renewal sweeps over you. Your hunger vanishes, 
            leaving you feeling unexpectedly full, and your mind clears with startling clarity. It's as if the fog that clouded your thoughts has been lifted, 
            replaced by a sharp focus and newfound energy.

            For the first time in what feels like ages, you feel truly alive.

            This golden treasure has added 15 health points.
                      """)
            if item == 'apple':
                self.health += 15
                print("""
            You reach up and grasp the apple, and it feels refreshingly cool in your hand, as if it had been plucked fresh from a morning dew soaked orchard. 
            Tiny droplets of moisture cling to its surface, offering a momentary balm to your parched, cracked fingers, a small relief in this forsaken forest.
            You can't resist, you raise it to your mouth and take a big, hungry bite.

            The skin gives way with a crisp snap, and immediately your mouth is flooded with cool, sweet juice. The freshness of the apple is unlike anything you've 
            experienced in ages, and the tangy liquid spills over your dry, chapped lips, running down your chin in sticky rivulets. 
            It quenches not only your thirst but also your parched spirit, the sweetness overwhelming your senses as if it had been made to revitalise the weary.

            As you swallow, you feel the cool juice travel down your throat, refreshing you from the inside out. The sensation spreads throughout your body, 
            like ice water coursing through your veins, momentarily washing away the fatigue and darkness that have clung to you for so long. 
            You close your eyes, savouring the moment, feeling a sense of renewal for the first time since stepping foot in this cursed place.

            This added 15 much needed health points.
                      """)
            if item == 'staff':
                self.health += 110
                print("""
            You gently pull the staff from the heart of the cherry blossom tree, its silvery light pulsing in your hand. As you do, the tree slowly and gracefully closes, 
            sealing itself back up, as if it had been guarding this treasure for countless ages. The staff feels warm and alive, radiating the same protective 
            and ancient magic that fills this peaceful oasis.
            
            You know immediately, this is the mage's staff, the very object you've been searching for, the key to your survival and the salvation of this cursed land. 
            The power coursing through the staff resonates with the magic that created this sanctuary, a shield against the creeping darkness of the forest. 
            This staff had stayed here, rooted in the earth, drawing strength and light from the cherry blossom tree to keep the malevolent forces at bay, 
            waiting for someone worthy to wield it once again.
            
            This oasis, this sacred grove, was created not just as a place of refuge, but as a beacon of hope, a final stand against the evil that has corrupted the forest. 
            The staff, long forgotten, had protected itself, waiting for the one who would bring an end to the darkness that has plagued this land for far too long.

            As you grip the staff, the weight of your journey still presses heavily on your shoulders, the trials, the dangers, the dark creatures you've faced. 
            But now, with the staff in your hand, you feel a surge of hope that you haven't felt in what seems like ages. The light that the staff emanates 
            pushes back the shadows of fear that have haunted you, filling you with a newfound resolve.

            You've found the light you so desperately needed. You've found your chance to end this. With the mage's staff, you now carry the power to 
            defeat the evil that has claimed this land and find your way back to freedom. The path ahead will be hard, but you know now that you are not alone.

            You've found the light in the darkness, and it's time to wield it
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
                          and you realise that the only way is "north".
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
                           The air is thick with the scent of decay, and the once lively space now stands silent, frozen in time. 
                           Tattered tents sag under the weight of age, and rusted tools lie scattered across the ground, untouched for what feels like centuries. 
                           The ground is strewn with broken bones, silent witnesses to something terrible that happened here.

                           As you cautiously step further, you realise with growing dread that there is no path forward but only the way you just came. 
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
    clearing7 = Room("""
                           You step cautiously into the abyss, the light from the clearing fading behind you as the tunnel swallows you whole. 
                           Your footsteps echo in the tight, narrow passage, the ceiling just low enough that the roots of the cursed trees above brush against your head and shoulders.
                           The air is thick, oppressive, the weight of the forest still hanging over you, even beneath the ground. 
                           Your eyes struggle to adjust to the gloom, the darkness swallowing all but the faintest outlines of the path ahead.
                      
                           As you descend, the faint glow of fungi begins to light the way, their sickly greenish light pulsing erratically, 
                           as if struggling to push back the overwhelming darkness. The deeper you go, the stronger a pungent odour grows, 
                           filling your nostrils with the smell of rot and decay. The air is warm and moist, clinging to your skin like a second layer, 
                           leaving a sense of unease in the pit of your stomach. You notice a path to the “west” and “north”, 
                           a gentle reminder to be mindful of where you go, getting lost could seal your fate.
                      
                           Finally, the narrow tunnel opens up into a cavern, barely illuminated by the fungi clinging to the walls. 
                           The flickering light casts long shadows that dance eerily across the uneven stone. You stop in your tracks as a wave of nausea hits you, 
                           the stench in here overpowering. The warm, stagnant air presses against your skin, thick with the smell of death and old blood.
                     
                           The floor of the cavern is littered with skeletons, their twisted forms sprawled in unnatural positions. 
                           They are not human. You crouch down to examine one and realise, with growing horror, 
                           that they resemble elves but these elves had been horrifically transformed, their bones warped as if they had been tortured or twisted by some dark force. 
                           Their elongated limbs and disfigured skulls suggest a kind of suffering beyond what flesh could endure.
                     
                           Your heart pounds in your chest as you scan the area. This place is an orc hole, you realise, the remnants of a den long since abandoned… or so you hope. 
                           The sight of the tortured elven remains suggesting the dark and terrible creation of an orc.
                           The cavern is eerily quiet, but the unease in your gut refuses to fade. 
                           The dim light of the fungi flickers, casting fleeting glimpses of shadows that seem to shift when you're not looking directly at them. 
                           You hope the orcs are long gone, but the faint, distant sounds of scraping stone and low guttural noises make you fear otherwise.
                           
                           There is no turning back now.
                     """)
    clearing8 = Room(""" 
                           You step into the cave, moving cautiously through the dim light cast by the familiar glow of the fungi.
                           The air is thick and heavy, the scent of decay mingling with the damp earth around you. 
                           As your eyes adjust, you notice the walls, they're covered in carved faces, twisted in expressions of sheer terror, agony, and despair. 
                           Each one appears to be caught in the throes of a silent scream, mouths wide open as though trapped in an eternal torment. 
                           The longer you look, the more unsettling the sight becomes. The faces seem almost too real, as if they were once alive and somehow fused with the rock, 
                           their torment forever etched into the stone. The path continues on to the “north”.
                     
                           Occasionally, the silence is pierced by faint moans or distant, muffled cries. 
                           It's unclear whether these are echoes of the past or something more sinister, as though the very walls are haunted by the souls of those who ventured too far.
                           The cries seem to come from within the stone itself, disembodied and desperate, as if some of the faces are still alive, 
                           trapped in an eternity of suffering.
                     
                           You cautiously approach the central pillar. From afar, it appears to be a simple stone column, but as you step closer, you see it too is carved into a face. 
                           The right side is contorted in a look of pure, unrelenting horror, as if the figure had witnessed something beyond comprehension. 
                           The left side of the face is frozen in an expression of excruciating pain, 
                           it's features twisted and unnatural, as though carved in the midst of unbearable suffering.
                     
                           As you circle the pillar, your gaze falls upon something on the ground. 
                           A piece of fabric, old and covered in dust, lies against the base of the pillar. 
                           You crouch down, gently brushing the dust away with trembling hands. What you uncover sends a shiver of hope through you—a mage's “hat”, 
                           withered and faded by time. The material is delicate, but unmistakable, and though it's worn, the distinct shape is clear.
                     
                           The mage passed through here. You are on the right track. Though the surroundings are haunting and oppressive, 
                           this small discovery fills you with a flicker of hope. The mage once stood where you stand now, and perhaps he, too, 
                           heard the cries of the trapped souls and felt the same dread creeping into their bones.
                     """)
    clearing9 = Room("""
                           You step into the dimly lit cave, the ever-present glow of the fungi clinging to the walls casting an eerie light across the space. 
                           The cave is vast, its ceiling arching high above like a stone cathedral, dripping with stalactites that gleam faintly in the soft, pulsing light. 
                           The air is damp, with the faint sound of dripping water echoing through the chamber, creating an unsettling rhythm in the silence.
                     
                           The floor is uneven, jagged rocks protruding from the ground, making each step uncertain. 
                           In the distance, you notice a faint breeze coming from the “north”, where an opening seems to lead out of this cavernous space. 
                           The air from that direction feels slightly fresher, a sign that this might be a way forward, perhaps even an exit, though the forest 
                           beyond promises its own dangers.
                     
                           To the “west”, another tunnel yawns open, its entrance wide and foreboding. 
                           This passage is darker, the fungi's glow barely reaching into the mouth of the cave. You can't see far down this western path, 
                           but the faintest of sounds, perhaps a shuffling or distant echo, emanates from the darkness within, hinting that something may lie in wait, 
                           or that the cave itself holds more secrets yet to be uncovered.
                     
                           Between the northern exit and the western cave, a choice looms. The unknown darkness to the west calls out, 
                           while the path to the north offers a hint of escape.
                     """)
    clearing10 = Room(""" 
                           You step into the chamber, and the first thing that strikes you is the overwhelming sense of dread. The air is thick, stagnant, 
                           carrying the faint, sickly scent of decay. All around, the walls and floor are littered with bones, not merely discarded, 
                           but arranged with nightmarish intent. Skeletons of humans and creatures alike are posed in twisted tableaux, locked forever 
                           in their final, torturous moments.
                      
                           One skeleton hangs limply from the ceiling, bound by strands of dark, fibrous material, its arms stretched unnaturally high as if it had been 
                           pulled apart slowly. Nearby, a pair of human skeletons are arranged face-to-face, their bony hands gripping each other's necks, caught in an eternal, 
                           silent struggle. Animal skulls line the edges of the room, staring with empty eye sockets as though they, too, bear witness to the torment on display.
                      
                           The dark fibres that bind them are grotesque, organic strands that weave through the bones like a grotesque web, holding them in place 
                           as if part of some twisted art. The fibres pulse faintly, almost as if they are still alive, snaking through ribs and spines, 
                           adding an eerie semblance of movement to the still, lifeless forms.
                      
                           Each scene is more horrifying than the last creatures twisted into poses of agony, humans frozen in desperate pleas for mercy. 
                           Some are kneeling, hands clasped together in silent prayer, while others are sprawled across the floor, their faces contorted into expressions of terror, 
                           jaws agape in screams that will never be heard.
                       
                           As you move deeper into the chamber, you hear it, the faintest rattling of bones. It's soft, almost imperceptible at first, 
                           but it grows louder with each step. The sound doesn't come from one place, but from everywhere at once. You freeze, eyes darting from 
                           one grotesque display to another, but nothing moves. The bones remain still, yet the sound continues, a rhythmic, unnatural clinking, 
                           as if the skeletons are shifting just out of sight, aware of your presence, waiting for something.
                      
                           Above you, the ceiling seems to writhe with bones, smaller skeletons, perhaps children, bound together in an intricate, macabre spiral, 
                           their faces turned toward the centre of the chamber, as if in worship of some unseen horror. 
                           The sight fills you with a sickening realisation: this place is a shrine, and the bones its unwilling congregation.
                      
                           The walls seem to breathe, the fibrous strands tightening, pulling the skeletons ever closer to you. The rattling grows, 
                           and you realise, with mounting dread, that you are not alone in this chamber. You notice a path towards the "east”, 
                           a hope of escape of this room chamber of nightmares
                      """)
    clearing11 = Room("""
                           You stumble forward, your breath echoing off the wet stone walls of the cave as you near its exit. The damp air clings to your skin, 
                           and the sharp scent of mould fills your lungs. The faint light ahead grows brighter as you take the final steps toward freedom. 
                           But as you emerge from the cave's maw, you feel no relief, only an unsettling chill crawling up your spine.
                      
                           The transition is abrupt. The oppressive darkness of the cave gives way to a dense fog that swirls through a spooky forest clearing. 
                           The air is unnervingly still, thick with the scent of damp earth and decay. Every tree surrounding the clearing is gnarled and twisted, 
                           their blackened branches reaching upward like skeletal fingers clawing at the sky. The bark appears to be burned or diseased, 
                           riddled with a familiar pulsing fungi that give off a sickly glow, casting unnatural shadows that dance across the ground.
                      
                           The clearing itself feels wrong, as though you've stepped into a place that should not exist. The ground beneath your feet is soft and spongy, 
                           but when you look down, you see no grass, no moss, only a thin layer of rotting leaves that squelch with every step. 
                           In the centre of the clearing stands a lone, barren tree, its massive trunk warped and hollow. Despite the stillness, the hollow seems to whisper faintly, 
                           carrying voices that flicker in and out of your perception like a half-forgotten memory.
                      
                           A light breeze stirs the fog, revealing shadowy shapes hidden amongst the trees. You blink, and they're gone, as if they were never there. 
                           Yet the feeling of being watched is impossible to shake. Somewhere in the distance, a low, mournful wail echoes through the woods, 
                           followed by the rustling of unseen creatures moving just beyond the edge of your sight.
                      
                           The clearing seems alive, waiting, watching, and the only visible path leads deeper ”north” into the forest, where the darkness grows thicker, 
                           the trees more twisted. The oppressive silence weighs on you, and you sense that this is no place to linger.
                      """)
    clearing12 = Room("""
                           You step into the clearing, and a strange silence falls over you. Before you stretches a field of scarecrows, 
                           each one standing crooked and lifeless among the tall, dry grass. Their bodies are fashioned from twisted, rotting wood and faded cloth, 
                           and their heads are a grotesque mix of sacks, bones, and masks, all with tattered hats perched on top. 
                           Their faces are distorted, painted in crude, unnatural expressions, some smiling, others glaring with hollow, 
                           empty eyes. You see the path breaks off into three directions, “North”, “East” and “West”, you must choose your path wisely. 
                           On an empty pole in more or less of the centre of the clearing, you see an old "robe" hanging on the rotting pole. 
                           Could it be? Could it be the mages robe?

                           The air is still and heavy, with no breeze to stir the grass or the crows perched in the distance. 
                           As you cautiously begin walking through the field, the overwhelming sense that you are being watched creeps over you.
                           You quicken your pace, the tall, skeletal forms of the scarecrows lining the path, standing motionless, but something is wrong.

                           From the corner of your eye, you swear you see one of the heads move. A subtle, almost imperceptible shift. 
                           You stop, heart pounding, and turn your head to check—but the scarecrow remains still, its crude face staring blankly ahead. 
                           With each step, the sensation intensifies. Their heads slowly turn, just at the edge of your vision, following your every move. 
                           The further you walk, the more certain you are that they're watching you, but when you look directly at them, 
                           they're always frozen in place—silent, unmoving, yet undeniably aware.

                           The eerie silence is only broken by the faint rustling of fabric and straw, though the air is perfectly still. 
                           The feeling of eyes, hundreds of them, bears down on you, cold and hostile. Every scarecrow, with its empty gaze, 
                           seems to be daring you to glance away for just a moment longer, as if they're waiting for the right instant to move.

                           The exit to the clearing is far off, and the rows of scarecrows seem endless. Each one that you pass feels closer than the last, 
                           and the further you go, the more the silence presses in, the more the field seems to come alive with unseen movements. 
                           You quicken your pace, heart racing, but the turning heads continue to track you, watching, waiting.
                      """)
    clearing13 = Room("""
                           You step into the clearing, and your senses are immediately overwhelmed by the thick, sickly sweet smell that hangs in the air. 
                           The ground beneath your feet is soft, spongy, covered entirely by a carpet of dull green moss that gives with every step. 
                           All around you, mushrooms of various shapes and sizes rise from the mossy floor, their pale caps blending into the muted gloom of the forest. 
                           Some are tall and thin, others squat and bulbous, but all are dull, as though life has been drained from their colours. The path forward lies “north”.
                           
                           The air is dense, almost oppressive, with an underlying rot that clings to the back of your throat. 
                           The mushrooms sickly forms twist and bend in ways that seem unnatural, their stems curling like gnarled fingers reaching up from the earth. 
                           The longer you stand, the more it feels as though the clearing is somehow alive, the very air around you buzzing with an eerie energy.
                           
                           In the centre of the clearing, however, your eye is drawn to something that stands out amidst the gloom, a bright green moss covered rock. 
                           Perched atop the rock are two mushrooms, starkly contrasting with the dull, lifeless surroundings. One is “white” with vivid red spots on its cap, 
                           the colour almost too vibrant for this dreary place, while the other is “golden”, dotted with delicate white spots, 
                           its surface shimmering faintly in the dim light. They seem out of place, as though they don't belong to this forest, 
                           their colours glowing with an unnatural brilliance.
                           
                           The mushrooms seem to hold a  hidden secret, as if they hold a secret not meant for the eyes of mere mortals. 
                           You can't help but feel that whatever choice you make regarding these strange mushrooms could alter your fate, for better or worse.
                           
                           The only path is "North".
                      """)
    clearing14 = Room("""
                           You step into a peculiar clearing, and immediately your eyes are drawn to the long, thin branches stretching from trees on all sides. 
                           From these branches hang countless shadowy figures, their forms resembling people suspended in mid-air, 
                           motionless yet swaying gently despite the eerie absence of wind. The shadows seem to ripple with the faintest suggestion of movement, 
                           their features indistinguishable but unmistakably human like.

                           As you cautiously move forward, a chilling realisation dawns on you, the hanging shadows are watching you. 
                           Though you never see them turn, you feel their gaze, cold and empty, following your every step. 
                           The silence in the clearing is heavy and suffocating, pressing down like a weight on your chest, broken only by the occasional creak of a branch, 
                           brittle and fragile, as if at any moment it could snap, sending the figures crashing to the ground.

                           The stillness is unnerving, each step echoing in the unnatural quiet, and you can't shake the feeling that the shadows are waiting for something, 
                           waiting for you.
                      
                           The only parth forward is "North".
                      """)
    clearing15 = Room("""
                           Stepping into the clearing, you immediately notice the dense canopy overhead, the tree tops weaving together so tightly that only faint, 
                           sickly light filters through. Looking down, the ground is a patchwork of different grasses, moss, and even fur, grotesquely stitched together 
                           as though the very earth had been sliced apart and sewn back in a crude and unnatural manner. The seams between these patches pulse faintly, 
                           as if something beneath the surface is alive, struggling to break free.

                           The trees surrounding the clearing are equally disturbing, their trunks marred by ragged, stitched wounds, oozing thick, 
                           dark sap like the blood of a dying creature. As you step deeper into the clearing, an unsettling sensation grips you, an invisible tug, 
                           gentle at first but growing stronger with each step, pulling you toward the heart of the clearing. 
                           It's as if invisible threads are slowly wrapping themselves around you, dragging you forward.

                           In the centre of this twisted landscape stands a single, towering tree. Its bark is tangled with strands of thread and bones, 
                           intricately woven into horrifying designs. The bones rattle softly, a whisper in the unnatural stillness, 
                           and the threads stretch taut across the bark, pulling the tree into a grotesque and unnatural shape. You feel the pull grow stronger, 
                           and though your instincts scream to turn back, you are inexorably drawn toward the looming tree and whatever terrible secret it holds. 
                           
                           Your only way forward is “North” deeper into the forest and "South" maybe there's another path untaken...
                      """)
    clearing16 = Room("""
                           The forest is growing drastically darker with each step you take, the oppressive gloom sinking into your skin like a cold, suffocating weight. 
                           Your mind drifts, trying to recall the warmth of sunlight or the feel of a breeze on your face, but those memories are distant, fading. 
                           It feels as though it's been an eternity since your lungs tasted fresh air, and your body is starting to fail, 
                           drained by the relentless encounters with the creatures that haunt this cursed place.
 
                           Stumbling forward, you suddenly find yourself in a clearing, and your breath catches—there, amid the endless shadow, 
                           a single broad sunbeam pierces the thick canopy, casting its warm glow onto a vibrant tree in the centre. The tree is an anomaly, 
                           its thick, glimmering leaves shimmer in the sunlight, pushing back the darkness that encircles the clearing like a predator lying in wait. 
                           The air is different here, lighter, easier to breathe, and your eyes, weary from the relentless gloom, 
                           are soothed by the sight of the lush, thriving tree.

                           As you step closer, you spot a single plump, juicy “apple” hanging from one of its branches, its skin glistening like a precious jewel in the sunlight. 
                           The sight makes your mouth water; hunger gnaws at you, and the thought of biting into something so ripe, so full of life, 
                           is almost too tempting to resist. Yet, a familiar chill creeps down your spine. This forest has taught you well, nothing here is what it seems.

                           The apple dangles there, so close, the temptation almost unbearable. But you hesitate, knowing that in this place of twisted magic and lurking evil, 
                           even the most beautiful things could be laced with unspeakable danger. 

                           The only way ahead is a path that veers to the “East”.
                      """)
    clearing17 = Room("""
                           You step into the clearing, and immediately the air feels unnaturally still, as if the forest itself is holding its breath. 
                           There's a suffocating quiet all around, broken only by the faint rustling of leaves in the distance, far too soft to be comforting. 
                           Your path continues to the “east”, but the stillness of the clearing draws your gaze toward the centre, where a perfectly still, 
                           reflective pool of water lies, undisturbed and eerily pristine.

                           The surface is so smooth that it mimics a mirror, reflecting the dense canopy of trees above with unsettling clarity. 
                           But as you approach, something begins to feel wrong. The trees reflected in the pool are not the same as the ones you see overhead in the water, 
                           they are barren, their limbs twisted and jagged, stripped of life. They look tortured, like frozen silhouettes of agony, 
                           sharp angles reaching up in anguish.

                           Your heart quickens as you glance at your reflection in the water. At first, it looks like you, but something is off. 
                           The figure in the pool doesn't move in sync with your actions. When you step forward, it lags behind, its movements jerky and deliberate. 
                           Its eyes, dark and hollow pits, bore into you from the still surface, unblinking and cold. A shiver races up your spine as you notice it, the smile. 
                           It begins as a subtle twitch at the corner of its lips, then slowly grows into a twisted, malevolent grin, wide and unnatural, 
                           as if the figure takes pleasure in watching you squirm.

                           You can't look away. As you cautiously circle the pond, its movements grow more erratic, the smile twisting into something grotesque and monstrous. 
                           It watches you, its dark eyes tracking your every move, and the longer you stare, the more it seems to warp, its limbs elongating, 
                           its head tilting at unnatural angles. The reflection seems to revel in your discomfort, as if taunting you, 
                           a malevolent force trapped beneath the surface.

                           Your breath quickens, and as you take a step back, the figure lunges forward in the reflection, though the water remains still and undisturbed. 
                           The smile widens, and for a moment, it feels like the reflection is just waiting for the right moment to break free.
                      """)
    clearing18 = Room("""
                           You step into the clearing, the oppressive weight of the forest behind you feels even heavier now, as if the trees themselves are watching, 
                           waiting. The air here is colder, biting at your skin despite the lack of wind. The light that manages to seep through the canopy above is muted and sickly, 
                           casting everything in an unnatural, greenish hue. A nauseating scent of decay and rot lingers in the air, and every breath feels wrong, 
                           like you're inhaling something that doesn't belong. You see the dark path continues "north".

                           The trees surrounding the clearing twist in unnatural ways, their branches gnarled and contorted into claw-like shapes that seem to reach toward you. 
                           Their bark is blackened and cracked, oozing dark sap that drips like blood onto the ground. Some of the trunks have deep, jagged gouges in them, 
                           as though something large and clawed had taken its fury out on them. The silence is deafening, the usual sounds of the forest utterly absent, 
                           replaced by a low, almost imperceptible hum, like the very air is vibrating with dark energy.

                           In the centre of the clearing stands a massive, crooked tree, ancient and imposing, its trunk twisted and bloated with tumours of wood that pulse faintly, 
                           as though alive. Bones, animal and human alike, are woven into the roots, bleached white and cracked, some hanging from the lower branches, 
                           gently swaying though there is no breeze. Scattered at the base of the tree are crude, makeshift dolls made from sticks and cloth, 
                           their faces crudely stitched with dried sinew, each one contorted into a look of pain or fear. They seem to stare at you, almost pleading.

                           The very ground beneath your feet feels unnatural, squelching softly as you step forward. The grass is sparse and blackened, 
                           patches of grey moss clinging to the soil like festering wounds. As you move closer to the tree, you notice the faint outline of a 
                           circular symbol carved into the earth, nearly obscured by grime and rot. 
                           The longer you stand in the clearing, the heavier your limbs feel, like something is slowly draining your energy, pulling it into the earth.

                           Above, a murder of crows sits motionless in the higher branches, their beady eyes fixed on you, their presence unnerving and unnatural. 
                           Not one of them makes a sound. They simply watch, their gaze heavy with malevolent intent.

                           Every part of this place whispers that you are close. The air is thick with her presence, you can feel it seeping into your skin, 
                           burrowing into your mind. You are nearing the witch's lair, and the forest itself seems to be warning you with every twisted branch and hollow-eyed doll.
                      """)
    clearing19 = Room("""
                           You walk down the dark, overgrown path and break into a clearing. The air is heavy with a musty stillness, as if time itself has abandoned this place. 
                           The first thing that catches your eye is the outline of an old cobblestone house, its structure barely holding on as the dense and ever-hungry 
                           undergrowth of the forest slowly swallows it whole. Moss clings to the crumbling walls, and vines snake through every crack, 
                           as if the forest is greedily reclaiming what was once its own.

                           To your right, you notice an old water well, its wooden frame rotted and leaning to one side, the bucket long since decayed. 
                           The stone rim is cracked, and thick tendrils of ivy crawl up from the depths, as if something beneath is trying to escape. 
                           Nearby, rotting fence posts jut out from the earth, marking the outline of what might have been an animal enclosure. 
                           The once vibrant life that thrived here has long since faded, leaving only faint echoes of what used to be.

                           Stepping into the rubble of the house, the floor crunches beneath your feet. The roof has long since caved in, 
                           and what remains of the walls barely stands. As you carefully make your way deeper inside, you stumble upon a scene that sends a chill down your spine. 
                           In the centre of the room, a family of skeletons lies in a macabre embrace, their bones intertwined in what looks like a final act of love or despair. 
                           Thin, winding vines have threaded through their bones, twisting around them like chains, as though the forest has claimed them for its own. 
                           The sight is both eerie and tragic, and you can't help but wonder what unspeakable fate befell them here.

                           The silence in the clearing is unnerving, broken only by the faint rustle of leaves. The forest seems alive, watching, waiting. 
                           A sense of unease settles over you as you realise this place holds secrets, dark ones that linger in the shadows of this long abandoned homestead.

                           To the “north”, you notice a narrow path, barely visible through the dense underbrush. It winds away from the ruins, beckoning you onward.
                      """)
    clearing20 = Room("""
                           You break through the dense underbrush and find yourself in a clearing teeming with unnatural plants. 
                           Each one seems to have been grown with a dark purpose, thorns curl into grotesque shapes, and their leaves twist unnaturally, as if in pain. 
                           The flowers emit a foul, sickly-sweet scent that clings to the air, making it hard to breathe. Beneath your feet, the ground feels disturbingly loose, 
                           like freshly turned earth hiding secrets. Scattered among the roots and tangled undergrowth, bones both human and animal stick out, 
                           partially buried in the soil, a macabre fertiliser for this sinister garden.

                           The ground here is strangely tended to, suggesting someone or something, has been maintaining this dreadful place. 
                           This must be the witch's garden. The sickening realisation makes your skin crawl.

                           In the centre of the clearing stands a dark, grey statue, draped in a tattered black cloth that flutters faintly, though no breeze touches the air. 
                           Its eyes, hollow and made of black stone, seem to follow your every movement, watching, waiting. As you cautiously approach, you hear the soft, 
                           unsettling whispers of the flowers, hissing your name into the quiet, their voices barely audible but unmistakable. 
                           The vines along the path begin to stir, writhing like serpents, their creeping tendrils slowly reaching toward you, drawn by your presence, 
                           alive with malice.

                           You spot the path veering off to the “west”, but you know leaving this cursed garden won't be easy, the garden, it seems, doesn't want to let you go.
                           You realise you are approaching your horrible destination, the need to find the staff is dire, you don't know how much more of this you can take.
                      """)
    clearing21 = Room("""
                           Stepping into the clearing, you find it bathed in a thick, unnatural fog that clings to the ground, curling around your ankles like cold, 
                           dead fingers. The eerie stillness of the air feels suffocating, every breath heavy with the scent of damp earth and decay. 
                           In the distance, faint flickering lights catch your eye will-o'-wisps, their ghostly glow dancing just out of reach, tempting you forward. 
                           Beneath the swirling mist, a faint whispering drifts in the air, distant voices murmuring ominously, urging you to turn back.
                    
                           A sick joke, as the path you entered from has vanished, swallowed by the fog. The deeper you venture, the thicker the fog becomes, 
                           twisting your sense of direction. The towering trees around you fade into shadowy shapes, barely distinguishable from the heavy mist. 
                           It's impossible to tell if you're still in the forest or have stumbled into some otherworldly realm, where reality bends and time feels distorted.

                           Just as disorientation begins to take hold, you notice a faint glow ahead, a possible exit to the “north”, 
                           though reaching it feels like a perilous gamble.
                      """)
    clearing22 = Room("""
                           Stepping through the dense fog, the dark, winding path stretches endlessly before you, twisting unnaturally as though it's alive, 
                           bending reality itself. Your eyes strain against the shifting shadows, and for a moment, it seems as if the path stretches infinitely ahead, 
                           an illusion that makes your heart race. Blinking hard, you rub your eyes, but when your vision clears, the same winding path lies ahead, 
                           unchanged yet unsettling.

                           You emerge into a clearing, and the sight before you sends a chill down your spine. Twisted wooden totems stand in a perfect circle at the clearing's 
                           centre, each one carved with disturbingly realistic human faces. The faces are warped with expressions of sorrow, anger, and terror, 
                           their eyes hollow, yet they seem to bore into your soul. Their grimaces are frozen in eternal anguish, as though these totems have witnessed 
                           something unspeakable.

                           The ground around the totems is littered with small, crude dolls made of straw and bone, their fragile limbs tied together with frayed, 
                           rotten thread. The dolls lie scattered, but their presence feels intentional, like forgotten offerings or warnings. The air is disturbingly still, 
                           unnaturally devoid of wind, as if even nature refuses to touch this cursed place. Yet, despite the stillness, the totems creak and sway, 
                           ever so slightly, as if moved by some unseen force.

                           At the centre of the totem circle lies a stone slab, dark and stained with what appears to be dried blood, its surface rough and weathered. 
                           The metallic scent of iron lingers heavily in the air, thick and oppressive, a reminder of the violent acts committed here. 
                           You can almost hear the echo of screams in the silence, the horror of past rituals seeping into the very ground beneath your feet.

                           The longer you stand there, the stronger the feeling becomes, the dolls and totems are watching you, their twisted gazes and hollow eyes
                           tracking your every move. The clearing feels like a trap, a place where the veil between worlds is thin, and you fear the horrors that 
                           have unfolded here may not yet be over. 
                      
                           You see the paths veers toward the "east".
                      """)
    clearing23 = Room("""
                           You step into the clearing, the air immediately thick with the familiar stench of rot and decay. A sense of dread creeps over you as your eyes 
                           fall upon a group of grey stone statues, their faces twisted in expressions of utter horror and fear. Each figure is frozen in mid-motion, 
                           their arms outstretched, all pointing, some toward the path to the “north”, others toward the path to the “east”. 
                           Their contorted faces seem to plead with you, silently warning you of the peril ahead.

                           Looking closer, you can feel a dark energy emanating from the northern path. The darkness there is impenetrable, thick and oppressive, 
                           and it reeks of evil, sending a shiver down your spine. You sense that whatever lies beyond the darkness is not something you are eager to face, 
                           yet the statues pointing north seem to beckon you toward that very path, as if urging you into the unknown abyss.

                           Turning your gaze to the eastern path, you notice a stark contrast. A strange light breeze brushes against your skin, 
                           carrying a hint of something refreshing, a sensation you haven't felt in this forest for what feels like an eternity. 
                           There's also a faint glow in the distance, a warm and inviting light, unlike anything you've encountered in this cursed place. 
                           It feels unnaturally out of place, yet somehow comforting. The statues pointing east appear more relaxed, as if they, too, are drawn to the light.

                           The choice looms before you: venture into the malevolent darkness or follow the promise of light and respite. 
                         
                           But in this forest, nothing is as it seems.
                      """)
    clearing24 = Room("""
                           You step into the clearing, and a gust of fresh air fills your lungs with a renewed vigour. For the first time in what feels like an eternity, 
                           you look up and see a break in the canopy, revealing a bright blue sky and golden sunshine streaming down. It's a sight you had almost forgotten, 
                           the warmth and light of the day, after being trapped in the oppressive gloom of the forest for so long. 
                           Time has become meaningless in this cursed place, and for the first time, you remember what it feels like to be alive. 
                           You notice that the only path is “west” the way you came.

                           Before you stands a singular cherry blossom tree, its branches adorned with blossoms of the purest light pink, their beauty almost ethereal. 
                           The ground is blanketed with fallen petals, which swirl and dance in the soft breeze, gracefully moving as though in celebration of your arrival. 
                           The tree, glowing with an inner radiance, seems to be pushing back the darkness, creating a haven of light and life amidst the surrounding decay. 
                           It's as if this tree is the heart of some ancient magic, holding the horrors of the forest at bay.

                           You can feel it, a profound sense of peace that soothes your weary soul, a momentary respite from the fear and exhaustion that has followed 
                           you throughout this journey. There is a powerful magic here, one that feels benevolent and pure.

                           As you step closer to the tree, the ground begins to tremble beneath your feet. You pause, watching in awe as the cherry blossom tree begins to part, 
                           its trunk gently splitting down the middle as though welcoming you. There is no violence in the movement, only grace and reverence. 
                           Inside, nestled within the tree's glowing heart, is a "staff", shimmering with a silvery light that pulses with energy.
                      """)
    clearing25 = Room("""
                           
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
    clearing7.set_exits({'south': 'clearing6', 'west': 'clearing8', 'north': 'clearing9'})
    clearing8.set_exits({'north': 'clearing10', 'east': 'clearing7'})
    clearing9.set_exits({'north': 'clearing11', 'west': 'clearing10', 'south': 'clearing7'})
    clearing10.set_exits({'south': 'clearing8', 'east': 'clearing9'})
    clearing11.set_exits({'north': 'clearing12', 'south': 'clearing9'})
    clearing12.set_exits({'south': 'clearing11', 'west': 'clearing13', 'east': 'clearing14', 'north': '15'})
    clearing13.set_exits({'north': 'clearing16'})
    clearing14.set_exits({'north': 'clearing17'})
    clearing15.set_exits({'north': 'clearing18', 'south': 'clearing12'})
    clearing16.set_exits({'east': 'clearing15'})
    clearing17.set_exits({'west': 'clearing15'})
    clearing18.set_exits({'south': 'clearing15', 'north': 'clearing19'})
    clearing19.set_exits({'south': 'clearing18', 'north': 'clearing20'})
    clearing20.set_exits({'west': 'clearing21'})
    clearing21.set_exits({'north': 'clearing22'})
    clearing22.set_exits({'east': 'clearing23'})
    clearing23.set_exits({'north': 'clearing25', 'east': 'clearing24'})
    clearing24.set_exits({'west': 'clearing23'})



    # Items placed in rooms
    forest_entrance.set_items(['stick'])
    clearing1.set_items(['letter'])
    clearing2.set_items(['sword'])
    clearing3.set_items(['helm'])
    clearing4.set_items(['potion'])
    clearing5.set_items(['blue bottle', 'green bottle'])
    clearing6.set_items(['hat'])
    clearing12.set_items(['robe'])
    clearing13.set_items(['white', 'golden'])
    clearing16.set_items(['apple'])
    clearing24.set_items(['staff'])

    
    
    # Enemies in rooms(clearings)
    clearing3.set_enemy(Enemy("The Great Forest Spider", 54))
    clearing4.set_enemy(Enemy("The Fire atronach", 65))
    clearing7.set_enemy(Enemy("Borzug the Dark Orc", 62))
    clearing10.set_enemy(Enemy("The Bonecrawler", 35))
    clearing12.set_enemy(Enemy("The Scarecrow", 37))
    clearing14.set_enemy(Enemy("The Shadow-man", 25))
    clearing15.set_enemy(Enemy("The Thread-man", 13))
    clearing17.set_enemy(Enemy("The Water-Shadow", 12))
    clearing20.set_enemy(Enemy("A Living Vine", 5))
    clearing22.set_enemy(Enemy("The Small Doll Horde", 10))

    

    

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
        'clearing7': clearing7,
        'clearing8': clearing8,
        'clearing9': clearing9,
        'clearing10': clearing10,
        'clearing11': clearing11,
        'clearing12': clearing12,
        'clearing13': clearing13,
        'clearing14': clearing14,
        'clearing15': clearing15,
        'clearing16': clearing16,
        'clearing17': clearing17,
        'clearing18': clearing18,
        'clearing19': clearing19,
        'clearing20': clearing20,
        'clearing21': clearing21,
        'clearing22': clearing22,
        'clearing23': clearing23,
        'clearing24': clearing24,
        'clearing25': clearing25,
    }

    return forest_map

def combat_loop(player, enemy):
    #Handles combat between player and enemy.
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
