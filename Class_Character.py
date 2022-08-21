import random
# from Fight_System import player1,player2

class fighter:
    def __init__(self,name,description,base_hp,hit_points,base_attack,attack,base_defense,defense,base_speed,speed,max_stamina,stamina,) -> None:
        self.name=name
        self.desc=description
        self.b_HP=base_hp
        self.HP=hit_points
        self.b_atk=base_attack
        self.atk=attack
        self.b_defn=base_defense
        self.defn=defense
        self.b_spd=base_speed
        self.spd=speed
        self.max_stam=max_stamina
        self.stam=stamina
        self.initiative=False
    #Attacks and Items
        self.atk_useable={}
        self.atk_useableS={}
        self.selected_atk=None
        self.consumable={'Hp Potion':inv_item('Hp Potion','Heals charater for half of missing HP.'),
                        'Attack Potion':inv_item('Attack Potion','Increases player attack for one turn.'),
                        'Defense Potion':inv_item('Defense Potion','Increases player defense for one turn.'),
                        'Speed Potion':inv_item('Speed Potion','Increases player speed for one turn.')}
        self.selected_item=None
    #Booleans and Turns for statis conditions
        #Bad:
        self.dmging_five=False
        self.dmging_seven=False
        self.turn_of_dmg_five=0
        self.turn_of_dmg_seven=0
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
        self.one_on_cooldown=False
        self.two_on_cooldown=False
        self.three_on_cooldown=False
        self.four_on_cooldown=False
        self.one_CD_turns=0
        self.two_CD_turns=0
        self.three_CD_turns=0
        self.four_CD_turns=0

    #Method of checking for statis conditions
    def update(self):
        #Bad:
        if self.dmging_five:
            self.r_dmg_five()
        if self.dmging_seven:
            self.r_dmg_seven()
        #Good:
        if self.deflect:
            self.deflect()

    #Methods of activating statis conditions
    def r_dmg_five(self,turn_of_dmg_five=False):
        if turn_of_dmg_five:
            self.turn_of_dmg_five=turn_of_dmg_five
            self.dmging_five=True
        else:
            self.HP-=5
            self.turn_of_dmg_five-=1
            if self.turn_of_dmg_five<=0:
                self.dmging_five=False

    def r_dmg_seven(self,turn_of_dmg_seven=False):
        if turn_of_dmg_seven:
            self.turn_of_dmg_seven=turn_of_dmg_seven
            self.dmging_seven=True
        else:
            self.HP-=7
            self.turn_of_dmg_seven-=1
            if self.turn_of_dmg_seven<=0:
                self.dmging_seven=False

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
                self.atk=self.b_atk
                self.attacky=False

    def methdefense(self,defensey_turns=False):
        if defensey_turns:
            self.defensey_turns=defensey_turns
            self.defensey=True
        else:
            self.defn+=2
            self.defensey_turns-=1
            if self.defensey_turns<=0:
                self.defn=self.b_defn
                self.defensey=False

    def methspeed(self,speedy_turns=False):
        if speedy_turns:
            self.speedy_turns=speedy_turns
            self.speedy=True
        else:
            self.spd*=2
            self.speedy_turns-=1
            if self.speedy_turns<=0:
                self.spd=self.b_spd
                self.speedy=False

    def cooldown_update(self):
        if self.one_on_cooldown:
            self.one_cooldown()
        if self.two_on_cooldown:
            self.two_cooldown()
        if self.three_on_cooldown:
            self.three_cooldown()
        if self.four_on_cooldown:
            self.four_cooldown()

    def one_cooldown(self,one_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if one_CD_turns:
                self.one_CD_turns=one_CD_turns
                self.one_on_cooldown=True
            else:
                sword_tackle.text_color='\033[0;30m'
                sword_tackle.on_cooldown=True
                self.one_CD_turns-=1
                if self.one_CD_turns<=0:
                    sword_tackle.text_color='\033[0m'
                    sword_tackle.on_cooldown=False
                    self.one_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if one_CD_turns:
                self.one_CD_turns=one_CD_turns
                self.one_on_cooldown=True
            else:
                sword_tackle2.text_color='\033[0;30m'
                sword_tackle2.on_cooldown=True
                self.one_CD_turns-=1
                if self.one_CD_turns<=0:
                    sword_tackle2.text_color='\033[0m'
                    sword_tackle2.on_cooldown=False
                    self.one_on_cooldown=False

    def two_cooldown(self,two_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if two_CD_turns:
                self.two_CD_turns=two_CD_turns
                self.two_on_cooldown=True
            else:
                fire_slash.text_color='\033[0;30m'
                fire_slash.on_cooldown=True
                self.two_CD_turns-=1
                if self.two_CD_turns<=0:
                    fire_slash.text_color='\033[0m'
                    fire_slash.on_cooldown=False
                    self.two_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if two_CD_turns:
                self.two_CD_turns=two_CD_turns
                self.two_on_cooldown=True
            else:
                fire_slash2.text_color='\033[0;30m'
                fire_slash2.on_cooldown=True
                self.two_CD_turns-=1
                if self.two_CD_turns<=0:
                    fire_slash2.text_color='\033[0m'
                    fire_slash2.on_cooldown=False
                    self.two_on_cooldown=False

    def three_cooldown(self,three_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if three_CD_turns:
                self.three_CD_turns=three_CD_turns
                self.three_on_cooldown=True
            else:
                shield_bash.text_color='\033[0;30m'
                shield_bash.on_cooldown=True
                self.three_CD_turns-=1
                if self.three_CD_turns<=0:
                    shield_bash.text_color='\033[0m'
                    shield_bash.on_cooldown=False
                    self.three_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if three_CD_turns:
                self.three_CD_turns=three_CD_turns
                self.three_on_cooldown=True
            else:
                shield_bash2.text_color='\033[0;30m'
                shield_bash2.on_cooldown=True
                self.three_CD_turns-=1
                if self.three_CD_turns<=0:
                    shield_bash2.text_color='\033[0m'
                    shield_bash2.on_cooldown=False
                    self.three_on_cooldown=False

    def four_cooldown(self,four_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if four_CD_turns:
                self.four_CD_turns=four_CD_turns
                self.four_on_cooldown=True
            else:
                tornado_slash.text_color='\033[0;30m'
                tornado_slash.on_cooldown=True
                self.four_CD_turns-=1
                if self.four_CD_turns<=0:
                    tornado_slash.text_color='\033[0m'
                    tornado_slash.on_cooldown=False
                    self.four_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if four_CD_turns:
                self.four_CD_turns=four_CD_turns
                self.four_on_cooldown=True
            else:
                tornado_slash2.text_color='\033[0;30m'
                tornado_slash2.on_cooldown=True
                self.four_CD_turns-=1
                if self.four_CD_turns<=0:
                    tornado_slash2.text_color='\033[0m'
                    tornado_slash2.on_cooldown=False
                    self.four_on_cooldown=False

class inv_item:
    def __init__(self,name,description) -> None:
        self.name=name
        self.desc=description

class attack:
    def __init__(self,name,description,base_dmg,stamina_useage,text_color,on_cooldown=False) -> None:
        self.name=name
        self.desc=description
        self.base_dmg=base_dmg
        self.stam_use=stamina_useage
        self.text_color=text_color
        self.on_cooldown=on_cooldown

#Inventory Items
#hp_potion=inv_item('Hp Potion','Heals charater for half of missing HP.')

#Basic Attacks
slash=attack('Slash','Basic attack. Deals 7 true damage.',7,15,'\033[0m')
slash2=attack('Slash','Basic attack. Deals 7 true damage.',7,15,'\033[0m')
fireball=attack('Fireball','Basic attack. Deals 7 true damage.',7,15,'\033[0m')
fireball2=attack('Fireball','Basic attack. Deals 7 true damage.',7,15,'\033[0m')
arrow=attack('Arrow','Basic attack. Deals 7 true damage',7,15,'\033[0m')
arrow2=attack('Arrow','Basic attack. Deals 7 true damage',7,15,'\033[0m')
#Warrior Attacks
sword_tackle=attack('Sword Tackle','Recklessly tackle with your sword.',15,25,'\033[0m')
sword_tackle2=attack('Sword Tackle','Recklessly tackle with your sword.',15,25,'\033[0m')
fire_slash=attack('Fire Slash','You light your sword ablaze.',25,35,'\033[0m')
fire_slash2=attack('Fire Slash','You light your sword ablaze.',25,35,'\033[0m')
shield_bash=attack('Shield Bash','You feel the bash of the shield, it shakes your arm.',20,30,'\033[0m')
shield_bash2=attack('Shield Bash','You feel the bash of the shield, it shakes your arm.',20,30,'\033[0m')
#Paladin Attacks
tornado_slash=attack('Tornado Tackle','Slash multiple times in succession.',12,25,'\033[0m')
tornado_slash2=attack('Tornado Tackle','Slash multiple times in succession.',12,25,'\033[0m')

#Character Classes
warrior=fighter('Warrior','Jack of all trades... master of none.',100,100,25,25,5,5,100,100,100,100)
warrior2=fighter('Warrior','Jack of all trades... master of none.',100,100,25,25,5,5,100,100,100,100)
warrior.atk_useable[slash]=slash
warrior2.atk_useable[slash2]=slash2
warrior.atk_useable[sword_tackle]=sword_tackle
warrior2.atk_useable[sword_tackle2]=sword_tackle2
warrior.atk_useable[fire_slash]=fire_slash
warrior2.atk_useable[fire_slash2]=fire_slash2
warrior.atk_useable[shield_bash]=shield_bash
warrior2.atk_useable[shield_bash2]=shield_bash2
warrior.atk_useableS['Slash']=slash
warrior2.atk_useableS['Slash']=slash2
warrior.atk_useableS['Sword Tackle']=sword_tackle
warrior2.atk_useableS['Sword Tackle']=sword_tackle2
warrior.atk_useableS['Fire Slash']=fire_slash
warrior2.atk_useableS['Fire Slash']=fire_slash2
warrior.atk_useableS['Shield Bash']=shield_bash
warrior2.atk_useableS['Shield Bash']=shield_bash2

paladin=fighter('Paladin','Excels at defense, healing, and lingering effects.',120,120,20,20,6,6,80,80,80,80)
paladin2=fighter('Paladin','Excels at defense, healing, and lingering effects.',120,120,20,20,6,6,80,80,80,80)
paladin.atk_useable[slash]=slash
paladin2.atk_useable[slash2]=slash2
paladin.atk_useable[tornado_slash]=tornado_slash
paladin2.atk_useable[tornado_slash2]=tornado_slash2
paladin.atk_useableS['Slash']=slash
paladin2.atk_useableS['Slash']=slash
paladin.atk_useable['Tornado Slash']=tornado_slash
paladin2.atk_useable['Tornado Slash']=tornado_slash2

assassin=fighter('Assassin','Fastest class. Applys bleed effect with most moves.',80,80,25,25,5,5,130,130,90,90)
assassin2=fighter('Assassin','Fastest class. Applys bleed effect with most moves.',80,80,25,25,5,5,130,130,90,90)
assassin.atk_useable['Slash']=slash
assassin2.atk_useable['Slash']=slash

knight=fighter('Knight','Hits for 2 turns worth of damage. Rides on horseback, takes a turn to regain momentum',120,120,20,20,6,6,120,120,100,100)
knight2=fighter('Knight','Hits for 2 turns worth of damage. Rides on horseback, takes a turn to regain momentum',120,120,20,20,6,6,120,120,100,100)
knight.atk_useable['Slash']=slash
knight2.atk_useable['Slash']=slash

archer=fighter('Archer','Pretty fast. Deals good damage with snipes in between armor.',80,80,30,30,4,4,110,110,110,110)
archer2=fighter('Archer','Pretty fast. Deals good damage with snipes in between armor.',80,80,30,30,4,4,110,110,110,110)
archer.atk_useable['Arrow']=arrow
archer2.atk_useable['Arrow']=arrow

mage=fighter('Mage','Slow but very powerful attacks. Low defense',100,100,30,30,4,4,70,70,120,120)
mage2=fighter('Mage','Slow but very powerful attacks. Low defense',100,100,30,30,4,4,70,70,120,120)
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