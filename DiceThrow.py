from random import randrange
import time
import math

def spinTheNumbers(num_range: int) -> None:
        """
        prints random numbers withing num_range and delets them with variable pouses
        """
        curentNumber, prevNumber = 0, 0
        num_num=randrange(90,111)

        for i in range (num_num):      
            while curentNumber == prevNumber:
                curentNumber = randrange(num_range)
            prevNumber = curentNumber
            print(curentNumber)
            
            def f(x): return math.pow(x,6)
            time.sleep(0.7*f(i)/f(num_num))
            if i==num_num-1: time.sleep(1)

            print('\033[1A', end='\x1b[2K') 

class Dice:
    def __init__(self, cube_range: int) -> None:
        self.cube_range = cube_range
        self.cube_pos = 0
    
    def throw(self) -> int:
        spinTheNumbers(self.cube_range)
        self.cube_pos = randrange(self.cube_range)
        return self.cube_pos
    
    def instaThrow(self) -> int:
        self.cube_pos = randrange(self.cube_range)
        return self.cube_pos
    
    def __str__(self) -> str:
        return str(self.cube_pos)

class Item:
    def __init__(self, name:str='noname', damage:int=0, defence:int=0) -> None:
        self.name = name
        self.damage = damage
        self.defence = defence
    
    def __str__(self) -> str:
        return f"{self.name}: {self.damage}, {self.defence}"

class Entity:
    def __init__(self, name: str = 'noname', health: int = 0) -> None:
        self.health = health
        self.name = name
        self.inventory = [None]
        self.arm_slot = [None]
    
    def __str__(self) -> str:
        return f"""{self.name}
health: {self.health} 
inventory: {list(item.__str__() for item in self.inventory)}
armslot: {list(item.__str__() for item in self.arm_slot)}"""
    
    def give(self, *items: Item) -> None:
        for item in items:
            self.inventory.append(item)
    
    def equip(self, item:Item) -> None:
        if item not in self.inventory:
            print("item missing")
            return
        self.arm_slot[0]=item

    def takeDamage(self, ammount):
        self.health -= ammount

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
            dice_roll = Dice(20).instaThrow()
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