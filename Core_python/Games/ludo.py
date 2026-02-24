import random  #Imported random module to generate random numbers

while(True):
    print()
    print("******WELCOME TO LUDO GAME******")
    player_count = int(input("Choose players (2-4) : ")) #This game starts with 2 players

    if (player_count == 2): #For two players
        print("2 players")
        p1_sum = 0 #Player 1
        p2_sum = 0 #Player 2
        while (p1_sum <= 20 and p2_sum <= 20): #If dice total is 20 or greater than 20
            dice = random.randint(1, 6) #To generate random number between 1 to 6
            if (dice == 6 or p1_sum != 0): #Initial count should start with 6 else it will jump to the next player
                p1_sum = p1_sum + dice

            dice = random.randint(1, 6)
            if (dice == 6 or p2_sum != 0):
                p2_sum = p2_sum + dice

            if (p1_sum >= 20):
                print("Player one is winner")
                break         #will break loop & print winner when total is 20 or above
            elif (p2_sum >= 20):
                print("Player two is winner")
                break

    elif (player_count == 3): #For three players
        print("3 players")
        p1_sum = 0 #Player 1
        p2_sum = 0 #Player 2
        p3_sum = 0 #Player 3
        while (p1_sum <= 20 and p2_sum <= 20 and p3_sum <= 20): #If dice total is 20 or greater than 20
            dice = random.randint(1, 6)
            if (dice == 6 or p1_sum != 0): #Initial count should start with 6 else it will jump to the next player
                p1_sum = p1_sum + dice

            dice = random.randint(1, 6)
            if (dice == 6 or p2_sum != 0):
                p2_sum = p2_sum + dice

            dice = random.randint(1, 6)
            if (dice == 6 or p2_sum != 0):
                p3_sum = p3_sum + dice

            if (p1_sum >= 20):
                print("Player one is winner")
                break        #will break loop & print winner when total is 20 or above
            elif (p2_sum >= 20):
                print("Player two is winner")
                break
            elif (p3_sum >= 20):
                print("Player three is winner")
                break

    elif (player_count == 4): #For four players
        print("4 players")
        p1_sum = 0 #Player 1
        p2_sum = 0 #Player 2
        p3_sum = 0 #Player 3
        p4_sum = 0 #Player 4
        while (p1_sum <= 20 and p2_sum <= 20 and p3_sum <= 20 and p4_sum <= 20): #If dice total is 20 or greater than 20
            dice = random.randint(1, 6)
            if (dice == 6 or p1_sum != 0): #Initial count should start with 6 else it will jump to the next player
                p1_sum = p1_sum + dice

            dice = random.randint(1, 6)
            if (dice == 6 or p2_sum != 0):
                p2_sum = p2_sum + dice

            dice = random.randint(1, 6)
            if (dice == 6 or p3_sum != 0):
                p3_sum = p3_sum + dice

            dice = random.randint(1, 6)
            if (dice == 6 or p4_sum != 0):
                p4_sum = p4_sum + dice

            if (p1_sum >= 20):
                print("Player one is winner")
                break          #will break loop & print winner when total is 20 or above
            elif (p2_sum >= 20):
                print("Player two is winner")
                break
            elif (p3_sum >= 20):
                print("Player three is winner")
                break
            elif (p4_sum >= 20):
                print("Player four is winner")
                break