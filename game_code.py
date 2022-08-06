print("\nWelcome, What is your name brave traveler?\n")
name = input()

# Introduction to the game: the player will enter their name and will be described the objectives of the game.
def welcome():
    print("\nAre you ready to Rescue the Princess?")
    print('Yes or No?\n')
    
    if input() == 'yes':
        print("\nLet's Rescue the Princess\n")
        describing_game()
    else:
        print("\nHurry, the Princess needs you!\n")
        return welcome()
         


# displaying the objectives of the game to the player. 


def describing_game():
    print(
        "\nOnce you arrive to the dragons's lair, you will need to find a sword and a shield in order to fight the dragon.\n"
         "If you do not find these items, you will not be able to fight the dragon!\n"
         "Some actions will cost strength to do. Be careful to save as much strength as possible to fight the dragon!"
         "You must defeat the dragon in order to save the Princess! Good Luck!"
    )

your_strength = 100
# Creating the scene for the player when they arrive to the castle after the 'intro' to the game

def arriving_at_lair():
    print("\n{name}, you've arrived at the dragon's lair!\n ".format(name=name))
    print("It's a dark and dreary castle, sitting at the edge of a cliff. In the distance you hear the faint roar of the dragon.\n"
    "As you approach, you see a barred door, could this be the entrance?\n"
    "\nIt looks like I can break down the door.\n"
    "\nDo you want to break down the door? This will cost '10' strength.\n"
    " Yes or No?")
    if input() == 'yes':
        global your_strength 
        your_strength -= 10
        print('\n{name}, you have broken down the door and gained entry to the castle!\n'.format(name=name))
        print('You now have ' + str(your_strength) + ' strength.')
                    
    else:
        print(
            "\nYou walk around and find a skeleton with a key hanging from its neck. That might unlock the door!\n"
            "\nYou return to the door with the key. It opens!\n"
            )
    

    
# This is while the player is inside the castle and will provid there path through to finding_the_dragon()
# Had to order this way for how the functions for how the different scenes are called.

player = []

def barracks():
    if 'shield' in player:
        print(
        '\nYou walk into the barracks to find empty racks that once held swords.\n'
        'As you turn around you catch a glimmer of something poking out behind a chest. As you get closer you realize it\'s a sword!\n'
        '\nIt must be my lucky day, someone must\'ve stashed this thinking they were coming back. Well finders keepers!\n'
        )
        print( 
        '\n{name} has found the sword!\n'.format(name=name)
        )
        player.append('sword')
        
        finding_the_dragon()
    
    elif 'shield' not in player:
        print(
             '\nYou walk into the barracks to find empty racks that once held swords.\n'
        'As you turn around you catch a glimmer of something poking out behind a chest. As you get closer you realize it\'s a sword!\n'
        '\nIt must be my lucky day, someone must\'ve stashed this thinking they were coming back. Well finders keepers!\n'
        )
        print( 
        '\n{name} has found the sword!\n'.format(name=name)
        )
        player.append('sword')
        print(
            '"\nNow that I\'ve found a sword all that\'s left is to find the shield" {name} thinks. Maybe the Blacksmith\'s shop might have something.'.format(name=name)
            )
        print(
            'Do you want to go back to the Blacksmith\'s shop?'
        )
        if input() == 'yes':
            blacksmiths_shop()
        else:
            print(
            '\nAs you search the barracks, you start losing hope of finding anything useful. You give up your efforts and cirlcle back to the Blacksmith\'s shop.\n'
            'As you enter the Blacksmith\s shop, You walk in to find some broken weapons and bent shields strewn about the floor, looks like something bad happened here.\n'
            'You search the room to see if you can find anything of use, underneath some broken tables you find a perfectly usuable shield!\n'
            '\n{name} has found the shield!\n'.format(name=name)
            )
        
            player.append('shield')
    
            finding_the_dragon()
        
        


def blacksmiths_shop():
    if 'sword' not in player:
        print(
        'As you enter the Blacksmith\s shop, You walk in to find some broken weapons and bent shields strewn about the floor, looks like something bad happened here.\n'
        'You search the room to see if you can find anything of use, underneath some broken tables you find a perfectly usuable shield!\n'
        '\n{name} has found the shield!\n'.format(name=name)
        )
    
        player.append('shield')
    
        print(
        '\nDo you want to go back and search the barracks?\n'
        'Yes or No\n'
        )
    
        if input() == 'yes':
            barracks()

        else:
            print(
            'You continue to search the Blacksmith\'s shop. After turning up nothing of use you exit the Blacksmit\'s shop and enter the Barracks.'
            )
        barracks()


