import random

stay = 0 
switch = 0

for _ in range(100):  
    doors = [0, 0, 1]  
    random.shuffle(doors)  
    user_choice = doors.pop()  
    doors.remove(0)  
    if user_choice == 1:
        stay += 1  
    else:
        switch += 1  

stay, switch
