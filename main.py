from gameClasses import Item, Entity, Dice
import time

sword = Item("sword", damage=2)
shield = Item("shield", defence=3)
healing = Item("healing", healing=3, durability=1)


def playGame(ent1_is_bot:bool, ent2_is_bot:bool)->None:

    player1 = Entity("player1", 20, isBot=ent1_is_bot)
    player1.give(sword, shield, healing)
    player1.equip(sword)

    player2 = Entity("player2", 20, isBot=ent2_is_bot)
    player2.give(sword, shield, healing)
    player2.equip(sword)

    print(player1)
    print(player2)

    players = [player1, player2]

    i = 0
    while len(players) > 1:
        i += 1
        print(f"ход {i}")
        print('-'*10)
        for i in range (len(players)):
            ent1 = players[i]
            ent2 = players[(i+1)%len(players)]

            message = ''
            for i, j in enumerate(ent1.inventory):
                message += f'\n{i+1} -> {j.name}'

            console_input = '0'
            if not ent1.isBot:
                while console_input not in list(str(i+1) for i in range(len(ent1.inventory))):
                    print(f"""chose: {message}""")
                    console_input = input()
                ent1.equip(ent1.inventory[int(console_input)-1])

            print (f"{ent1.name} confronts {ent2.name}")
            print (f"{ent1.name} uses {ent1.arm_slot[0].name}")

            dice_roll = Dice(20).throw()
            print(f'{dice_roll}')
            time.sleep(0.5)

            damage_amount = int(ent1.arm_slot[0].damage * dice_roll/10 / ent2.arm_slot[0].defence)
            if damage_amount != 0:
                ent2.takeDamage(damage_amount)
                print(f"""{ent1.name} with 
                    dice roll: {dice_roll}, 
                    {ent1.arm_slot[0].__str__()} 
                    gives {damage_amount} damage to
                    {ent2.name} with
                    {ent2.arm_slot[0].__str__()}  
                    {ent2.name} health: {ent2.health}""")
            
            heal_amount = int(ent1.arm_slot[0].healing * dice_roll/10)
            if heal_amount != 0:
                ent1.takeDamage(-heal_amount)
                print(f"""{ent1.name} healed {heal_amount} hp with
                      {ent1.arm_slot[0].healing} 
                      up to {ent1.health} health""")
                
            ent1.arm_slot[0].durability -= 1    
            if ent1.arm_slot[0].durability <= 0:
                print(ent1.arm_slot[0].name +" broke")
                ent1.inventory.remove(ent1.arm_slot[0])

            if ent2.health <= 0:
                players.remove(ent2)
                print(f'{ent2.name} died')
            if len(players) == 1:
                print(f'{players[0].name} wins!')
                break




if __name__ == "__main__":

    print("""select game mode:
          1 -> bvb
          2 -> pvb
          3 -> pvp""")
    console_input = input()
    match console_input:
        case '1': playGame(True, True)
        case '2': playGame(False, True)
        case '3': playGame(False, False)
