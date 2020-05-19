                                                #Shadowrun Dice Roller
                                                #written by Devon Stinchcombe

        #imports random library         
import random                                                                                               
        #loop statement                                    
while True:     
        #number of sides per die  
    num_sides = 6     
    print('_______________________________________________________________________________________\n')
        # input for total number of dice converted from string to integer
    num_dice = int(input('How many D6? '))
        #relevant integer tracking definitions    
    five_count = 0      
    six_count = 0           
    one_count = 0    
        #generates number of results based on integer input of num_dice
    for i in range(num_dice):       
        #generates random integer between one and num_sides
        result = random.randint(1, num_sides)              
        #adds to relevant number count based on returned values modified by num_dice
        if result == 5:     
            five_count += 1                                            
        elif result == 6:     
            six_count += 1      
        elif result == 1 and num_dice == 1:
            one_count += 1    
        elif result == 1 and num_dice > 1:
            one_count += 1    
        #establish total of fives and sixes for output            
    total = five_count + six_count    
        #outputs glitch condition based on one as a percentage of num_dice 
    if result == 1 and total == 0 and num_dice > 1 and one_count >= num_dice // 2 + num_dice % 2:                                  
        print('\n                                                     *** CRITICAL GLITCH ***')      
    elif result == 1 and total >= 1 and num_dice > 1 and one_count >= num_dice // 2 + num_dice % 2:                                     
        print('\n                                                             *** GLITCH ***')       
        #total count of fives
    if five_count == 1:
        print('\n                                                            You rolled', five_count, 'Five')
    elif five_count > 1:
        print('\n                                                            You rolled', five_count, 'Fives')               
        #total count of sixes
    if six_count == 1:
        print('\n                                                            You rolled', six_count, 'Six')
    elif six_count >1:
        print('\n                                                            You rolled', six_count, 'Sixes')       
        #total count of fives and sixes    
    if total > 1:
        print('\n                                                               ',total,'good rolls')
    elif total == 1:
        print('\n                                                               ',total,'good roll')
    elif total == 0:
        print('\n                                                              No good rolls')
     
     

