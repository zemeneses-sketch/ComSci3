year = int(input("Enter your birth year: "))

baseline = 1900

if year < baseline:
    print("Invalid output. It must not be earlier than 1900 :<")

elif year > baseline:
    modolus = (year - baseline) % 12
    if modolus == 0:
        print("Your zodiac sign is: Rat (鼠 / Shǔ)")
    elif modolus == 1:
        print("Your zodiac sign is: Ox (牛 / Niú)")
    elif modolus == 2:
        print("Your zodiac sign is: Tiger (虎 / Hǔ)")
    elif modolus == 3:
        print("Your zodiac sign is: Rabbit (兔 / Tù)")
    elif modolus == 4:
        print("Your zodiac sign is: Dragon (龙 / Lóng)")
    elif modolus == 5:
        print("Your zodiac sign is: Snake (蛇 / Shé)")
    elif modolus == 6:
        print("Your zodiac sign is: Horse (马 / Mǎ)")
    elif modolus == 7:
        print("Your zodiac sign is: Goat (羊 / Yáng)")
    elif modolus == 8:
        print("Your zodiac sign is: Monkey (猴 / Hóu)")
    elif modolus == 9:
        print("Your zodiac sign is: Rooster (鸡 / Jī)")
    elif modolus == 10:
        print("Your zodiac sign is: Dog (狗 / Gǒu)")
    elif modolus == 11:
        print("Your zodiac sign is: Pig (猪 / Zhū)")

else:
    print("you have entered an invalid input")