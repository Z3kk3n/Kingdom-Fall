# if __name__=='main':
import random

class fighter:
    def __init__(self,name,description,base_hp,hit_points,base_attack,attack,base_defense,defense,speed,max_stamina,stamina,) -> None:
        self.name=name
        self.desc=description
        self.b_HP=base_hp
        self.HP=hit_points
        self.b_atk=base_attack
        self.atk=attack
        self.b_defn=base_defense
        self.defn=defense
        self.spd=speed
        self.max_stam=max_stamina
        self.stam=stamina
        self.initiative=False
    #Attacks and Items
        self.atk_useable={}
        self.selected_atk=None
        self.consumable={'Hp Potion':inv_item('Hp Potion','Heals charater for half of missing HP.'),
                        'Attack Potion':inv_item('Attack Potion','Increases player attack for one turn.'),
                        'Defense Potion':inv_item('Defense Potion','Increases player defense for one turn.'),
                        'Speed Potion':inv_item('Speed Potion','Increases player speed for one turn.')}
        self.selected_item=None
    #Booleans and Turns for statis conditions
        #Bad:
        self.burning=False
        self.turn_of_burn=0
        #Good:
        self.deflecting=False
        self.turn_of_deflect=0

    #Consumables
        self.attacky=False
        self.defensey=False
        self.speedy=False
        self.attacky_turns=0
        self.defensey_turns=0
        self.speedy_turns=0

    #Cooldowns
        # self.ST_on_cooldown=False
        # self.CD_ST_turns=0

    #Method of checking for statis conditions
    def update(self):
        #Bad:
        if self.burning:
            self.burn()
        #Good:
        if self.deflect:
            self.deflect()
    #Methods of activating statis conditions
    def burn(self,turn_of_burn=False):
        if turn_of_burn:
            self.turn_of_burn=turn_of_burn
            self.burning=True
        else:
            self.HP-=3
            self.turn_of_burn-=1
            if self.turn_of_burn<=0:
                self.burning=False
    def deflect(self,turn_of_deflect=False):
        if turn_of_deflect:
            self.turn_of_deflect=turn_of_deflect
            self.deflecting=True
        else:
            if random.randrange(1,100)<=40:
                print('You block 5 damage.')
                self.HP+=5
            self.turn_of_deflect-=1
            if self.turn_of_deflect<=0:
                self.deflecting=False

    def consumable_update(self):
        if self.attacky:
            self.methattack()
        if self.defensey:
            self.methdefense()
        if self.speedy:
            self.methspeed()

    def methattack(self,attacky_turns=False):
        if attacky_turns:
            self.attacky_turns=attacky_turns
            self.attacky=True
        else:
            self.atk+=5
            self.attacky_turns-=1
            if self.attacky_turns<=0:
                self.atk-=5
                self.attacky=False

    def methdefense(self,defensey_turns=False):
        if defensey_turns:
            self.defensey_turns=defensey_turns
            self.defensey=True
        else:
            self.defn+=2
            self.defensey_turns-=1
            if self.defensey_turns<=0:
                self.defn-=2
                self.defensey=False

    def methspeed(self,speedy_turns=False):
        if speedy_turns:
            self.speedy_turns=speedy_turns
            self.speedy=True
        else:
            self.spd*=2
            self.speedy_turns-=1
            if self.speedy_turns<=0:
                self.spd/=2
                self.speedy=False

    # def cooldown_update(self):
    #     if self.ST_on_cooldown:
    #         self.ST_cooldown()

    # def ST_cooldown(self,CD_ST_turns=False):
    #     if CD_ST_turns:
    #         self.CD_ST_turns=CD_ST_turns
    #         self.ST_on_cooldown=True
    #     else:
    #         if sword_tackle in self.atk_useable:
    #             del self.atk_useable['Sword Tackle']
    #         self.CD_ST_turns-=1
    #         if self.CD_ST_turns<=0:
    #             self.atk_useable['Sword Tackle']=sword_tackle
    #             self.ST_on_cooldown=False

class inv_item:
    def __init__(self,name,description) -> None:
        self.name=name
        self.desc=description

