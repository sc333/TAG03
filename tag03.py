#!/usr/bin/python

from data import *
from actions import *

def main():
    print CLRSCR 
    #INITIALISE
    roomNum = 3
    strength = int(random.random()*50+75)
    wealth = int(random.random()*50+50)
    oxy = int(random.random()*16)
    tally = 0
    mK = 0 # droids killed
    laser = 0
    trnsprt = 0
    ion = 0
    suit = 0
    light = 0
    player = raw_input(" WHAT IS YOUR NAME, SPACE HERO? ")
    print CLRSCR 
    exploring = True
    while exploring: # main game loop
        #########################################################
        strength -= 5
        if strength <= 10:
            print " WARNING CAPTAIN %s, YOUR STRENGTH" % player
            print " IS RUNNING LOW"
            print " YOU NEED AN OXYGEN BOOST"
            print
        if strength <= 0:
            print " YOU HAVE DIED........."
            break
        #########################################################
        # STATUS AREA
        print " "+ player +", YOUR STRENGTH IS %d" % strength
        if wealth > 0:
            print " YOU HAVE $%d IN SOLARIAN CREDITS" % wealth
        if oxy > 0:
            print " YOUR RESERVE TANKS HOLD",oxy,"UNITS OF OXYGEN."
        if suit > 0:
            print " YOU ARE WEARING BATTLE ARMOR"
        if light>0 or ion>0 or laser>0 or trnsprt>0:
            print " YOU ARE CARRYING",
            if ion > 0:
                print "AN ION GUN",
            if laser > 0:
                print "A LASER",
            if (ion >= 1 or laser >= 1) and trnsprt >= 1:
                print "AND",
            if trnsprt > 0:
                print "THE MATTER TRANSPORTER",
        #########################################################
        if light < 1:
            print " IT IS TOO DARK TO SEE ANYTHING"
            print
        if light > 0:
            roomNum = roomDescriptions(roomNum)
        #########################################################
        # ROOM CONTENTS
        contents = travelTable[roomNum-1][6]
        #########################################################
        # IS MONSTER IN ROOM?
        droid=""
        if contents < 0:
            if contents == -1:
                fF = 5 # ferocity Factor
            elif contents == -2:
                fF = 10
            elif contents == -3:
                fF = 15
            elif contents == -4:
                fF = 20
            print
            print
            print " DANGER...THERE IS DANGER HERE...."
            time.sleep(2)
            mK,fF,droid,strength,ion,laser,suit=fight(mK,fF,droid,strength,ion,laser,suit) 
        #########################################################
        # IS TREASURE IN ROOM?
        if travelTable[roomNum-1][6] > 9:
            print " THERE IS TREASURE HERE WORTH $",travelTable[roomNum-1][6]
        #########################################################
        while True:
            vocabulary=["Q","N","S","E","W","U","D","R","F","I","B","P","M","H","?"]
            print
            move = raw_input(" WHAT DO YOU WANT TO DO? ")
            if move.upper() not in vocabulary:
                continue
            else: break
        print
        print
        print " ------------------------------------"
        print
        #########################################################
        # HELP
        if move.upper() == "H" or move.upper() == "?":
            instructions()
        #########################################################
        # QUIT
        if move.upper() == "Q":
            exploring = False
        #########################################################
        if move.upper() == "R" and travelTable[roomNum-1][6] < 0:
            if random.random() > .7:
                print " NO, YOU MUST STAND AND FIGHT"
                print
                move = "F"
                delay(1)
            else:
                move = raw_input(" WHICH WAY DO YOU WANT TO FLEE? ")
        #########################################################
        # NO MOVE THAT WAY: NSEWUD
        for inx in range(0,numD):
            if move.upper() == directionTable[inx][0] \
                    and travelTable[roomNum-1][inx] == 0:
                print
                print directionTable[inx][1]
                print
        #########################################################
        # NOTHING TO FIGHT
        if move.upper() == "F" and travelTable[roomNum-1][6] > -1:
            print " THERE IS NOTHING TO FIGHT HERE."
            print
        #########################################################
        if move.upper() == "I":
            light,ion,laser,oxy,trnsprt,suit,wealth = inventory(light,ion,laser,oxy,trnsprt,suit,wealth)
        #########################################################
        if move.upper() == "B":
            if oxy > 0:
                oxy, strength = replenishOxy(oxy, strength)
            else:
                print " YOU HAVE NO OXYGEN."
                print
            tally -= 1
        #########################################################
        if move.upper() == "P":
            if travelTable[roomNum-1][6] != 0:
                if light == 0:
                    print " YOU CANNOT SEE WHERE IT IS."
                    print
                else:
                    #print "\n YOU PICK UP THE TREASURE."
                    wealth = wealth + travelTable[roomNum-1][6]
                    travelTable[roomNum-1][6] = 0
            else:
                print " THERE IS NOTHING TO PICK UP HERE."
                print
            tally -= 1
        tally += 1
        #########################################################
        # FIGHT MONSTER
        if move.upper() == "F" and travelTable[roomNum-1][6] < 0:
            mK,fF,droid,strength,ion,laser,suit=battle(mK,fF,droid,strength,ion,laser,suit) 
            travelTable[roomNum-1][6] = fF # this should be ZER0 after fight routines 
        #########################################################
        # MOVE TO ROOM
        for inx in range(0,numD):
            if move.upper() == directionTable[inx][0] \
                    and travelTable[roomNum-1][inx]!=0:
                roomNum = travelTable[roomNum-1][inx]
        #########################################################
        if move.upper() == "M":
            roomNum = random.randint(0,20)
            if move.upper() == "M" and roomNum == 13:
                print " THAT IS NOT POSSIBLE"
            while roomNum == 6 or roomNum == 11:
                roomNum = random.randint(1,20)
        #########################################################
        if roomNum == 6:
            print " YOU ARE FREE. YOU HAVE MADE IT.  YOUR"
            print " POD SAILS FREE INTO SPACE..........."
            print
            delay(2)
            exploring = False
        #########################################################
    strength = strength * 5
    wealth = wealth * 2
    tally = tally * 3
    oxy = 10 * oxy 
    mK = mK * 30
    score = strength+wealth+tally+oxy+mK
    print "\n YOUR SCORE WAS %d" % score

if __name__ == "__main__":
    main()
