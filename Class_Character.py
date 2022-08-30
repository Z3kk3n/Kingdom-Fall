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
        self.dmging_three=False
        self.dmging_seven=False
        self.paladin_slowing=False
        self.turn_of_dmg_three=0
        self.turn_of_dmg_seven=0
        self.turn_of_paladin_slow=0
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
        self.five_on_cooldown=False
        self.six_on_cooldown=False
        self.seven_on_cooldown=False
        self.eight_on_cooldown=False
        self.nine_on_cooldown=False
        self.ten_on_cooldown=False
        self.eleven_on_cooldown=False
        self.twelve_on_cooldown=False
        self.thirteen_on_cooldown=False
        self.fourteen_on_cooldown=False
        self.fifteen_on_cooldown=False
        self.knight_on_cooldown=False
        self.one_CD_turns=0
        self.two_CD_turns=0
        self.three_CD_turns=0
        self.four_CD_turns=0
        self.five_CD_turns=0
        self.six_CD_turns=0
        self.seven_CD_turns=0
        self.eight_CD_turns=0
        self.nine_CD_turns=0
        self.ten_CD_turns=0
        self.eleven_CD_turns=0
        self.twelve_CD_turns=0
        self.thirteen_CD_turns=0
        self.fourteen_CD_turns=0
        self.fifteen_CD_turns=0
        self.knight_CD_turns=0


    #Method of checking for statis conditions
    def update(self):
        #Bad:
        if self.dmging_three:
            self.r_dmg_three()
        if self.dmging_seven:
            self.r_dmg_seven()
        if self.paladin_slowing:
            self.paladin_slow()
        #Good:
        if self.deflecting:
            self.deflect()

    #Methods of activating statis conditions
    def r_dmg_three(self,turn_of_dmg_three=False):
        if turn_of_dmg_three:
            self.turn_of_dmg_three=turn_of_dmg_three
            self.dmging_three=True
        else:
            print('Bleed - 3 HP.')
            self.HP-=3
            self.turn_of_dmg_three-=1
            if self.turn_of_dmg_three<=0:
                self.dmging_three=False

    def r_dmg_seven(self,turn_of_dmg_seven=False):
        if turn_of_dmg_seven:
            self.turn_of_dmg_seven=turn_of_dmg_seven
            self.dmging_seven=True
        else:
            print('You take 7 damage.')
            self.HP-=7
            self.turn_of_dmg_seven-=1
            if self.turn_of_dmg_seven<=0:
                self.dmging_seven=False

    def paladin_slow(self,turn_of_paladin_slow=False):
        if turn_of_paladin_slow:
            self.turn_of_paladin_slow=turn_of_paladin_slow
            self.paladin_slowing=True
        else:
            if self!=warrior2 or self!=paladin2 or self!=assassin2 or self!=knight2 or self!=archer2 or self!=mage2:
                if random.randrange(1,100)<=50:
                    print('You get your foot caught. Speed down.')
                    self.spd=paladin.b_spd
                self.turn_of_paladin_slow-=1
            elif self!=warrior or self!=paladin or self!=assassin or self!=knight or self!=archer or self!=mage:
                if random.randrange(1,100)<=50:
                    print('You get your foot caught. Speed down.')
                    self.spd=paladin.b_spd
                self.turn_of_paladin_slow-=1
            if self.turn_of_paladin_slow<=0:
                self.spd=self.b_spd
                self.paladin_slowing=False

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
        if self.five_on_cooldown:
            self.five_cooldown()
        if self.six_on_cooldown:
            self.six_cooldown()
        if self.seven_on_cooldown:
            self.seven_cooldown()
        if self.eight_on_cooldown:
            self.eight_cooldown()
        if self.nine_on_cooldown:
            self.nine_cooldown()
        if self.ten_on_cooldown:
            self.ten_cooldown()
        if self.eleven_on_cooldown:
            self.eleven_cooldown()
        if self.twelve_on_cooldown:
            self.twelve_cooldown()

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

    def five_cooldown(self,five_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if five_CD_turns:
                self.five_CD_turns=five_CD_turns
                self.five_on_cooldown=True
            else:
                fissure.text_color='\033[0;30m'
                fissure.on_cooldown=True
                self.five_CD_turns-=1
                if self.five_CD_turns<=0:
                    fissure.text_color='\033[0m'
                    fissure.on_cooldown=False
                    self.five_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if five_CD_turns:
                self.five_CD_turns=five_CD_turns
                self.five_on_cooldown=True
            else:
                fissure2.text_color='\033[0;30m'
                fissure2.on_cooldown=True
                self.five_CD_turns-=1
                if self.five_CD_turns<=0:
                    fissure2.text_color='\033[0m'
                    fissure2.on_cooldown=False
                    self.five_on_cooldown=False

    def six_cooldown(self,six_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if six_CD_turns:
                self.six_CD_turns=six_CD_turns
                self.six_on_cooldown=True
            else:
                heal.text_color='\033[0;30m'
                heal.on_cooldown=True
                self.six_CD_turns-=1
                if self.six_CD_turns<=0:
                    heal.text_color='\033[0m'
                    heal.on_cooldown=False
                    self.six_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if six_CD_turns:
                self.six_CD_turns=six_CD_turns
                self.six_on_cooldown=True
            else:
                heal2.text_color='\033[0;30m'
                heal2.on_cooldown=True
                self.six_CD_turns-=1
                if self.six_CD_turns<=0:
                    heal2.text_color='\033[0m'
                    heal2.on_cooldown=False
                    self.six_on_cooldown=False
                    
    def seven_cooldown(self,seven_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if seven_CD_turns:
                self.seven_CD_turns=seven_CD_turns
                self.seven_on_cooldown=True
            else:
                vampirism.text_color='\033[0;30m'
                vampirism.on_cooldown=True
                self.seven_CD_turns-=1
                if self.seven_CD_turns<=0:
                    vampirism.text_color='\033[0m'
                    vampirism.on_cooldown=False
                    self.seven_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if seven_CD_turns:
                self.seven_CD_turns=seven_CD_turns
                self.seven_on_cooldown=True
            else:
                vampirism2.text_color='\033[0;30m'
                vampirism2.on_cooldown=True
                self.seven_CD_turns-=1
                if self.seven_CD_turns<=0:
                    vampirism2.text_color='\033[0m'
                    vampirism2.on_cooldown=False
                    self.seven_on_cooldown=False
                    
    def eight_cooldown(self,eight_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if eight_CD_turns:
                self.eight_CD_turns=eight_CD_turns
                self.eight_on_cooldown=True
            else:
                silent_takedown.text_color='\033[0;30m'
                silent_takedown.on_cooldown=True
                self.eight_CD_turns-=1
                if self.eight_CD_turns<=0:
                    silent_takedown.text_color='\033[0m'
                    silent_takedown.on_cooldown=False
                    self.eight_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if eight_CD_turns:
                self.eight_CD_turns=eight_CD_turns
                self.eight_on_cooldown=True
            else:
                silent_takedown2.text_color='\033[0;30m'
                silent_takedown2.on_cooldown=True
                self.eight_CD_turns-=1
                if self.eight_CD_turns<=0:
                    silent_takedown2.text_color='\033[0m'
                    silent_takedown2.on_cooldown=False
                    self.eight_on_cooldown=False

    def nine_cooldown(self,nine_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if nine_CD_turns:
                self.nine_CD_turns=nine_CD_turns
                self.nine_on_cooldown=True
            else:
                ryuu.text_color='\033[0;30m'
                ryuu.on_cooldown=True
                self.nine_CD_turns-=1
                if self.nine_CD_turns<=0:
                    ryuu.text_color='\033[0m'
                    ryuu.on_cooldown=False
                    self.nine_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if nine_CD_turns:
                self.nine_CD_turns=nine_CD_turns
                self.nine_on_cooldown=True
            else:
                ryuu2.text_color='\033[0;30m'
                ryuu2.on_cooldown=True
                self.nine_CD_turns-=1
                if self.nine_CD_turns<=0:
                    ryuu2.text_color='\033[0m'
                    ryuu2.on_cooldown=False
                    self.nine_on_cooldown=False

    def ten_cooldown(self,ten_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if ten_CD_turns:
                self.ten_CD_turns=ten_CD_turns
                self.ten_on_cooldown=True
            else:
                firework.text_color='\033[0;30m'
                firework.on_cooldown=True
                self.ten_CD_turns-=1
                if self.ten_CD_turns<=0:
                    firework.text_color='\033[0m'
                    firework.on_cooldown=False
                    self.te_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if ten_CD_turns:
                self.ten_CD_turns=ten_CD_turns
                self.ten_on_cooldown=True
            else:
                firework2.text_color='\033[0;30m'
                firework2.on_cooldown=True
                self.ten_CD_turns-=1
                if self.ten_CD_turns<=0:
                    firework2.text_color='\033[0m'
                    firework2.on_cooldown=False
                    self.ten_on_cooldown=False

    def eleven_cooldown(self,eleven_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if eleven_CD_turns:
                self.eleven_CD_turns=eleven_CD_turns
                self.eleven_on_cooldown=True
            else:
                deliberate_miss.text_color='\033[0;30m'
                deliberate_miss.on_cooldown=True
                self.eleven_CD_turns-=1
                if self.eleven_CD_turns<=0:
                    deliberate_miss.text_color='\033[0m'
                    deliberate_miss.on_cooldown=False
                    self.eleven_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if eleven_CD_turns:
                self.eleven_CD_turns=eleven_CD_turns
                self.eleven_on_cooldown=True
            else:
                deliberate_miss2.text_color='\033[0;30m'
                deliberate_miss2.on_cooldown=True
                self.eleven_CD_turns-=1
                if self.eleven_CD_turns<=0:
                    deliberate_miss2.text_color='\033[0m'
                    deliberate_miss2.on_cooldown=False
                    self.eleven_on_cooldown=False

    def twelve_cooldown(self,twelve_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if twelve_CD_turns:
                self.twelve_CD_turns=twelve_CD_turns
                self.twelve_on_cooldown=True
            else:
                hwacha.text_color='\033[0;30m'
                hwacha.on_cooldown=True
                self.twelve_CD_turns-=1
                if self.twelve_CD_turns<=0:
                    hwacha.text_color='\033[0m'
                    hwacha.on_cooldown=False
                    self.twelve_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if twelve_CD_turns:
                self.twelve_CD_turns=twelve_CD_turns
                self.twelve_on_cooldown=True
            else:
                hwacha2.text_color='\033[0;30m'
                hwacha2.on_cooldown=True
                self.twelve_CD_turns-=1
                if self.twelve_CD_turns<=0:
                    hwacha2.text_color='\033[0m'
                    hwacha2.on_cooldown=False
                    self.twelve_on_cooldown=False

    def thirteen_cooldown(self,thirteen_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if thirteen_CD_turns:
                self.thirteen_CD_turns=thirteen_CD_turns
                self.thirteen_on_cooldown=True
            else:
                frost_heal.text_color='\033[0;30m'
                frost_heal.on_cooldown=True
                self.thirteen_CD_turns-=1
                if self.thirteen_CD_turns<=0:
                    frost_heal.text_color='\033[0m'
                    frost_heal.on_cooldown=False
                    self.thirteen_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if thirteen_CD_turns:
                self.thirteen_CD_turns=thirteen_CD_turns
                self.thirteen_on_cooldown=True
            else:
                frost_heal2.text_color='\033[0;30m'
                frost_heal2.on_cooldown=True
                self.thirteen_CD_turns-=1
                if self.thirteen_CD_turns<=0:
                    frost_heal2.text_color='\033[0m'
                    frost_heal2.on_cooldown=False
                    self.thirteen_on_cooldown=False

    def fourteen_cooldown(self,fourteen_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if fourteen_CD_turns:
                self.fourteen_CD_turns=fourteen_CD_turns
                self.fourteen_on_cooldown=True
            else:
                ground_lance.text_color='\033[0;30m'
                ground_lance.on_cooldown=True
                self.fourteen_CD_turns-=1
                if self.fourteen_CD_turns<=0:
                    ground_lance.text_color='\033[0m'
                    ground_lance.on_cooldown=False
                    self.fourteen_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if fourteen_CD_turns:
                self.fourteen_CD_turns=fourteen_CD_turns
                self.fourteen_on_cooldown=True
            else:
                ground_lance2.text_color='\033[0;30m'
                ground_lance2.on_cooldown=True
                self.fourteen_CD_turns-=1
                if self.fourteen_CD_turns<=0:
                    ground_lance2.text_color='\033[0m'
                    ground_lance2.on_cooldown=False
                    self.fourteen_on_cooldown=False

    def fifteen_cooldown(self,fifteen_CD_turns=False):
        if self==warrior or self==paladin or self==assassin or self==knight or self==archer or self==mage:
            if fifteen_CD_turns:
                self.fifteen_CD_turns=fifteen_CD_turns
                self.fifteen_on_cooldown=True
            else:
                explosion.text_color='\033[0;30m'
                explosion.on_cooldown=True
                self.fifteen_CD_turns-=1
                if self.fifteen_CD_turns<=0:
                    explosion.text_color='\033[0m'
                    explosion.on_cooldown=False
                    self.fifteen_on_cooldown=False
        elif self==warrior2 or self==paladin2 or self==assassin2 or self==knight2 or self==archer2 or self==mage2:
            if fifteen_CD_turns:
                self.fifteen_CD_turns=fifteen_CD_turns
                self.fifteen_on_cooldown=True
            else:
                explosion2.text_color='\033[0;30m'
                explosion2.on_cooldown=True
                self.fifteen_CD_turns-=1
                if self.fifteen_CD_turns<=0:
                    explosion2.text_color='\033[0m'
                    explosion2.on_cooldown=False
                    self.fifteen_on_cooldown=False

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
fire_slash=attack('Fire Slash','Lights your sword ablaze.',25,35,'\033[0m')
fire_slash2=attack('Fire Slash','Lights your sword ablaze.',25,35,'\033[0m')
shield_bash=attack('Shield Bash','The bash of the shield shakes your arm.',20,30,'\033[0m')
shield_bash2=attack('Shield Bash','The bash of the shield shakes your arm.',20,30,'\033[0m')
#Paladin Attacks
tornado_slash=attack('Tornado Slash','Slash multiple times in succession.',12,25,'\033[0m')
tornado_slash2=attack('Tornado Slash','Slash multiple times in succession.',12,25,'\033[0m')
fissure=attack('Fissure','Splits the ground in two, opponent may get caught.',30,35,'\033[0m')
fissure2=attack('Fissure','Splits the ground in two, opponent may get caught.',30,35,'\033[0m')
heal=attack('Heal','Heals 40 percent of max health.',48,30,'\033[0m')
heal2=attack('Heal','Heals 40 percent of max health.',48,30,'\033[0m')
#Assassin Attacks
vampirism=attack('Vampirism','Steals health and applies bleed.',21,30,'\033[0m')
vampirism2=attack('Vampirism','Steals health and applies bleed.',21,30,'\033[0m')
silent_takedown=attack('Silent Takedown','Stealth behind the enemy and attack, applies bleed.',26,30,'\033[0m')
silent_takedown2=attack('Silent Takedown','Stealth behind the enemy and attack, applies bleed.',26,30,'\033[0m')
ryuu=attack('Ryuu','Strike like a dragon, applies bleed.',30,50,'\033[0m')
ryuu2=attack('Ryuu','Strike like a dragon, applies bleed.',30,50,'\033[0m')
#Knight Attacks
#Archer Attacks
firework=attack('Firework','Fires an arrow tipped with a small bomb.',15,30,'\033[0m')
firework2=attack('Firework','Fires an arrow tipped with a small bomb.',15,30,'\033[0m')
deliberate_miss=attack('Deliberate Miss','Fire a bomb arrow near the ground. Opponent speed and damage down.',10,40,'\033[0m')
deliberate_miss2=attack('Deliberate Miss','Fire a bomb arrow near the ground. Opponent speed and damage down.',10,40,'\033[0m')
hwacha=attack('Hwacha','Rain of firework arrows. Pure damage but slow cooldown.',28,50,'\033[0m')
hwacha2=attack('Hwacha','Rain of firework arrows. Pure damage but slow cooldown.',28,50,'\033[0m')
#Mage Attacks
frost_heal=attack('Frost Heal','Heal so potent and ice blast is released.',10,30,'\033[0m')
frost_heal2=attack('Frost Heal','Heal so potent and ice blast is released.',10,30,'\033[0m')
ground_lance=attack('Ground Lance','Break apart the earth into lances',10,30,'\033[0m')
ground_lance2=attack('Ground Lance','Break apart the earth into lances',10,30,'\033[0m')
explosion=attack('Explosion','EX-CI-PA-LO-SION, Big Boom, Big Damage.',30,50,'\033[0m')
explosion2=attack('Explosion','EX-CI-PA-LO-SION, Big Boom, Big Damage.',30,50,'\033[0m')

#Character Classes
warrior=fighter('Warrior','Jack of all trades... master of none.',120,120,25,25,5,5,100,100,100,100)
warrior2=fighter('Warrior','Jack of all trades... master of none.',120,120,25,25,5,5,100,100,100,100)
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

paladin=fighter('Paladin','Excels at defense, healing, and lingering effects.',140,140,20,20,6,6,80,80,80,80)
paladin2=fighter('Paladin','Excels at defense, healing, and lingering effects.',140,140,20,20,6,6,80,80,80,80)
paladin.atk_useable[slash]=slash
paladin2.atk_useable[slash2]=slash2
paladin.atk_useable[tornado_slash]=tornado_slash
paladin2.atk_useable[tornado_slash2]=tornado_slash2
paladin.atk_useable[fissure]=fissure
paladin2.atk_useable[fissure2]=fissure2
paladin.atk_useable[heal]=heal
paladin2.atk_useable[heal2]=heal2
paladin.atk_useableS['Slash']=slash
paladin2.atk_useableS['Slash']=slash
paladin.atk_useableS['Tornado Slash']=tornado_slash
paladin2.atk_useableS['Tornado Slash']=tornado_slash2
paladin.atk_useableS['Fissure']=fissure
paladin2.atk_useableS['Fissure']=fissure2
paladin.atk_useableS['Heal']=heal
paladin2.atk_useableS['Heal']=heal2

assassin=fighter('Assassin','Fastest class. Applys bleed effect with most moves.',100,100,25,25,5,5,130,130,90,90)
assassin2=fighter('Assassin','Fastest class. Applys bleed effect with most moves.',100,100,25,25,5,5,130,130,90,90)
assassin.atk_useable[slash]=slash
assassin2.atk_useable[slash2]=slash2
assassin.atk_useable[vampirism]=vampirism
assassin2.atk_useable[vampirism2]=vampirism2
assassin.atk_useable[silent_takedown]=silent_takedown
assassin2.atk_useable[silent_takedown2]=silent_takedown2
assassin.atk_useable[ryuu]=ryuu
assassin2.atk_useable[ryuu2]=ryuu2
assassin.atk_useableS['Slash']=slash
assassin2.atk_useableS['Slash']=slash2
assassin.atk_useableS['Vampirism']=vampirism
assassin2.atk_useableS['Vampirism']=vampirism2
assassin.atk_useableS['Silent Takedown']=silent_takedown
assassin2.atk_useableS['Silent Takedown']=silent_takedown2
assassin.atk_useableS['Ryuu']=ryuu
assassin2.atk_useableS['Ryuu']=ryuu2

knight=fighter('Knight','Hits for 2 turns worth of damage. Rides on horseback, takes a turn to regain momentum',140,140,20,20,6,6,120,120,100,100)
knight2=fighter('Knight','Hits for 2 turns worth of damage. Rides on horseback, takes a turn to regain momentum',140,140,20,20,6,6,120,120,100,100)
knight.atk_useable['Slash']=slash
knight2.atk_useable['Slash']=slash

archer=fighter('Archer','Pretty fast. Deals good damage with snipes in between armor.',100,100,30,30,4,4,110,110,110,110)
archer2=fighter('Archer','Pretty fast. Deals good damage with snipes in between armor.',100,100,30,30,4,4,110,110,110,110)
archer.atk_useable[arrow]=arrow
archer2.atk_useable[arrow2]=arrow2
archer.atk_useable[firework]=firework
archer2.atk_useable[firework2]=firework2
archer.atk_useable[deliberate_miss]=deliberate_miss
archer2.atk_useable[deliberate_miss2]=deliberate_miss2
archer.atk_useable[hwacha]=hwacha
archer2.atk_useable[hwacha2]=hwacha2
archer.atk_useableS['Arrow']=arrow
archer2.atk_useableS['Arrow']=arrow2
archer.atk_useableS['Firework']=firework
archer2.atk_useableS['Firework']=firework2
archer.atk_useableS['Deliberate Miss']=deliberate_miss
archer2.atk_useableS['Deliberate Miss']=deliberate_miss2
archer.atk_useableS['Hwacha']=hwacha
archer2.atk_useableS['Hwacha']=hwacha2

mage=fighter('Mage','Slow but very powerful attacks. Low defense',120,120,30,30,4,4,70,70,120,120)
mage2=fighter('Mage','Slow but very powerful attacks. Low defense',120,120,30,30,4,4,70,70,120,120)
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
