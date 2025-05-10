# Author: Jean Toussaint
# class: Py
# Date:2/18/25

# Inter Planetary Weight

# Constants

fMERCURY_GRAVITY = 0.38
fVENUS_GRAVITY = 0.91
fMOON_GRAVITY = 0.165
fMARS_GRAVITY = 0.38
fJUPITER_GRAVITY = 2.34
fSATURN_GRAVITY = 0.93
fURANUS_GRAVITY = 0.92
fNEPTUNE_GRAVITY = 1.12
fPLUTO_GRAVITY = 0.066

# step 1 - input & conversions
sName = input("What is your name: ")
nWeight = float(input(f"What is {sName}'s weight: "))



# step 2 - calculate
fWeight1 = fMERCURY_GRAVITY * nWeight
fWeight2 = fVENUS_GRAVITY * nWeight 
fWeight3 = fMOON_GRAVITY * nWeight  
fWeight4 = fMARS_GRAVITY * nWeight
fWeight5 = fJUPITER_GRAVITY * nWeight
fWeight6 = fSATURN_GRAVITY * nWeight
fWeight7 = fURANUS_GRAVITY * nWeight
fWeight8 = fNEPTUNE_GRAVITY * nWeight
fWeight9 = fPLUTO_GRAVITY * nWeight
 

# step 3 - output
print(f"{sName} here is your weights on our solar system's planets: ")
print(f"{'Weight on Mercury':25s}{fWeight1:10,.2f} ")
print(f"{'Weight on venus'  :25s}{fWeight2:10,.2f} ")
print(f"{'Weight on Moon'   :25s}{fWeight3:10,.2f} ")
print(f"{'Weight on Mars'   :25s}{fWeight4:10,.2f} ")
print(f"{'Weight on Jupiter':25s}{fWeight5:10,.2f} ")
print(f"{'Weight on Saturn' :25s}{fWeight6:10,.2f} ")
print(F"{'Weight on Uranus' :25s}{fWeight7:10,.2f} ")
print(f"{'Weight on Neptune':25s}{fWeight8:10,.2f} ")
print(f"{'Weight on Pluto'  :25s}{fWeight9:10,.2f} ")









