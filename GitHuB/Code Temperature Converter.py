# Author Jean Toussaint
# Class Py
# Date 3/6/2025


# Code Temperature Converter


# Input

print ("Welcome to Jean's Temp Converter\n\n")

fUserTemp = float(input('What is your Temperature: '))
nTempType = input ("Is the Temperature F for fahrenheit or C for Celsius? ")


# conversions
fFahrenheit = ((9.0 / 5.0) * fUserTemp ) + 32
fCelsius = (5.0 / 9) * (fUserTemp - 32)

# logic Statement
if nTempType == 'F' or nTempType == 'f':
    if fUserTemp > 212:
        print('Temperature can not be > 212')
    elif fUserTemp <= 212:
        print(f"The Celsius equivalent is: {fCelsius:.1f}")
elif nTempType == 'C' or nTempType == 'c':
    if fUserTemp > 100:
        print("Temperature can not be > 100")
    elif fUserTemp <= 100:
        print(f"The Celsius equivalent is {fFahrenheit:.1f}")
else:
    print ("Enter F or C only.")
    
 





 



