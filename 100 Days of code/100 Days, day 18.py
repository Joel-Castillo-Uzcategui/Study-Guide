g=0
while True:
    n=int(input("Guess the right number! OneInOneMillion!"))
    g+=1
    if n==696969:
        print("Congratulations, you got it correctly!\nIt took you",g,"tries to guess the right number")
        break
    elif n<696969:
        print("too low")
        continue
    elif n>696969:
        print("too high")
        continue
    else:
        print("Didn't understand, please insert a number between 1(one) and 1000000(1 million)")
        continue