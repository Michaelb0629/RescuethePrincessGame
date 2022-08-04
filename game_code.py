from multiprocessing.connection import wait
from tkinter import N
from tkinter.messagebox import NO, YES, YESNO
from unicodedata import name


def welcome():
    print("Welcome, are you ready to Rescue the Princess?")
    print('Yes or No')
    if input() == "yes":
        print("\nLet's Rescue the Princess\n")
    
    else:
        print("\nHurry, the Princess needs you!\n")
        return welcome()
         

welcome()



def describing_game():
    print(
        "Once you arrive to the dragons's lair, you will need to find a sword and a shield in order to fight the dragon.\n"
         "If you do not find these items, you will not be able to fight the dragon!/n"
         "Be careful some choices will cost strength to execute them." 
         "You may wish to save as much strength as possible to fight the dragon!\n"
    )

print("What is your name brave traveler?")
name = input()

print('\nVery well {name}, Let\'s begin our quest!\n'.format(name=name))

describing_game()

def arriving_at_lair():
    your_strength = 100 
    print("\n{name}, you've arrived at the dragon's lair!\n ".format(name=name))
    print("It's a dark and dreary castle, sitting at the edge of a cliff. In the distance you hear the faint roar of the dragon.\n"
    "As you approach, you see a barred door, could this be the entrance?\n"
    "\nIt looks like I can break down the door.\n"
    "\nDo you want to break down the door? This will cost 10 strength")
    if input() == 'yes':
        your_strength -= 10
        print("\nYou've broken down the door and gained entry to the castle!\n")
        print("\nYour Strength is: "+ str(your_strength))
    else:
        print(
            "\nYou walk around and find a skeleton with a key hanging from its neck. That might unlock the door!\n"
            "\nYou return to the door with the key. It opens!\n"
            )
    
print('Do you want to read your journal entries about your journey to the castle?')
if input() == 'yes':
    print(
    '\n02/16/1207: The mighty king summoned me to rescue his daughter from the evil dragon "Hrothgar".\n'
    '02/17/1207: I ready my things and tell my family I love them, for I might not come back. Let\'s hope thats not the case...'
    '02/18/1207: I have a journey of a two fortnights through dangerous creatures and deadly enemies. I better get some rest, for tomorrow I set off on my journey!\n'
    '02/23/1207: I have finally traversed the famous Mountain of Uzul.\n' 
    '02/27/1207: I have defeated the Giant of Melkath.\n'
    '03/01/1207: I can\'t seem to shake this feeling of someone watching me.\n'
    '03/03/1207: I woke up and as I was leaving last nights camp, I discovered a make shift cot only 10 yards from me. That\'s must\'ve been following me.\n'
    '03/05/1207: I have arrived at "Hrothgar\'s" lair! I will pitch camp and tackle the dragon tomorrow!\n'
    )
    arriving_at_lair()
    
else:
    arriving_at_lair()




def barracks():
    print(
        'You walk into the barracks to find empty racks that once held swords.\n'
        'As you turn around you catch a glimmer of something poking out behind a chest. As you get closer you realize it\'s a sword!\n'
        '\nIt must be my lucky day, someone must\'ve stashed this thinking they were coming back. Well finders keepers!'
        '\nDo you want to search the Blacksmith\'s shop?'
        )
    if input() == 'yes':
        blacksmiths_shop()


def blacksmiths_shop():
    print(
        'You walk in to find some broken weapons and bent shields strewn about the floor, looks like something bad happened here.\n'
    'You search the room to see if you can find anything of use, underneath some broken tables you find a perfectly usuable shield!\n'
    '\nDo you want to go back and search the barracks?\n'
    'Yes or No\n'
    )
    if input() == 'yes':
        barracks()

def inside_the_castle():
    print(
        '\nYou walk in and you see a stairs to the left and stairs to right. The left stairs seem to go up, and the right stairs seem to go down.\n'
        'Which stairs do you want to take: Left or Right?\n'
        )
    if input() == 'left':
        print('\nYou walk up the stairs and enter into small torch lit area of an long dark hallway.\n'
        'You grab the torch and head towards what seems to be a foyer.\n'
        'In the foyer you find a set of doors, one leads to the Black smith shop, the other leads to the barracks.\n'
        'Which way do you want to go? To the "Blacksmith\'s shop" or to the "Barracks"?\n')
        if input() == 'blacksmith\'s shop':
            blacksmiths_shop()

        else:
            barracks()

inside_the_castle()


            
            # )
       
            
            
        
            #     else:
            #         print('\nYou go down the stairs and enter through a door to find the kitchen.\n'
            #         'In there, you come across two doors, one looks like it might lead to the Dining Room, the other leads to the Great Hall.\n'
            #         'Where do you want to go? The Dining Room or the Great hall?\n'
            #     )
            #     if input() == 'Dining Room':
            #     print(
            #         '\n You walk into the dining room to find what looks like the a shield with some sort of crest on it.'
            #         'You take the shield as this will definitely help you later.'
            #         '\nYou have found the shield!\n'
            #         )
            


