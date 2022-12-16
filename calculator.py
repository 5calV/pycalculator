
#--------------------------------------------------------------------------------------------------------------------------------------------

#   ╭∩╮   ╭∩╮
#    \(͡⚈ᴗ͡⚈)/

#--------------------------------------------------------------------------------------------------------------------------------------------

# Loop Start
while True:


# Global Variables

# Addition, Subtraction, Multiplication or Division?
    calculation = input("Which Type of Calculation do you want to use?\nAddition ( 1 )\nSubtraction ( 2 )\nMultiplication ( 3 )\nDivision ( 4 )\n")

# User gives number 1, number 2.
    a = float(input('Enter Number 1: '))
    b = float(input('Enter Number 2: '))

# Result
    addition = (a+b)
    subtraction = (a-b)
    multiplication = (a*b)
    division = (a/b)

#--------------------------------------------------------------------------------------------------------------------------------------------

# Addition

    if (calculation) == "1":
        print (('Your Result:'), addition)

# Subtraction

    if (calculation) == "2":
        print (('Your Result:'), subtraction)

# Multiplication

    if (calculation) == "3":
        print (('Your Result:'), multiplication)

# Division

    if (calculation) == "4":
        print (('Your Result:'), division)

#---------------------------------------------------------------------------------------------------------------------------------------------

# Restart?

    restart = input("Would you like to do another Calculation? ( y / n )\n")

    if (restart) == ("y"):
        continue
    else:
        break

#----------------------------------------------------------------------------------------------------------------------------------------------
