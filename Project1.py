import math
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

# Player and Rocket Variables
totalcash = 1000 #in $
account = totalcash #in $
fuelw = 700 #in kg/kL
fuelcost = 1830 #in $/kL
fuelburn = 0.025 #in kL/s
weight = 0 #in kg

# Cardboard Variables
cardcost = 50 #in $/m
cardw = 200 #in kg/m**3
cardeff = 0.25 #in %
cardthick = .05 #in m

# PVC Variables
pvccost = 150 #in $/m
pvcw = 1450 #in kg/m**3
pvceff = 0.75 #in %
pvcthick = .025 #in m

# Tubing Variables
tubingcost = 250 #in $/m
tubingw = 7850 #in kg/m**3
tubingeff = 1.00 #in %
tubingthick = .012 #in m

# Random Variables
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Functions
def matreset(): #Written by Aiden
    print(RED + f"You have spent too much money! Please restart selection!" + RESET)
    account = totalcash
    weight = 0
    return weight, account

def legreset(): #Written by Blake
    print(RED + f"Select a number in the interval [0.5, 10] for legnth! Please restart selection!" + RESET)
    account = totalcash
    weight = 0
    return weight, account

def blastoff(): #Written by Sam
    action = input("Hit [Enter] to launch Rocket!")
    for i in range(3,-1,-1):
        print(i,"...")
        sleep(1.05)

def launch(fv, fb, ep, w): #Written by Sam
    burntime = fv/fb
    accel = (ep / (w)) - .98
    VFinal = 0.5 * (accel) * (burntime ** 2)
    position1 = (0.5 * VFinal * burntime)
    return position1, VFinal, burntime

def fuelask(): #Written by Presley
    print(GREEN + f"\nYou still have ${account:.2f}" + RESET)
    percent = float((input(f"Fuel costs ${fuelcost:.2f} per kiloliter and you can have up to {possiblefuel:.2f} kiloliters\nProvide the percent of the volume you want to fill: ")))
    return percent

def intro(): #Written by Alex
    print(f"Welcome to the rocket maker!\nYour goal is to make the rocket go as high as possible for as cheap as possible!\nYou are given ${account} to start off with\nYour Score is calculated based off total height and money saved\nGood Luck!")
    sleep(1.5)

def matask(): #Written by Alex
    mat = input(f"\nPlease select a material - You still have ${account:.2f}\n1) Cardboard costs ${cardcost:.2f} per cubic meter - EFF score of {cardeff:.2f}\n2) PVC costs ${pvccost:.2f} per cubic meter - EFF score of {pvceff:.2f}\n3) Steel costs ${tubingcost:.2f} per cubic meter - EFF score of {tubingeff:.2f}\n")
    return mat

def result(): #Written by Griffin
    print(f"\nYour rocket flew {position1:.2e} meters in {burntime:.2f} seconds before running out of fuel!\nPossessed a final velocity of {VFinal:.2f} meters per second!")
    print(GREEN + f"You got a score of {effscore:.3e}" + RESET)
    print(code)





intro()

# Material and legnth selection
loop1 = True
while loop1:

    mat = matask()

    if "ca" in mat.casefold():
        legnth = float(input(f"Given {mat} costs ${cardcost:.2f} per cubic meter, how long, in meters, do you want the to be?\n"))
        code = "C"

        if 0.5 <= legnth <= 10:
            code += "+" + str(legnth) #This will be given back to the user at the end and can be used as a history of the inputs the user entered
            matthick = cardthick
            radii = legnth / 20
            mateff = cardeff
            volume = (math.pi*(radii**2)*legnth - math.pi*((radii - matthick)**2)*legnth)
            weight += volume * cardw
            account -= cardcost * math.pi*radii*legnth
            
            if account <= 0:
                weight, account = matreset()

            else:    
                totalcash = account
                break
        else:
            weight, account = legreset()

    elif "pv" in mat.casefold():
        legnth = float(input(f"Given {mat} costs ${pvccost:.2f} per cubic meter, how long, in meters, do you want the rocket to be?\n"))
        code = "P"

        if 0.5 <= legnth <= 10:
            code += "+" + str(legnth) #This will be given back to the user at the end and can be used as a history of the inputs the user entered
            matthick = pvcthick
            radii = legnth / 20
            mateff = pvceff
            volume = (math.pi*(radii**2)*legnth - math.pi*((radii - matthick)**2)*legnth)
            weight += volume * pvcw
            account -= pvccost * math.pi*radii*legnth
            
            if account <= 0:
                weight, account = matreset()

            else:    
                totalcash = account
                break

        else:
            weight, account = legreset()
    
    elif "st" in mat.casefold():
        legnth = float(input(f"Given {mat} costs ${tubingcost:.2f} per cubic meter, how long, in meters, do you want the rocket to be?\n"))
        code = "T"

        if 0.5 <= legnth <= 10:
            code += "+" + str(legnth) #This will be given back to the user at the end and can be used as a history of the inputs the user entered
            matthick = tubingthick
            radii = legnth / 20
            mateff = tubingeff
            volume = (math.pi*(radii**2)*legnth - math.pi*((radii - matthick)**2)*legnth)
            weight += volume * tubingw
            account -= tubingcost * math.pi*radii*legnth
            
            if account <= 0:
                weight, account = matreset()

            else:
                totalcash = account    
                break
        
        else:
            weight, account = legreset()
        
    else:
        print(RED + "Please select either Cardboard, PVC, or Steel! Please restart selection!" + RESET)

# fuel fill selection
loop2 = True
while loop2:
    possiblefuel = math.pi*((radii - matthick)**2)*legnth
    percent = fuelask()
    if 1 <= percent <= 100:

        if account <= 0:
            print(RED + f"You have spent too much money! Please restart selection!" + RESET)
        
        else:
            fuelvolume = possiblefuel * (percent / 100)
            account -= fuelcost * fuelvolume
            if account <= 0:
                print(RED + f"You have spent too much money! Please restart selection!" + RESET)
                account = totalcash

            else:
                weight += fuelw * fuelvolume
                code += "+" + str(percent) #This will be given back to the user at the end and can be used as a history of the inputs the user entered
                fuelvolume *= mateff
                enginepower = legnth**0.95 * mateff * (200 * account + 90000)**0.5
                print(f"\nYou now have:\n1) {fuelvolume:.2f} kiloliters of fuel\n2) ${account:.2f} left\n3) Total weight of {weight:.2f}kg\n4) {enginepower:.2e} Newtons engine-power")
                break

    else:
        print(RED + "Please chose a number between 1 and 100!" + RESET)

print("")

blastoff()

stuff = launch(fuelvolume, fuelburn, enginepower, weight)
position1, VFinal, burntime = stuff[0], stuff[1], stuff[2]
effscore = (position1 * account)

result()

# Plot the rocket's trajectory
t = np.linspace(0, burntime, 100)
y = VFinal * t -  9.81 * t**2
plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Rocket Trajectory")
plt.xticks(np.arange(0, burntime/2 + 2, 1))
plt.minorticks_on()
plt.ylim(bottom=0)
plt.show()