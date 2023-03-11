import random
import mymodule
random_number = random.randint(1,10)
print(random_number)
print(mymodule.pi)
random_float = random.random()  ## It will generate the number in between 0 & 1 not including 1 
print(random_float)
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")