def inside_the_castle():
    print(
        '\nYou walk in and you see stairs to your left and right. The left set of stairs go up, and the right set of stairs go down.\n'
        'Which stairs do you want to take: Left or Right?\n'
        )
    if input() == 'left':
        print(
            '\nYou walk up the stairs and enter into small torch lit area of an long dark hallway.\n'
        'You grab the torch and head towards what seems to be a foyer.\n'
        '\nIn the foyer you find a set of doors, one leads to the Black smith shop, the other leads to the barracks.\n'
        'Which way do you want to go? To the "Blacksmith\'s shop" or to the "Barracks"?\n'
        )
        if input() == 'blacksmith\'s shop':
            blacksmiths_shop()

        else:
             barracks()
    else:
        print(
        '\nYou go down the stairs and enter through a door to find the dungeon.\n'
        'Other than some old skeletons in the cells, there\'s nothing down here.\n'
        '\nYou walk back up the stairs and continue up the stairs to the left. You enter into small torch lit area of an long dark hallway.\n'
        'You grab the torch and head towards what seems to be a foyer.\n'
        '\nIn the foyer you find a set of doors, one leads to the Blacksmith\'s shop, the other leads to the barracks.\n'
        'Which way do you want to go?\n "Blacksmith\'s shop" or to the "Barracks"?\n'
        )

        if input() == 'blacksmith\'s shop':
            blacksmiths_shop()
            
        else:
            barracks()
    
    
    
            


            
            
            
    
        

#had to put before finding dragon because im calling this about_to_fight_the_dragon() in finding_the_dragon()
def exploring_the_caves():
    print(
        '"Maybe I should see if there\'s anything around here that could help me" {name} thinks.'.format(name=name)
    )
    print(
        ''
    )
def about_to_fight_the_dragon():
    print(
        '\nYou enter through the giant door, it creaking eerily as you open it, it shuts with a echoed thud.\n'
        'As you turn around you are struck with the sight of an expansive cave with a staircase along the walls of it, the stairs crumbling in some spots.\n'
        'You start to descend the stairs and come upon a gap, it looks like I can jump this!\n'
        '\nDo you want to jump the gap? This will cost \'3\' strength.\n'
        'Yes or No?\n'
        )
    if input() == 'yes':
        print(
            '\n{name} jumped the gap!'.format(name=name)
        )
        global your_strength 
        your_strength -= 3
        print(
            'You now have: ' + str(your_strength) + ' strength'
        )
        
    else:
        print(
            'There\'s no other way around, it looks like I\'m going to have to jump it anyway...'
        )
        print( 
            '\n{name} has jumped across the gap!'
        )
        your_strength -= 3
        print(
            '\nYou now have ' + str(your_strength) + ' strength.'
        )
        
    print(
        '\nAs {name} continues down the stairs, they hear what sounds like the dragon coming!\n'. format(name=name)
        )
    print(
        '\nYou run down the rest of the stairs as quickly as you can, your armour rattling with every step.\n'
        'You jump behind some broken stones and pieces of the crumbling stairs to hide. Just as you\'re crouching behind the large piece of stairs\n'
        ' the dragon peaks his in to check what those sounds were. You hold your breath, fearing if you even breath, it will alert him.\n'
        )
    print(
        '"Is this my oppurtunity to supprise attack?" {name} wonders.\n'.format(name=name)
        )
    print(    
        '\n Do you want to attack now? This will cost \'15\' strength.\n'
        'Yes or No\n'
        )
    if input() == 'yes':
        your_strength -= 15
        
        print(
            '\nYou slowly draw your sword, You jump out and charge "Hrothgar" giving him your most terrifying war cry.\n'
            'You raise your sword in anticipation of attack, Your so close to being able to stab him thrugh his eye.\n'
            'When at the last moment Hrothgar swings his out of the way and centers you in his vision. "I got a bad feeling about this" {name} thinks.'.format(name=name))
        print(
            '\nAs Hrothgar is slowly raising his posture, you are paralyzed with fear, his stature much more intimidating than you thought it would be.\n'
            'He opens his gaping jaws and breaths an inferno towards you, burning you to ash.\n'
            'May the next brave traveler have better luck than {name}.'.format(name=name))
        print(
            '\nWould you like to try again?\n Yes or No?\n'
        )
        if input() == 'yes':
            arriving_at_lair()

        else:
            print(
                '\nThanks for playing {name}! Better luck next time!\n'.format(name=name)
            )
            welcome()
    
    else:
        print(
            '\nYou remain hidden behind the large piece of fallen stairs with your sword drawn just in case.\n'
            'Holding your breath, you hear the sniffing of Hrothgar right around the corner, your heart starts pounding.\n'
            'When all of a sudden, something startles him from some other part of the castle, he quickly leaves to investigate.\n'
            'You are able to relax and sheath your sword\n'
            '\nAfter Hrothgar leaves, you enter through the doorway he was in. It opens up to a massive passage way of sorts, with doorways along both sides\n'
            'You look down and see the footprints of the dragon, much more larger than you anticipated. "This could be a challenge!" {name} thinks.\n'.format(name=name)
            )
        print(
            '\nDo you want to follow the footprints?'
            'Yes or No?'
        )
        if input() == 'yes':
            fighting_the_dragon()


        else:
            exploring_the_caves()



