#!/usr/bin/python

import random
import time

CLRSCR = "\n"*50

def delay(seconds):
    time.sleep(seconds)

def instructions():
    print CLRSCR
    print " HELLO EXPLORER!"
    print \
    """
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 ENTER ONE OF THE FOLLOWING KEYS TO PLAY THE GAME:
   
 [N] = NORTH    [E] = EAST    [U] = UP      [P] = PICK-UP
 [S] = SOUTH    [W] = WEST    [D] = DOWN    [I] = INVENTORY
 [F] = FIGHT    [R] = RUN     [M] = MAGIC   [C] = CONSUME
 [Q] = QUIT     [H] = HELP    [?] = HELP 
     
 GOOD LUCK!
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n
     """
     
numD = 6
directionTable=[["N","\n NO EXIT THAT WAY"],
                ["S","\n THERE IS NO EXIT SOUTH"],
                ["E","\n YOU CANNOT GO IN THAT DIRECTION"],
                ["W","\n YOU CANNOT MOVE THROUGH SOLID STONE"],
                ["U","\n THERE IS NO WAY UP FROM HERE"],
                ["D","\n YOU CANNOT DESCEND FROM HERE"]]

# Set up the Travel Table
#             N S E W U D T        
travelTable=[[0,5,2,0,0,0,0],       # ROOM 1
             [0,0,0,1,0,0,0],       # ROOM 2
             [3,7,4,3,3,3,0],       # ROOM 3
             [0,0,0,3,0,0,0],       # ROOM 4
             [1,5,7,5,5,5,0],       # ROOM 5 
             [6,6,6,6,6,6,0],       # ROOM 6
             [3,0,8,5,0,0,0],       # ROOM 7
             [8,12,8,7,8,8,0],      # ROOM 8
             [11,13,10,0,0,0,0],    # ROOM 9 
             [0,14,0,9,0,0,0],      # ROOM 10
             [9,6,6,6,6,6,0],       # ROOM 11
             [8,16,19,0,0,0,0],     # ROOM 12 
             [13,0,0,13,0,13,0],    # ROOM 13
             [10,0,15,17,0,18,0],   # ROOM 14
             [0,0,0,14,0,19,0],     # ROOM 15
             [12,16,16,18,16,16,0], # ROOM 16
             [14,0,18,0,0,0,0],     # ROOM 17
             [0,0,16,17,14,0,0],    # ROOM 18 
             [0,12,0,0,15,0,0]]     # ROOM 19  

# Distribute the treasure 
cnt = 0
while cnt <= 3:
        room = int(random.random()*19)+1
        if room == 6: 
            continue
        if room == 11: 
            continue
        if room == 13:
            continue
        if travelTable[room-1][6] != 0:
            continue
        b = range(10,110)
        treasure = random.choice(b)
        travelTable[room-1][6] = treasure
        cnt += 1
        
# Place monsters in rooms
cnt = 4
while cnt > 0:
        room = int(random.random()*19)+1
        if room == 6: 
            continue
        if room == 11: 
            continue
        if room == 13:
            continue
        if travelTable[room-1][6] != 0:
            continue
        travelTable[room-1][6] = -cnt
        cnt -= 1

# Put treasure in the Private Meeting Room and the Treasury. 
# These lines overwrite anything else which has been placed there:
a = range(1,99)
travelTable[3][6]= 100 + random.choice(a)
travelTable[15][6]= 100 + random.choice(a)

def roomDescriptions(roomNum):
    print
    print
    print " **************************"
    print
    print
    if roomNum == 1: room1()
    if roomNum == 2: room2() 
    if roomNum == 3: room3()
    if roomNum == 4: room4() 
    if roomNum == 5: room5() 
    if roomNum == 6: room6()
    if roomNum == 7: room7() 
    if roomNum == 8: room8() 
    if roomNum == 9: room9()
    if roomNum == 10: room10() 
    if roomNum == 11: room11() 
    if roomNum == 12: room12()
    if roomNum == 13: room13() 
    if roomNum == 14: room14() 
    if roomNum == 15: room15()
    if roomNum == 16: room16() 
    if roomNum == 17: room17() 
    if roomNum == 18: room18()
    if roomNum == 19: room19()
    return roomNum

