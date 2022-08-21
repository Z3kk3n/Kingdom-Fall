import Class_Character
import FS_Engine
import msvcrt
import os,sys,time,random

def slow_type(text,typing_speed= 100,new_line=True):

    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    if new_line:
        print ('')
    while msvcrt.kbhit():
        msvcrt.getch()

os.system('cls')
print('\nWelcome to Kingdom Fall! Player 1 and Player 2 are on opposite sides of a war.\nYou are going to have a 1v1 for a very impotant territory.\nWhoever wins this battle wins the war. Good luck!')
print('\nNOTE: Game is NOT capital letter dependent. You can also type the number associated with the option.')

while True:
    game_start=input("Ready to battle? Type 'Fight'!\n>")
    if game_start=='Fight' or game_start=='fight' or game_start=='test':
        break
    else:
        pass


if game_start == 'Fight'or game_start == 'fight':

    while True:
        os.system('cls')
        print('Player 1, choose your class!')
        player1=None
        for index,ftype in enumerate(Class_Character.playable):
            print(f'[{index+1}] {ftype}')

        selection=input('>')
        try:
            selection = int(selection)-1
            for index,ftype in enumerate(Class_Character.playable):
                if index == selection:
                    player1= Class_Character.playable[ftype]
        except ValueError:
            selection=selection.capitalize()
            if selection in Class_Character.playable:
                player1= Class_Character.playable[selection]
        while True:
            os.system('cls')
            playercheck=input(f'\nAre you certain about this class? [Yes][No]\n\nClass: {player1.name}\nDescription: {player1.desc}\nMax HP: {player1.b_HP}\nBase Attack: {player1.b_atk}\nBase Defense: {player1.b_defn}\nSpeed: {player1.spd}\nStamina: {player1.stam}\n>')

            if playercheck == 'Yes' or playercheck == 'yes':
                break
            elif playercheck == 'No' or playercheck == 'no':
                player1=None
                break
            else:
                pass
        if player1:
            break
        else:
            pass

    while True:
        os.system('cls')
        print('Player 2, choose your class!')
        player2=None
        for index,ftype in enumerate(Class_Character.playable2):
            print(f'[{index+1}] {ftype}')

        selection=input('>')
        try:
            selection = int(selection)-1
            for index,ftype in enumerate(Class_Character.playable2):
                if index == selection:
                    player2= Class_Character.playable2[ftype]
        except ValueError:
            selection=selection.capitalize()
            if selection in Class_Character.playable2:
                player2= Class_Character.playable2[selection]
        while True:
            os.system('cls')
            playercheck=input(f'\nAre you certain about this class? [Yes][No]\n\nClass: {player2.name}\nDescription: {player2.desc}\nMax HP: {player2.b_HP}\nBase Attack: {player2.b_atk}\nBase Defense: {player2.b_defn}\nSpeed: {player2.spd}\nStamina: {player2.stam}\n>')

            if playercheck == 'Yes' or playercheck == 'yes':
                break
            if playercheck == 'No' or playercheck == 'no':
                player2=None
                break
            else:
                pass
        if player2:
            break
        else:
            pass
elif game_start == 'test':
    player1 = Class_Character.warrior
    player2 = Class_Character.warrior2
else:
    os.system('cls')
    exit()

