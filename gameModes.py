from gameClasses import Item, Entity, Dice


sword = Item("sword", 2, 1)
shield = Item("shield", 1, 3)


def playGame(ent1_is_bot:bool, ent2_is_bot:bool)->None:

    player = Entity("player1", 20, isBot=ent1_is_bot)
    player.give(sword, shield)
    player.equip(sword)

    bot = Entity("player2", 20, isBot=ent2_is_bot)
    bot.give(sword, shield)
    bot.equip(sword)

    print(player)
    print(bot)

    players = [player, bot]

    i = 0
    while len(players) > 1:
        i += 1
        print(f"ход {i}")
        print('-'*10)
        for i in range (len(players)):
            ent1 = players[i]
            ent2 = players[(i+1)%len(players)]

            if not ent1.isBot:
                print("""chose:
                    1 -> sword
                    2 -> shield""")
                
                console_input = input()

                match console_input:
                    case "1": ent1.equip(sword)
                    case "2": ent1.equip(shield)

            print (f"{ent1.name} atacks {ent2.name}")
            dice_roll = Dice(20).throw()
            print(f'dice rolled on {dice_roll}')
            damage_amount = int(ent1.arm_slot[0].damage * dice_roll/10)
            ent2.takeDamage(damage_amount)
            print(f"{ent2.name} takes {damage_amount} damage")
            print(f'health: {ent2.health}')

            if ent2.health <= 0:
                players.remove(ent2)
                print(f'{ent2.name} died')
            if len(players) == 1:
                print(f'{players[0].name} wins!')
                break