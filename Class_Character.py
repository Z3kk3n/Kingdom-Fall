# if __name__=='main':
class fighter:
    def __init__(self,name,description,base_hp,hit_points,base_attack,attack,base_defense,defense,speed,stamina,) -> None:
        self.name=name
        self.desc=description
        self.b_HP=base_hp
        self.HP=hit_points
        self.b_atk=base_attack
        self.atk=attack
        self.b_defn=base_defense
        self.defn=defense
        self.spd=speed
        self.stam=stamina
        self.atk_useable={}
        self.selected_atk=None
        self.consumable={"HP Potion":inv_item('HP Potion','Heals charater for 10 HP.')}
        self.selected_item=None
        self.initiative=False

class inv_item:
    def __init__(self,name,description) -> None:
        self.name=name
        self.desc=description

class attack:
    def __init__(self,name,description,base_dmg,stamina_useage) -> None:
        self.name=name
        self.desc=description
        self.base_dmg=base_dmg
        self.stam_use=stamina_useage


#Inventory Items
hp_potion=inv_item('HP Potion','Heals charater for half of missing HP.')

#Attacks
slash=attack('Slash','Basic attack. Deals 7 true damage.',7,10)
fireball=attack('Fireball','Basic attack. Deals 7 true damage.',7,10)
arrow=attack('Arrow','Basic attack. Deals 7 true damage',7,10)




#Character Classes
warrior=fighter('Warrior','Jack of all trades... master of none.',100,100,25,25,5,5,100,100)
warrior2=fighter('Warrior','Jack of all trades... master of none.',100,100,25,25,5,5,100,100)
warrior.atk_useable['Slash']=slash
warrior2.atk_useable['Slash']=slash

paladin=fighter('Paladin','Excels at defense, healing, and lingering effects.',120,120,20,20,6,6,80,80)
paladin2=fighter('Paladin','Excels at defense, healing, and lingering effects.',120,120,20,20,6,6,80,80)
paladin.atk_useable['Slash']=slash
paladin2.atk_useable['Slash']=slash

assassin=fighter('Assassin','Fastest class. Applys bleed effect with most moves.',80,80,25,25,5,5,130,90)
assassin2=fighter('Assassin','Fastest class. Applys bleed effect with most moves.',80,80,25,25,5,5,130,90)
assassin.atk_useable['Slash']=slash
assassin2.atk_useable['Slash']=slash

knight=fighter('Knight','Hits for 2 turns worth of damage. Rides on horseback, takes a turn to regain momentum',120,120,20,20,6,6,120,100)
knight2=fighter('Knight','Hits for 2 turns worth of damage. Rides on horseback, takes a turn to regain momentum',120,120,20,20,6,6,120,100)
knight.atk_useable['Slash']=slash
knight2.atk_useable['Slash']=slash

archer=fighter('Archer','Pretty fast. Deals good damage with snipes in between armor.',80,80,30,30,4,4,110,110)
archer2=fighter('Archer','Pretty fast. Deals good damage with snipes in between armor.',80,80,30,30,4,4,110,110)
archer.atk_useable['Arrow']=arrow
archer2.atk_useable['Arrow']=arrow

mage=fighter('Mage','Slow but very powerful attacks. Low defense',100,100,30,30,4,4,70,120)
mage2=fighter('Mage','Slow but very powerful attacks. Low defense',100,100,30,30,4,4,70,120)
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



consumable={}
consumable['HP Potion']=hp_potion

#useable={}
#useable['Slash']=slash