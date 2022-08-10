from logging import PlaceHolder
import string
import Class_Character

#Holds most dictionaries and functions.

#Notes for me:
    #Remember to use .name when eval from class so as to not return the object but the name string.
    #Think about game disign of speed stat and items.
    #Inv() and fight functions need help.


#Dictionaries
action={'Fight':'Fight_Opp','fight':'Fight_Opp','1':'Fight_Opp',
'Bag':'Inv','bag':'Inv','2':'Inv',
'Status':'Stat','status':'Stat','3':'Stat'}

f_action={'Slash':'slash_attack',
'Arrow':'arrow_attack',
'Fireball':'fireball_attack',
'Sword Tackle':'sword_tackle_attack',
'Fire Slash':'fire_slash_attack',
'Shield Bash':'shield_bash_attack'}

consumableact={'Hp Potion':'hp_consumable'}

#Fight Actions
def slash_attack(player,oplayer) -> None:
    print('You strike with your blade.')
    oplayer.HP = oplayer.HP - 7
    player.stam -= Class_Character.slash.stam_use
    print('Player Stamina - 10')
    print('Opposing player HP - 7\n')

def arrow_attack(player,oplayer) -> None:
    print('You draw back and release a perfect shot.')
    oplayer.HP = oplayer.HP - 7
    player.stam -= Class_Character.slash.stam_use
    print('Player Stamina - 10')
    print('Opposing player HP - 7\n')

def fireball_attack(player,oplayer) -> None:
    print('You attack with a fiery passion.')
    oplayer.HP = oplayer.HP - 7
    player.stam -= Class_Character.slash.stam_use
    print('Player Stamina - 15')
    print('Opposing player HP - 7\n')
    oplayer.burn(4)

#Warrior Attack Functions
def sword_tackle_attack(player,oplayer) -> None:
    dmg = Class_Character.sword_tackle.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.sword_tackle.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.sword_tackle.stam_use}\n')

def fire_slash_attack(player,oplayer) -> None:
    dmg = Class_Character.fire_slash.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.fire_slash.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.sword_tackle.stam_use}\n')

def shield_bash_attack(player,oplayer) -> None:
    dmg = Class_Character.shield_bash.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.shield_bash.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.shield_bash.stam_use}\n')
    player.deflect(1)

#Consumable Actions
def hp_consumable(player):
    print('You feel the liquid trikle down your throat.')

    health = player.b_HP - player.HP
    health = health/2
    player.HP = player.HP + health

    print(f'HP + {health}\n')


#Main Actions
def Inv(player,oplayer) -> None:
    print("Chose an item or type 'Close'.")

    selected_item=None
    for index,item in enumerate(player.consumable):
        print(f'[{index+1}] {item}')

    selection=input('>')
    if selection=='Close' or selection=='close':
        return
    try:
        selection = int(selection)-1
        for index,item in enumerate(player.consumable):
            if index == selection:
                selected_item= player.consumable[item]
                return selected_item
    except ValueError:
        selection=string.capwords(selection)
        if selection in player.consumable:
            selected_item= player.consumable[selection]
            return selected_item

def Fight_Opp(player,oplayer) -> None:
    print("Chose an attack or type 'Close'.")

    selected_atk=None
    for index,attack in enumerate(player.atk_useable):
        print(f'[{index+1}] {attack}')

    selectionA=input('>')
    if selectionA=='Close' or selectionA=='close':
        return
    try:
        selectionA = int(selectionA)-1
        for index,attack in enumerate(player.atk_useable):
            if index == selectionA:
                selected_atk= player.atk_useable[attack]
                return selected_atk
    except ValueError:
        selectionA=string.capwords(selectionA)
        if selectionA in player.atk_useable:
            selected_atk= player.atk_useable[selectionA]
            return selected_atk

#Need to make curent and opposing players first then this will work.

def Stat(player,oplayer) -> None:
    print(f'HP: {player.HP}')

    print(f'Attack: {player.atk}')

    print(f'Defense: {player.defn}')

    print(f'Speed: {player.spd}')

    print(f'Stamina: {player.stam}')

    print(f'Opponent HP: {oplayer.HP}')
    input('Press ENTER to continue.')