turn=0
player_list=[player1,player2]
while True:
    turn+=1
    player1.stam += 10
    player1.stam = min(player1.stam,player1.max_stam)
    player2.stam += 10
    player2.stam = min(player2.stam,player2.max_stam)

    player1.selected_item = None
    player2.selected_item = None
    player1.selected_atk = None
    player2.selected_atk = None

    player1.cooldown_update()
    player2.cooldown_update()

    while True:
        os.system('cls')
        print(f"--------Turn:{turn}--------\n")

        print("player 1 choose your action. Type 'End' to finish turn.\n[1] Fight\n[2] Bag\n[3] Status")
        Act=input(">")
        if Act=='End' or Act=='end':
            break
        if Act in FS_Engine.action:
            temp_item=eval(f"FS_Engine.{FS_Engine.action[Act]}(player1,player2)")
            if isinstance(temp_item,Class_Character.inv_item):
                player1.selected_item=temp_item
            if isinstance(temp_item,Class_Character.attack):
                player1.selected_atk=temp_item
    while True:
        os.system('cls')
        print(f"--------Turn:{turn}--------\n")

        print("player 2 choose your action. Type 'End' to finish turn.\n[1] Fight\n[2] Bag\n[3] Status")
        Act=input(">")
        if Act=='End' or Act=='end':
            break
        if Act in FS_Engine.action:
            temp_item=eval(f"FS_Engine.{FS_Engine.action[Act]}(player2,player1)")
            if isinstance(temp_item,Class_Character.inv_item):
                player2.selected_item=temp_item
            if isinstance(temp_item,Class_Character.attack):
                player2.selected_atk=temp_item




    os.system('cls')
    print(f'--------Turn:{turn}--------\n')

    if player1.selected_item:
        eval(f'FS_Engine.{FS_Engine.consumableact[player1.selected_item.name]}(player1)')

        if player1.selected_item.name in player1.consumable:
            del player1.consumable[player1.selected_item.name]
    
    if player1.selected_item:
        if player2.selected_item == None:
            input('Press ENTER to continue.')
        else:
            pass
    else:
        pass

    if player2.selected_item:
        eval(f'FS_Engine.{FS_Engine.consumableact[player2.selected_item.name]}(player2)')

        if player2.selected_item.name in player2.consumable:
            del player2.consumable[player2.selected_item.name]
        input('Press ENTER to continue.')

    player1.consumable_update()
    player2.consumable_update()

    if player1.spd==player2.spd:
        player1.initiative,player2.initiative=False,False
        choice = random.choice(player_list)
        choice.initiative=True
    else:
        if player1.spd>player2.spd:
            player1.initiative=True
            player2.initiative=False
        if player1.spd<player2.spd:
            player1.initiative=False
            player2.initiative=True
    os.system('cls')
    print(f'--------Turn:{turn}--------\n')

    if player1.initiative:
        if player1.selected_atk:
            print('Player 1:')
            eval(f'FS_Engine.{FS_Engine.f_action[player1.selected_atk.name]}(player1,player2)')
            if player2.selected_atk == None:
                input('Press ENTER to continue.')
            else:
                pass
        if player2.HP <= 0:
            if player2.selected_atk:
                input('Press ENTER to continue.')
            break
        else:
            pass
        if player2.selected_atk:
            print('Player 2:')
            eval(f'FS_Engine.{FS_Engine.f_action[player2.selected_atk.name]}(player2,player1)')
            input('Press ENTER to continue.')
            if player1.HP <= 0:
                break
            else:
                pass

    else:
        if player2.selected_atk:
            print('Player 2:')
            eval(f'FS_Engine.{FS_Engine.f_action[player2.selected_atk.name]}(player2,player1)')
            if player1.selected_atk == None:
                input('Press ENTER to continue.')
            else:
                pass
        if player1.HP <= 0:
            if player2.selected_atk:
                input('Press ENTER to continue.')
            break
        else:
            pass
        if player1.selected_atk:
            print('Player 1:')
            eval(f'FS_Engine.{FS_Engine.f_action[player1.selected_atk.name]}(player1,player2)')
            input('Press ENTER to continue.')
            if player2.HP <= 0:
                break
            else:
                pass

    if player1.burning==True or player2.burning==True or player1.deflecting==True or player2.deflecting==True:
        if player1.initiative:
            os.system('cls')
            print('\nPlayer 1:')
            player1.update()
            print('\nPlayer 2:')
            player2.update()
            time.sleep(2)
        else:
            os.system('cls')
            print('\nPlayer 2:')
            player2.update()
            print('\nPlayer 1:')
            player1.update()
            time.sleep(2)
    else:
        pass

os.system('cls')
if player1.HP <= 0:
    print("\nPlayer 1's kingdom falls.\nTotal victory to Player 2!\n*fireworks*\n*fireworks*\n")
elif player2.HP <= 0:
    print("\nPlayer 2's kingdom falls.\nTotal victory to Player 1!\n*fireworks*\n*fireworks*\n")
else:
    print('\nCombat Error #6969420:\nIf you get this error I (The Developer) know the issue and how to fix it.')
    print('However, no one should get this error unless something went terribly wrong.')
    print('If you are reading this after looking at my code.\nThank you for being interested in my game!')
