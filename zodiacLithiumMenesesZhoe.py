year = int(input("Enter your birth year: ")) # making the user input the year that they were born

Baseline = 1900 # variable for the standard baseline of computation

#While loop to makesure if the user entered a valid input
# if not the while loop will stop 
while year < Baseline:
    #print statement if the input is wrong 
    print("invalid year :<, should not be before 1900")
    year = int(input("Enter your birth year: "))

#list that holds all of the zodiac signs
Zodiac_sign = ["Rat (鼠 / Shǔ)", 
      "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)", 
        " Rabbit (兔 / Tù)", 
        "Dragon (龙 / Lóng)", 
        "Snake (蛇 / Shé)", 
        "Horse (马 / Mǎ)", 
        "Goat (羊 / Yáng)", 
        "Monkey (猴 / Hóu)", 
        "Rooster (鸡 / Jī)",
        " Dog (狗 / Gǒu)",
        " Pig (猪 / Zhū)" ]


#to calculate the index to be used in the list or valiable "Zodiac_sign"
#i used modulus 12 because it is stated that teh zodiac repeats every 12 years
index = (year - Baseline) % 12

#getting the zodiac sign by some computations
#searching for the index in teh list
Final_zodiac = Zodiac_sign[index]

#final print statement stating the zodiac sign 
print(f"Your zodiac sign is : {Final_zodiac}")






