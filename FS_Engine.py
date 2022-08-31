from logging import PlaceHolder
from math import ceil
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
'Shield Bash':'shield_bash_attack',
'Tornado Slash':'tornado_slash_attack',
'Fissure':'fissure_attack',
'Heal':'heal_attack',
'Vampirism':'vampirism_attack',
'Silent Takedown':'silent_takedown_attack',
'Ryuu':'ryuu_attack',
'Skewer':'skewer_attack',
'Horse Trample':'horse_trample_attack',
'Heavy Cavalry':'heavy_cavalry_attack',
'Firework':'firework_attack',
'Deliberate Miss':'deliberate_miss_attack',
'Hwacha':'hwacha_attack',
'Frost Heal':'frost_heal_attack',
'Ground Lance':'ground_lance_attack',
'Explosion':'explosion_attack'}

consumableact={'Hp Potion 1':'hp_consumable',
'Hp Potion 2':'hp_consumable',
'Hp Potion 3':'hp_consumable',
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
    player.four_cooldown(3)
    oplayer.r_dmg_seven(2)

def fissure_attack(player,oplayer) -> None:
    dmg = Class_Character.fissure.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.fissure.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.fissure.stam_use}\n')
    player.five_cooldown(4)
    oplayer.paladin_slow(1)

def heal_attack(player,oplayer) -> None:
    healhp = Class_Character.heal.base_dmg
    round(healhp)
    player.HP += healhp
    player.HP = min(player.HP,player.b_HP)
    player.stam -= Class_Character.heal.stam_use
    print(f'You heal {healhp} HP.')
    print(f'Stamina - {Class_Character.fissure.stam_use}\n')
    player.six_cooldown(4)

#Assassin Attacks
def vampirism_attack(player,oplayer) -> None:
    dmg = Class_Character.vampirism.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    healhp = dmg / 2
    oplayer.HP -= dmg
    player.HP = min(player.HP,player.b_HP)
    player.HP += healhp
    player.stam -= Class_Character.vampirism.stam_use
    print(f'You deal {dmg} damage. Vampirism HP + {healhp}')
    print(f'Stamina - {Class_Character.vampirism.stam_use}\n')
    player.seven_cooldown(3)
    oplayer.r_dmg_three(2)

def silent_takedown_attack(player,oplayer) -> None:
    dmg = Class_Character.silent_takedown.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.silent_takedown.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.silent_takedown.stam_use}\n')
    player.eight_cooldown(4)
    oplayer.r_dmg_three(2)

def ryuu_attack(player,oplayer) -> None:
    dmg = Class_Character.ryuu.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.ryuu.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.ryuu.stam_use}\n')
    player.nine_cooldown(5)
    oplayer.r_dmg_three(2)

#Knight Attacks
def skewer_attack(player,oplayer) -> None:
    dmg = Class_Character.skewer.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.skewer.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.skewer.stam_use}\n')
    player.knight_cooldown(2)
    oplayer.paladin_slow(1)

def horse_trample_attack(player,oplayer) -> None:
    dmg = Class_Character.horse_trample.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.horse_trample.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.horse_trample.stam_use}\n')
    player.knight_cooldown(2)
    oplayer.deflect(1)

def heavy_cavalry_attack(player,oplayer) -> None:
    dmg = Class_Character.heavy_cavalry.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.heavy_cavalry.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.heavy_cavalry.stam_use}\n')
    player.knight_cooldown(2)

#Archer Attacks
def firework_attack(player,oplayer) -> None:
    dmg = Class_Character.firework.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.firework.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.firework.stam_use}\n')
    player.ten_cooldown(3)

def deliberate_miss_attack(player,oplayer) -> None:
    dmg = Class_Character.deliberate_miss.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.deliberate_miss.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.deliberate_miss.stam_use}\n')
    player.eleven_cooldown(4)
    oplayer.paladin_slow(2)
    oplayer.deflect(1)

def hwacha_attack(player,oplayer) -> None:
    dmg = Class_Character.hwacha.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.hwacha.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.hwacha.stam_use}\n')
    player.twelve_cooldown(5)

#Mage Attacks
def frost_heal_attack(player,oplayer) -> None:
    dmg = Class_Character.frost_heal.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    healhp = dmg / 2
    player.HP += healhp
    player.HP = min(player.HP,player.b_HP)
    oplayer.HP -= dmg
    player.stam -= Class_Character.frost_heal.stam_use
    print(f'You deal {dmg} damage and heal {healhp}.')
    print(f'Stamina - {Class_Character.frost_heal.stam_use}\n')
    player.thirteen_cooldown(2)

def ground_lance_attack(player,oplayer) -> None:
    dmg = Class_Character.ground_lance.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.ground_lance.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.ground_lance.stam_use}\n')
    player.fourteen_cooldown(2)
    oplayer.paladin_slow(1)

def explosion_attack(player,oplayer) -> None:
    dmg = Class_Character.explosion.base_dmg * player.atk / oplayer.defn / 4
    round(dmg)
    oplayer.HP -= dmg
    player.stam -= Class_Character.explosion.stam_use
    print(f'You deal {dmg} damage.')
    print(f'Stamina - {Class_Character.explosion.stam_use}\n')
    player.fifteen_cooldown(5)
    oplayer.r_dmg_three(3)

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
    print("Chose an item. Type 'Close' to exit or 'None' to cancel your choice.")
    while True:
        selected_item=None
        for index,item in enumerate(player.consumable):
            print(f'[{index+1}] {item.name} -- {item.desc}')

        selection=input('>')
        if selection=='Close' or selection=='close':
            return
        elif selection=='None' or selection=='none':
            player.selected_item=None
            return
        try:
            selection = int(selection)-1
            for index,item in enumerate(player.consumable):
                if index == selection:
                    selected_item= player.consumable[item]
        except ValueError:
            selection=string.capwords(selection)
            if selection in player.consumableS:
                selected_item= player.consumableS[selection]

        if selected_item not in player.consumable:
            pass
        else:
            return selected_item

def Fight_Opp(player,oplayer) -> None:
    print("Chose an attack. Type 'Close' to exit or 'None' to cancel your choise.")
    while True:
        selected_atk=None
        for index,attack in enumerate(player.atk_useable):
            print(f'{attack.text_color}[{index+1}] {attack.name} -- {attack.desc}')

        selectionA=input('\033[0m>')
        if selectionA=='Close' or selectionA=='close':
            return
        elif selectionA=='None' or selectionA=='none':
            player.selected_atk=None
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
        elif selected_atk.stam_use>=player.stam:
            print('You do not have enough stamina for that move.')
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
