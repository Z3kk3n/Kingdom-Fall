from logging import PlaceHolder
from opcode import HAVE_ARGUMENT
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

consumableact={'Hp Potion':'hp_consumable',
'Attack Potion':'atk_consumable',
'Defense Potion':'defn_consumable',
'Speed Potion':'spd_consumable'}

#Fight Actions
def slash_attack(player,oplayer) -> None:
    print('You strike with your blade.')
    oplayer.HP = oplayer.HP - 7
    player.stam -= Class_Character.slash.stam_use
    print('Player Stamina - 15')
    print('Opposing player HP - 7\n')

def arrow_attack(player,oplayer) -> None:
    print('You draw back and release a perfect shot.')
    oplayer.HP = oplayer.HP - 7
    player.stam -= Class_Character.slash.stam_use
    print('Player Stamina - 15')
    print('Opposing player HP - 7\n')

def fireball_attack(player,oplayer) -> None:
    print('You attack with a fiery passion.')
    oplayer.HP = oplayer.HP - 7
    player.stam -= Class_Character.slash.stam_use
    print('Player Stamina - 15')
    print('Opposing player HP - 7\n')

#Warrior Attack Functions
def sword_tackle_attack(player,oplayer) -> None:
    dmg = Class_Character.sword_tackle.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.sword_tackle.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.sword_tackle.stam_use}\n')
    player.one_cooldown(2)

def fire_slash_attack(player,oplayer) -> None:
    dmg = Class_Character.fire_slash.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.fire_slash.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.sword_tackle.stam_use}\n')
    player.two_cooldown(3)

def shield_bash_attack(player,oplayer) -> None:
    dmg = Class_Character.shield_bash.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.shield_bash.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.shield_bash.stam_use}\n')
    player.three_cooldown(3)
    player.deflect(1)

#Paladin Attack Functions
def tornado_slash_attack(player,oplayer) -> None:
    dmg = Class_Character.tornado_slash.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.tornado_slash.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.tornado_slash.stam_use}\n')

#Consumable Actions
def hp_consumable(player):
    print('You feel the liquid trikle down your throat.')

    health = player.b_HP - player.HP
    health = health/2
    player.HP = player.HP + health

    print(f'HP + {health}\n')

def atk_consumable(player):
    print('You feel the power trikle down your thoat.')
    player.methattack(2)
    print('Attack + 5\n')

def defn_consumable(player):
    print('You feel a liquid like iron trikle down your thoat.')
    player.methdefense(2)
    print('Defense + 2\n')

def spd_consumable(player):
    print('You drink the liquid lightning quick.')
    player.methspeed(2)
    print('Speed x 2\n')

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
    while True:
        selected_atk=None
        for index,attack in enumerate(player.atk_useable):
            print(f'{attack.text_color}[{index+1}] {attack.name}')

        selectionA=input('\033[0m>')
        if selectionA=='Close' or selectionA=='close':
            return
        try:
            selectionA = int(selectionA)-1
            for index,attack in enumerate(player.atk_useable):
                if index == selectionA:
                    selected_atk= player.atk_useable[attack]
        except ValueError:
            selectionA=string.capwords(selectionA)
            if selectionA in player.atk_useableS:
                selected_atk= player.atk_useableS[selectionA]

        if selected_atk not in player.atk_useable:
            pass
        else:
            if selected_atk.on_cooldown:
                print("You are still tired out from this attack. You're on cooldown.")
            elif selected_atk.on_cooldown==False:
                return selected_atk
            else:
                return

def Stat(player,oplayer) -> None:
    print(f'HP: {player.HP}')

    print(f'Attack: {player.atk}')

    print(f'Defense: {player.defn}')

    print(f'Speed: {player.spd}')

    print(f'Stamina: {player.stam}')

    print(f'Opponent HP: {oplayer.HP}')
    input('Press ENTER to continue.')