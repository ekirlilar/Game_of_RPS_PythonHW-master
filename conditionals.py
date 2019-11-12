# look at a temperature and figure out what state water is in - solid, liquid or gas

   # set the temperature first - and turn our text input into a number => that's what int() does
temp = int(input("enter a temperzture: "))

if temp < 4:
    print ("water is frozen - a solid")

if temp > 4 and temp < 100:
    print("wter is liquid")

if temp >= 100:
    print("water is a gas")

else:
    print("Try again")


# need to check all of your conditions after checking for a tie