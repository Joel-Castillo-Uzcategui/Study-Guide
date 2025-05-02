p1=0
p2=0
while int(p1)<3 or int(p2)<3:
    c1=input("Welcome!\n Player one, pick Rock (R), Paper (P), Scissors (S)\n")
    c2=input("And what does Player 2 pick?\n")
    if c1=="R" and c2=="P" or c1=="P" and c2=="S" or c1=="S" and c2=="R":
        p1+=1
        if p1==3:
            print("Hurray!, Player 1 won")
            break
        elif p2==3:
            print("Hurray!, Player 2 won")
            break
        else:
            print("Congratulations!, Player 2 won")
            continue
    elif c2=="R" and c1=="P" or c2=="P" and c1=="S" or c2=="S" and c1=="R":
        p2+=1
        if p1==3:
            print("Hurray!, Player 1 won")
            break
        elif p2==3:
            print("Hurray!, Player 2 won")
            break
        else:
            print("Congratulations!, Player 1 won")
            continue
    elif c2==c1:
        print("Whoops, you drew the same, try again")
    else:
        print("Huh?, Didn't get it, try again")
        continue