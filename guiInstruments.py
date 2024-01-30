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