class attack:
    def __init__(self,name,description,base_dmg,stamina_useage,turn_cooldown = 0) -> None:
        self.name=name
        self.desc=description
        self.base_dmg=base_dmg
        self.stam_use=stamina_useage
        self.TCD=turn_cooldown

#Inventory Items
#hp_potion=inv_item('Hp Potion','Heals charater for half of missing HP.')

#Basic Attacks
slash=attack('Slash','Basic attack. Deals 7 true damage.',7,15)
fireball=attack('Fireball','Basic attack. Deals 7 true damage.',7,15)
arrow=attack('Arrow','Basic attack. Deals 7 true damage',7,15)
#Warrior Attacks
sword_tackle=attack('Sword Tackle','Recklessly tackle with your sword.',15,25,turn_cooldown=1)
fire_slash=attack('Fire Slash','You light your sword ablaze.',25,35,turn_cooldown=2)
shield_bash=attack('Shield Bash','You feel the bash of the shield, it shakes your arm.',20,30,turn_cooldown=2)


#Character Classes
warrior=fighter('Warrior','Jack of all trades... master of none.',100,100,25,25,5,5,100,100,100)
warrior2=fighter('Warrior','Jack of all trades... master of none.',100,100,25,25,5,5,100,100,100)
warrior.atk_useable['Slash']=slash
warrior2.atk_useable['Slash']=slash
warrior.atk_useable['Sword Tackle']=sword_tackle
warrior2.atk_useable['Sword Tackle']=sword_tackle
warrior.atk_useable['Fire Slash']=fire_slash
warrior2.atk_useable['Fire Slash']=fire_slash
warrior.atk_useable['Shield Bash']=shield_bash
warrior2.atk_useable['Shield Bash']=shield_bash

paladin=fighter('Paladin','Excels at defense, healing, and lingering effects.',120,120,20,20,6,6,80,80,80)
paladin2=fighter('Paladin','Excels at defense, healing, and lingering effects.',120,120,20,20,6,6,80,80,80)
paladin.atk_useable['Slash']=slash
paladin2.atk_useable['Slash']=slash

assassin=fighter('Assassin','Fastest class. Applys bleed effect with most moves.',80,80,25,25,5,5,130,90,90)
assassin2=fighter('Assassin','Fastest class. Applys bleed effect with most moves.',80,80,25,25,5,5,130,90,90)
assassin.atk_useable['Slash']=slash
assassin2.atk_useable['Slash']=slash

knight=fighter('Knight','Hits for 2 turns worth of damage. Rides on horseback, takes a turn to regain momentum',120,120,20,20,6,6,120,100,100)
knight2=fighter('Knight','Hits for 2 turns worth of damage. Rides on horseback, takes a turn to regain momentum',120,120,20,20,6,6,120,100,100)
knight.atk_useable['Slash']=slash
knight2.atk_useable['Slash']=slash

archer=fighter('Archer','Pretty fast. Deals good damage with snipes in between armor.',80,80,30,30,4,4,110,110,110)
archer2=fighter('Archer','Pretty fast. Deals good damage with snipes in between armor.',80,80,30,30,4,4,110,110,110)
archer.atk_useable['Arrow']=arrow
archer2.atk_useable['Arrow']=arrow

mage=fighter('Mage','Slow but very powerful attacks. Low defense',100,100,30,30,4,4,70,120,120)
mage2=fighter('Mage','Slow but very powerful attacks. Low defense',100,100,30,30,4,4,70,120,120)
mage.atk_useable['Fireball']=fireball
mage2.atk_useable['Fireball']=fireball




#Class Dictionaries
playable={}
playable['Warrior']=warrior
playable['Paladin']=paladin
playable['Assassin']=assassin
playable['Knight']=knight
playable['Archer']=archer
playable['Mage']=mage
playable2={}
playable2['Warrior']=warrior2
playable2['Paladin']=paladin2
playable2['Assassin']=assassin2
playable2['Knight']=knight2
playable2['Archer']=archer2
playable2['Mage']=mage2

#consumable={}
#consumable['Hp Potion']=hp_potion