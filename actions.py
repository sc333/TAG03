#!/usr/bin/python

import random
import time
from data import *

def inventory(light,ion,laser,oxy,trnsprt,suit,wealth):
    """Supply Android"""
    if wealth == 0:
        print " YOU HAVE NO MONEY"
        delay(2)
        print CLRSCR
        return light,ion,laser,oxy,trnsprt,suit,wealth
    print " A SUPPLY ANDROID HAS ARRIVED" 
    choice=["0","1","2","3","4","5","6"]
    while choice != "0":
        if wealth == 0:
            print " YOU HAVE NO SOLARIAN CREDITS LEFT"
            delay(2)
            print CLRSCR
            break 
        else:
            print "\n YOU HAVE $%d IN SOLARIAN CREDITS" % wealth
            print "\n\n"
        print \
        """
 YOU CAN BUY  1 - NUCLEONIC LIGHT ($15)
              2 - ION GUN ($10)
              3 - LASER ($20)
              4 - OXYGEN ($2 PER UNIT)
              5 - MATTER TRANSPORTER ($30)
              6 - COMBAT SUIT ($50)
              0 - TO CONTINUE EXPLORATION """
        buy = raw_input(" ENTER NO. OF ITEM REQUIRED? ")
        if buy not in choice:
            continue
        if buy == "0":
            print CLRSCR
            break
        if buy == "1":
            light = 1
            wealth -= 15
        if buy == "2":
            ion = 1
            wealth -= 10
        if buy == "3":
            laser = 1
            wealth -= 20
        if buy == "5":
            trnsprt = 1
            wealth -= 30
        if buy == "6":
            suit = 1
            wealth -= 50
        if wealth < 0:
            print " YOU HAVE TRIED TO CHEAT ME!"
            print " YOU HAVE NO MONEY"
            delay(2)
            wealth=0;suit=0;light=0;ion=0;laser=0;trnsprt=0;oxy=int(oxy/4)
            print CLRSCR
            return light,ion,laser,oxy,trnsprt,suit,wealth
        if buy == "4":
            if oxy > 0:
                print " YOU HAVE %d UNITS OF OXYGEN" % oxy
            units = raw_input(" HOW MANY UNITS OF OXYGEN? ")
            units = int(units)
            if 2 * units > wealth:
                print " YOU HAVEN'T GOT ENOUGH MONEY."
            oxy += units
            wealth -= 2 * units
        print
    return light,ion,laser,oxy,trnsprt,suit,wealth

def replenishOxy(oxy,strength):
    """[B]reathe"""
    print CLRSCR
    if oxy < 1:
        return oxy,strength
    while oxy > 0:
        print " YOU HAVE",oxy,"UNITS OF OXYGEN LEFT"
        units = raw_input(" HOW MANY DO YOU WANT TO ADD TO YOUR TANKS? ")
        units = int(units)
        if units > oxy:
            continue
        else:
            break
        delay(1)
    strength = strength + (5 * units)
    oxy = oxy - units
    print CLRSCR
    return oxy,strength

def fight(mK,fF,droid,strength,ion,laser,suit):
    """
    part 1 - fight preparation
    """
    if fF == 5: 
        droid = "BERSERK ANDROID"
    if fF == 10: 
        droid = "DERANGED DEL-FIEVIAN"
    if fF == 15: 
        droid = "RAMPAGING ROBOTIC DEVICE"
    if fF == 20: 
        droid = "SNIGGERING GREEN ALIEN"
    print
    print " IT IS A %s" % droid
    print
    print " YOUR PERSONAL DANGER METER REGISTERS %d!!" % fF
    print
    delay(1)
    return mK,fF,droid,strength,ion,laser,suit

def battle(mK,fF,droid,strength,ion,laser,suit):
    #print "\n ------------------------------------\n"
    raw_input(" PRESS ENTER KEY TO FIGHT\n")
    #print CLRSCR
    if suit > 0:
        print " YOUR SPACE-ARMOR INCREASES YOUR CHANCE OF SUCCESS"
        fF=(3*(int(fF/4)))
        delay(1.5)
        #print CLRSCR
    for i in range(0,6): 
        print" *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*"
    if ion == 0 and laser == 0:
        print " YOU HAVE NO WEAPONS"
        print " YOU MUST FIGHT WITH BARE HANDS!"
        print
        fF=int(fF+(fF/5))
        delay(1)
    if ion == 1 and laser == 0:
        print " YOU ONLY HAVE AN ION GUN TO FIGHT WITH."
        print
        fF=(4*(int(fF/5)))
    if ion == 0 and laser == 1:
        print " YOU MUST FIGHT WITH YOUR LASER."
        print
        fF=(3*(int(fF/4)))
        delay(1)
    if ion == 1 and laser == 1:
        z=""
        while z != "1" and z != "2":
            z = raw_input(" WHICH WEAPON? 1 - ION GUN, 2 - LASER ")
            print
            if z == "1": 
                fF=(4*(int(fF/5)))
                break
            if z == "2": 
                fF=(3*(int(fF/4)))
                break
    """
    part 2 - the battle: fight droid
    """
    while True:
        if random.random() > .5:
            print
            print " %s ATTACKS" % droid
        else:
            print " YOU ATTACK"
        delay(2)
    
        if random.random() > .5:
            print
            print " YOU GIVE THE %s A GLANCING BLOW." % droid
            fF=int(5*(fF/6))
        else:
            print
            print " THE %s WOUNDS YOU." % droid
            strength -= 5
            
        attack = random.randint(0,100)
        if random.random() > .35:
            continue
        else:
            break

    """part 3 - fight aftermath"""
    if random.random()*16 > fF:
        print
        print " AND YOU MANAGED TO KILL THE %s" % droid
        print 
        print
        mK += 1
    else:
        print
        print " THE %s SERIOUSLY WOUNDS YOU" % droid 
        print 
        print
        strength = int(strength/2)
    fF = 0
    delay(2)
    return mK,fF,droid,strength,ion,laser,suit

