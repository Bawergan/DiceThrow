from gameClasses import Item, Entity, Dice

if __name__ == "__main__":
    sword = Item("sword", 2, 1)
    shield = Item("shield", 1, 3)

    player1 = Entity("player1", 20)
    player1.give(sword, shield)
    player1.equip(sword)

    player2 = Entity("player2", 20)
    player2.give(sword, shield)
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