# Now trying to find the dragon after finding the weapon and shield in the blacksmiths shop and barracks



def finding_the_dragon():
    print(
        '\n"Now that I\'ve found the sword and shield, I\'m ready to take on the dragon!"\n'
        '"But first, I got to find it, can\'t be that hard, ... Can it?"\n'
        '\nAs {name} is walking around exploring the Great Hall, they uncover a key!\n'.format(name=name))
    print(
        'Do you want to keep this key?\n Yes or No?'
        )
    if input() == 'yes':
            print('\n{name} has found the key to the "Caves of Hrothgar".\n'.format(name=name))
            print(
            '\nAs they\'re coming close to the end of the Great Hall, {name} finds a door spanning the height of the Great Hall.\n'.format(name=name))
            print('"A dragon could definitely fit through there" {name} thinks.'.format(name=name))
            print('But wait its locked, I wonder if that key would unlock this. It worked! '
            )
            about_to_fight_the_dragon()
    else:
        print(
            '{name} has put the key back.'.format(name=name)
            )
        print(
            '\nAs they come to the ending of the Great Hall, {name} comes across a giant door spanning the height of the walls.\n'.format(name=name)
            )
        print(
            '\nIt appears to be locked. But you remember the key you found earlier, that might work with this door!\n'
            'Do you want to go back and grab the key?\n Yes or No'
            )
        if input() == 'yes':
            print(
                '\nYou go back to grab the key.\n'
                )
            print(
                '\n{name} has found the key to the "Caves of Hrothgar".\n'.format(name=name)
                )
            print(
                '\nYou try unlocking the door, It worked!\n'
                )
            about_to_fight_the_dragon()
        else:
            print('\nYou need a key to unlock this door! Let\'s start that over...\n')
            finding_the_dragon()



# OKAY LETS PLAY THE GAME! CALLING THE FUNCTIONS 




print('\nVery well {name}, Let\'s begin our quest!\n'.format(name=name))

welcome()


print('\nDo you want to read your journal entries about your journey to the castle?\n "Yes or No".')
if input() == 'yes':
        print(
    '\n02/16/1207: The mighty king summoned me to rescue his daughter from the evil dragon "Hrothgar".\n'
    '\n02/17/1207: I ready my things and tell my family I love them, for I might not come back. Let\'s hope thats not the case...\n'
    '\n02/18/1207: I have a journey of a two fortnights through dangerous creatures and deadly enemies. I better get some rest, for tomorrow I set off on my journey!\n'
    '\n02/23/1207: I have finally traversed the famous Mountain of Uzul.\n' 
    '\n02/27/1207: I have defeated the Giant of Melkath.\n'
    '\n03/01/1207: I can\'t seem to shake this feeling of someone watching me.\n'
    '\n03/03/1207: I woke up and as I was leaving last nights camp, I discovered a make shift cot only 10 yards from me. That\'s must\'ve been following me.\n'
    '\n03/05/1207: I stopped just a day\'s ride from "Hrothgar\'s" lair! I will pitch camp and tackle the dragon tomorrow!\n'
    )
        arriving_at_lair()
else:
    arriving_at_lair()

inside_the_castle()

finding_the_dragon()

about_to_fight_the_dragon()



