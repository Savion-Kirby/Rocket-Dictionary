# Savion Kirby - Python Dictionary Project
loop = 0
while loop == 0:  # start of the while loop
    # dictionary
    rockets = {
        "Redstone":  {'Class': 'Sub Orbital', 'First Flight': 1953, 'Last Flight': 1961},
        'Atlas LV-3B': {'Class': 'Small Lift', 'First Flight': 1960, 'Last Flight': 1963},
        'Titan II': {'Class': 'Medium Lift', 'First Flight': 1962, 'Last Flight': 2003},
        'Saturn V': {'Class': 'Super Heavy Lift', 'First Flight': 1967, 'Last Flight': 1973},
        'Soyuz': {'Class': 'Medium Lift', 'First Flight': 1967, 'Last Flight': 'still in operation'},
        'N1/L3': {'Class': 'Super Heavy Lift', 'First Flight': 1969, 'Last Flight': 1972},
        'Space Shuttle': {'Class': 'Heavy Lift', 'First Flight': 1981, 'Last Flight': 2011},
        'Delta II': {'Class': 'Medium Lift', 'First Flight': 1989, 'Last Flight': 2018},
        'Delta III': {'Class': 'Medium Lift', 'First Flight': 1998, 'Last Flight': 2000},
        'Ariane 5': {'Class': 'Heavy Lift', 'First Flight': 1996, 'Last Flight': 'still in operation'},
        'Atlas III': {'Class': 'Medium Lift', 'First Flight': 2000, 'Last Flight': 2005},
        'Falcon 9': {'Class': 'Medium Lift', 'First Flight': 2015, 'Last Flight': 'still in operation'},
    }

    list = [] # defining the list
    for key in rockets:
        list.append(key) # putting keys into the list 
    list.insert(0, 'Rocket Keys:') #modifying the list
    list.insert(13, 'End of List')

    # primary selction
    print('Rocket Dictionary')
    print('Choose a rocket:')
    print('1 - Redstone')
    print('2 - Titan II')
    print('3 - Saturn V')
    print('4 - Soyuz')
    print('5 - N1/L3')
    print('6 - Space Shuttle')
    print('7 - Delta II')
    print('8 - Delta III')
    print('9 - Ariane 5')
    print('10 - Atlas III')
    print('11 - Falcon 9')

    choice = 0 # the first choice of the rocket
    subchoice = 0

    choice = int(input('Type the coresponding number...'))
    if choice < 1 or choice > 11:
        print ()
        print('Invalid Option')
    
    def opperation(key): #solving operation years method
        oppyears = int(rockets[key]["Last Flight"]) - int(rockets[key]["First Flight"])
        mod = (10%2) 
        return oppyears
    
    if choice == 1:  # Redstone
        key = 'Redstone'
        oppyears = opperation(key)
        print()
        print('Redstone')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5: #error checking
            print ()
            print('Invalid Option')  
        if subchoice == 1:
            print()
            print('The Redstone is classified as a',
                  rockets['Redstone']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('The Restone first flew in',
                  rockets['Redstone']['First Flight'])
        if subchoice == 3:
            print()
            print('The Restone last flew in',
                  rockets['Redstone']['Last Flight'])
        if subchoice == 4:
            print()
            REDanswer = int(input('What was the year did the Redstone rocket first fly?'))
            if REDanswer == 1953:
                print()
                print('Your answer is correct')
                rockets['Redstone']['TAnswer'] = REDanswer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Redstone']['TAnswer'] = REDanswer
        if subchoice == 5:
            print()
            print('Years in opperation:', oppyears) 

    if choice == 2:  # Titan II
        key = 'Titan II'
        oppyears = opperation(key)
        print()
        print('Titan II')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5:#error checking
            print ()
            print('Invalid Option')
        if subchoice == 1:
            print()
            print('The Titan II is classified as a',
                  rockets['Titan II']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('The Titan II first flew in',
                  rockets['Titan II']['First Flight'])
        if subchoice == 3:
            print()
            print('The Titan II last flew in',
                  rockets['Titan II']['Last Flight'])
        if subchoice == 4:
            print()
            TITanswer = int(input('What was the last year the Titan II booster flew?'))
            if TITanswer == 2003:
                print()
                print('Your answer is correct')
                rockets['Titan II']['TAnswer'] = TITanswer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Titan II']['TAnswer'] = TITanswer
        if subchoice == 5:
            print()
            print('Years in opperation:', oppyears) 

    if choice == 3:  # Saturn V
        key = 'Saturn V'
        oppyears = opperation(key)
        print()
        print('Saturn V')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5: #error checking
            print ()
            print('Invalid Option')
        if subchoice == 1:
            print()
            print('The Saturn V is classified as a',
                  rockets['Saturn V']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('The Saturn V first flew in',
                  rockets['Saturn V']['First Flight'])
        if subchoice == 3:
            print()
            print('The Saturn V last flew in',
                  rockets['Saturn V']['Last Flight'])
        if subchoice == 4:
            print()
            SATanswer = int(input('How many times did the Saturn V launch?'))
            if SATanswer == 13:
                print()
                print('Your answer is correct')
                rockets['Saturn V']['TAnswer'] = SATanswer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Saturn V']['TAnswer'] = SATanswer
        if subchoice == 5:
            print()
            print('Years in opperation:', oppyears) 

    if choice == 4:  # Soyuz
        
        print()
        print('Soyuz')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please type the coresponding number....'))
        if subchoice < 1 or subchoice > 5: #error checking
            print ()
            print('Invalid Option')
        if subchoice == 1:
            print()
            print('Soyuz is classified as a',
                  rockets['Soyuz']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('Soyuz first flew in', rockets['Soyuz']['First Flight'])
        if subchoice == 3:
            print()
            print('Soyuz is', rockets['Soyuz']['Last Flight'])
        if subchoice == 4:
            print()
            SOYanswer = int(input('How may astronauts can the Soyuz carry to the ISS at once?'))
            if SOYanswer == 3:
                print()
                print('Your answer is correct')
                rockets['Soyuz']['TAnswer'] = SOYanswer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Soyuz']['TAnswer'] = SOYanswer
        if subchoice == 5:
            print()
            print('Soyuz is still in operation') 

    if choice == 5:  # N1/L3
        key = 'N1/L3'
        oppyears = opperation(key)
        print()
        print('N1/L3')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice == 1:
            print()
            print('The N1 is classified as a',
                  rockets['N1/L3']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('The N1 first flew in', rockets['N1/L3']['First Flight'])
        if subchoice == 3:
            print()
            print('The N1 last flew in', rockets['N1/L3']['Last Flight'])
        if subchoice == 4:
            print()
            N1answer = int(input('How many times did the N1 blow up?'))
            if N1answer == 4:
                print()
                print('Your answer is correct')
                rockets['N1/L3']['TAnswer'] = N1answer
            else:
                print()
                print('Your answer is incorrect')
                rockets['N1/L3']['TAnswer'] = N1answer
        if subchoice == 5:
            print()
            print('Years in opperation:', oppyears) 
                
    if choice == 6:  # Space Shuttle
        key = 'Space Shuttle'
        oppyears = opperation(key)
        print()
        print('Space Shuttle')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5: #error checking
            print ()
            print('Invalid Option')
        if subchoice == 1:
            print()
            print('The Space Shuttle is classified as a',
                  rockets['Space Shuttle']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('The Space Shuttle first flew in',
                  rockets['Space Shuttle']['First Flight'])
        if subchoice == 3:
            print()
            print('The Space Shuttle last flew in',
                  rockets['Space Shuttle']['Last Flight'])
        if subchoice == 4:
            print()
            SSanswer = int(input('How many STS missions are there?'))
            if SSanswer == 135:
                print()
                print('Your answer is correct')
                rockets['Space Shuttle']['TAnswer'] = SSanswer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Space Shuttle']['TAnswer'] = SSanswer
        if subchoice == 5:
            print()
            print('Years in opperation:', oppyears) 

    if choice == 7:  # Delta II
        key = 'Delta II'
        oppyears = opperation(key)
        print()
        print('Delta II')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5:
            print ()
            print('Invalid Option')
        if subchoice == 1:
            print()
            print('The Delta II is classified as a',
                  rockets['Delta II']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('The Delta II first flew in',
                  rockets['Delta II']['First Flight'])
        if subchoice == 3:
            print()
            print('The Delta II last flew in',
                  rockets['Delta II']['Last Flight'])
        if subchoice == 4:
            print()
            DEL2answer = int(input("What is the maximum nunber of SRB's the Delta II used?"))
            if DEL2answer == 9:
                print()
                print('Your answer is correct')
                rockets['Delta II']['TAnswer'] = DEL2answer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Delta II']['TAnswer'] = DEL2answer
        if subchoice == 5:
            print()
            print('Years in opperation:', oppyears) 

    if choice == 8:  # Delta III
        key = 'Delta III'
        oppyears = opperation(key)
        print()
        print('Delta III')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5: #error checking
            print ()
            print('Invalid Option')
        if subchoice == 1:
            print()
            print('The Delta III is classified as a',
                  rockets['Delta III']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('The Delta III first flew in',
                  rockets['Delta III']['First Flight'])
        if subchoice == 3:
            print()
            print('The Delta III last flew in',
                  rockets['Delta III']['Last Flight'])
        if subchoice == 4:
            print()
            DEL3answer = int(input("Of its 3 flight, how many times did a lauch failure occur?"))
            if DEL3answer == 2:
                print()
                print('Your answer is correct')
                rockets['Delta III']['TAnswer'] = DEL3answer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Delta III']['TAnswer'] = DEL3answer
        if subchoice == 5:
            print()
            print('Years in opperation:', oppyears) 

    if choice == 9:  # Ariane 5
        print()
        print('Ariane 5')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5: #error checking
            print ()
            print('Invalid Option')
        print()
        if subchoice == 1:
            print()
            print('Ariane 5 is classified as a',
                  rockets['Ariane 5']['Class'], 'vehicle.')
        if subchoice == 2:
            print()
            print('Ariane 5 first flew in',
                  rockets['Ariane 5']['First Flight'])
        if subchoice == 3:
            print()
            print('Ariane 5 is', rockets['Ariane 5']['Last Flight'])
        if subchoice == 4:
            print()
            ARIanswer = int(input("How many SRBs' are used on the Ariane 5?"))
            if ARIanswer == 2:
                print()
                print('Your answer is correct')
                rockets['Ariane 5']['TAnswer'] = ARIanswer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Ariane 5']['TAnswer'] = ARIanswer
        if subchoice == 5:
            print()
            print('Ariane 5 is still in operation')

    if choice == 10:  # Atlas III
        key = 'Atlas III'
        oppyears = opperation(key)
        print()
        print('Atlas III')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5: #error checking
            print ()
            print('Invalid Option')
        print()
        if subchoice == 1:
            print()
            print('The Atlas III is classified as a',
                  rockets['Atlas III']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('The Atlas III first flew in',
                  rockets['Atlas III']['First Flight'])
        if subchoice == 3:
            print()
            print('The Atlas III last flew in',
                  rockets['Atlas III']['Last Flight'])
        if subchoice == 4:
            print()
            ATLanswer = int(input('How many stages did the Atlas III have?'))
            if ATLanswer == 2:
                print()
                print('Your answer is correct')
                rockets['Atlas III']['TAnswer'] = ATLanswer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Atlas III']['TAnswer'] = ATLanswer
        if subchoice == 5:
            print()
            print('Years in opperation:', oppyears) 

    if choice == 11:  # Falcon 9
        print()
        print('Falcon 9')
        print('Select a sub option:')
        print('1 - Vehicle Class')
        print('2 - First Flight')
        print('3 - Last Flight')
        print('4 - Trivia')
        print('5 - Opperation Years') 
        subchoice = int(input('Please tye the coresponding number....'))
        if subchoice < 1 or subchoice > 5: #error checking
            print ()
            print('Invalid Option')
        if subchoice == 1:
            print()
            print('Falcon 9 is classified as a',
                  rockets['Falcon 9']['Class'], 'vehicle')
        if subchoice == 2:
            print()
            print('Falcon 9 first flew in',
                  rockets['Falcon 9']['First Flight'])
        if subchoice == 3:
            print()
            print('The Falcon 9 is', rockets['Falcon 9']['Last Flight'])
        if subchoice == 4:
            print()
            F9answer = int(input('How many engines are used on the first stage of the Falcon 9?'))
            if F9answer == 9:
                print()
                print('Your answer is correct')
                rockets['Falcon 9']['TAnswer'] = F9answer
            else:
                print()
                print('Your answer is incorrect')
                rockets['Falcon 9']['TAnswer'] = F9answer
        if subchoice == 5:
            print()
            print('Falcon 9 is still in operation') 
                
    print()
    print('Would you like to see the modified list of all keys?') #viewing the list
    ukey = str(input("y|n:"))
    print()
    if ukey == "y" or ukey == "Y":
        for i in list:
            print(i, end = ", ")
    print()
    print() 
    print('Would you like to see the whole updated dictionary?') # viewing the updated dictionary
    view = str(input("y|n:"))
    if view == "y" or view == "Y":
        print(rockets)
        print()
        print('Run Again')
    else:
        print('Run Again?') 
    loop = str(input("y|n:")) # while loop
    if loop == "y" or loop == "Y":
        loop = 0
    else:
        loop = 1
        print("Goodbye")
