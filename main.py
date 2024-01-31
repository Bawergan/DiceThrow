from gameClasses import Item, Entity, Dice
import time

sword = Item("sword", damage=2)
shield = Item("shield", defence=3)
healing = Item("healing", healing=3, durability=1)

def generatePlayers(player_types):
    players = []
    bot_counter = 0
    player_counter = 0
    for ptype in player_types:
        if ptype == 'b': 
            bot_counter += 1
            name = f'bot{bot_counter}'
        if ptype == 'p':
            player_counter += 1
            name = f'player{player_counter}'
        print(name)
        players.append(Entity(name, 20, isBot=ptype=="b"))
    print(f'added {bot_counter} bots, {player_counter} players')
    return players

def startGameLoop(players, instaDice = False):
    order = 0
    move = 0
    while len(players) > 1:
        if order % len(players) == 0:
            move += 1

            print(f"ход {move}")
            print('-'*10)

        ent1 = players[order%len(players)]
        ent2 = players[(order+1)%len(players)]

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

        dice_roll = Dice(20).throw(instaDice)
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
        
        order += 1


if __name__ == "__main__":

    print("""choose your players, b for bot, p for player""")
    console_input = input()

    players = generatePlayers(console_input)
    for player in players:
        player.give(sword, shield, healing)
        player.equip(sword)

    startGameLoop(players, True)