def room1():
    print " YOU ARE IN THE FORMER RECREATION"
    print " CENTER. EQUIPMENT FOR MUSCLE-TRAINING"
    print " IN ZERO GRAVITY LITTERS THE AREA"
    print

def room2():
    print " THIS WAS THE REPAIR AND MAINTENANCE"
    print " HOLD OF THE SHIP. YOU CAN ONLY LEAVE IT"
    print " VIA THE GIANT HANGAR DOOR TO THE WEST"
    print

def room3():
    print " YOU ARE IN THE WRECKED HOLD OF A SPACESHIP"
    print " THE CAVERNOUS INTERIOR IS LITTERED WITH"
    print " FLOATING WRECKAGE, AS IF FROM SOME"
    print " TERRIBLE EXPLOSION EONS AGO......"
    print

def room4():
    if random.random() > 0.6:
        print " WHAT A SUPERB SIGHT......."
    print " THE VIEW OF THE STARS FROM THIS OBSERVATION"
    print " PLATFORM IS MAGNIFICENT, AS FAR AS THE EYE"
    print " CAN SEE. THE SINGLE EXIT IS BACK WHERE YOU"
    print " CAME FROM"
    print

def room5():
    print " ACRE UPON ACRE OF DRIED-UP HYDROPONIC"
    print " PLANT BEDS STRETCH AROUND YOU.  ONCE THIS"
    print " AREA FED THE THOUSAND ON BOARD THE SHIP"
    if random.random() > 0.5:
        print " THE SOLAR LAMPS ARE STILL SHINING"
    if random.random() > 0.5:
        print " A FEW PLANTS ARE STILL ALIVE TO THE EAST"
    print

def room6():
    pass

def room7():
    print " YOU ARE IN THE CREW'S SLEEPING QUARTERS"
    print " "
    print " "
    if random.random() > 0.5:
        print " MOST OF THE SLEEPING SHELLS ARE EMPTY"
    if random.random() > 0.5:
        print " THE FEW REMAINING CREW STIR FITFULLY"
        print " IN THEIR ENDLESS, DREAMLESS SLEEP"
    if random.random() > 0.7:
        print " THERE ARE EXITS TO THE NORTH, EAST AND WEST"
    print

def room8():
    print " THE FORMER PASSENGER SUSPENDED ANIMATION DORMITORY..."
    if random.random() > 0.5:
        print " PASSENGERS FLOAT BY AT RANDOM"
    if random.random() > 0.5:
        print " IT IS ENORMOUS, IT SEEMS TO GO ON FOREVER"
    if random.random() > 0.9:
        print " THE ONLY EXITS ARE TO THE WEST AND SOUTH"
    print

def room9():
    print " THIS IS THE SHIP'S HOSPITAL, WHITE AND STERILE."
    print " A BUZZING SOUND, AND A STRANGE WARMTH COME FROM"
    print " THE SOUTH, WHILE A CHILL IS FELT TO THE NORTH"
    print

def room10():
    print " FOOD FOR ALL THE CREW WAS PREPARED IN THIS"
    print " GALLEY. THE REMAINS FROM PREPARATIONS OF"
    print " FINAL MEAL CAN BE SEEN. DOORS LEAVE THE"
    print " GALLEY TO THE SOUTH AND TO THE WEST"
    print

def room11():
    print " AHA...THAT LOOKS LIKE THE SPACE POD"
    print " NOW, AND ITS OUTSIDE DIALS"
    print " INDICATE IT IS STILL IN PERFECT CONDITION."
    return

