from random import randrange
import guiInstruments

class Dice:
    def __init__(self, cube_range: int) -> None:
        self.cube_range = cube_range
        self.cube_pos = 0
    
    def throw(self) -> int:
        guiInstruments.spinTheNumbers(self.cube_range)
        self.cube_pos = randrange(self.cube_range)
        return self.cube_pos
    
    def instaThrow(self) -> int:
        self.cube_pos = randrange(self.cube_range)
        return self.cube_pos
    
    def __str__(self) -> str:
        return str(self.cube_pos)

class Item:
    def __init__(self, name:str='noname', damage:int=0, defence:int=1, healing: int = 0, durability: int = 100) -> None:
        self.name = name
        self.damage = damage
        self.defence = defence
        self.healing = healing
        self.durability = durability
    
    def __str__(self) -> str:
        return f"{self.name}: {self.damage}, {self.defence}"

class Entity:
    def __init__(self, name: str = 'noname', health: int = 0, isBot: bool = True) -> None:
        self.health = health
        self.name = name
        self.isBot = isBot
        self.inventory = []
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