def room12():
    if random.random() > 0.5:
        print " THIS IS THE SHIP'S MAIN NAVIGATION ROOM"
    print " STRANGE MACHINERY LINES THE WALLS, WHILE"
    print " OVERHEAD, A HOLOGRAPHIC STAR MAP SLOWLY TURNS"
    print " BY THE FLICKERING GREEN LIGHT YOU CAN JUST"
    print " MAKE OUT EXITS"
    if random.random() > 0.8:
        print " TO THE SOUTH AND TO THE EAST"
    print

def room13():
    if random.random() > 0.5:
        print " YOUR BODY TWISTS AND BURNS..."
    print " YOU ARE CAUGHT IN A DEADLY RADIATION FIELD"
    print " SLOWLY YOU REALISE THIS IS THE END"
    if random.random() > 0.5:
        print " NO MATTER WHAT YOU DO"
    if random.random() > 0.5:
        print " YOU ARE DOOMED TO DIE HERE"
    print

def room14():
    print " THIS IS THE POWER CENTER OF THE SHIP"
    print " THE CHARACTERISTIC BLUE METAL LIGHT"
    print " OF THE STILL-FUNCTIONING ION DRIVE"
    print " FILLS THE ENGINE ROOM. THROUGH THE"
    print " HAZE YOU CAN SEE DOORS"
    if random.random() > 0.9:
        print " TO THE NORTH AND WEST"
    if random.random() > 0.6:
        print " A SHAFT LEADS DOWNWARDS TO THE REPAIR CENTER"
    print

def room15():
    print " YOU ARE STANDING IN THE ANDROID STORAGE HOLD"
    print " ROW UPON ROW OF METAL MEN STAND STIFFLY AT"
    print " ATTENTION, AWAITING THE DISTINCTIVE SOUND OF"
    print " THEIR LONG-DEAD CAPTAIN TO SET THEM INTO MOTION"
    print " A LIGHT COMES FROM THE WEST AND THROUGH THE"
    print " GRAVITY WELL SET INTO THE FLOOR"
    print

def room16():
    print " ANOTHER CAVERNOUS, SEEMINGLY ENDLESS HOLD,"
    print " THIS ONE CRAMMED WITH GOODS FOR TRADING..."
    if random.random() > 0.7:
        print " RARE METALS AND VENUSIAN SCULPTURES"
    if random.random() > 0.8:
        print " PRESERVED SCALAPIAN DESERT FISH"
    if random.random() > 0.7:
        print " FLASHING EBONY SCITH STONES FROM XARIAX IV"
    if random.random() > 0.8:
        print " AWESOME TRADER ANT EFIGIES FROM THE QWERTYIOPIAN EMPIRE"
    if random.random() > 0.9:
        print " THE LIGHT IS STRONGER TO THE WEST"
    print

def room17():
    print " A STARK, METALLIC ROOM, REEKING OF LUBRICANTS"
    print " WEAPONS LINE THE WALL, RANK UPON RANK. EXITS FOR"
    print " SOLDIER ANDROIDS ARE TO THE NORTH AND THE EAST"
    print

def room18():
    print " ABOVE YOU IS THE GRAVITY SHAFT LEADING TO "
    print " THE ENGINE ROOM. THIS IS THE SHIP REPAIR "
    print " CENTER WITH EMERGENCY EXITS TO THE SOLDIER "
    print " ANDROIDS STORAGE AND TO THE TRADING GOODS HOLD "
    print

def room19():
    print " YOU'VE STUMBLED ON THE SECRET COMMAND CENTER "
    print " WHERE SCREENS BRING VIEWS FROM ALL AROUND "
    print " THE SHIP. THERE ARE TWO EXITS........"
    if random.random() > 0.5:
        print " ONE OF WHICH IS THE GRAVITY WELL" 
    else:
        print " ONE OF WHICH LEADS TO THE GOODS HOLD"
    print

