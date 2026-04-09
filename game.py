import random
def choix():
    c = random.randint(0,3)

    if c == 0:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        r = input(f'{num1} + {num2} = ')
        if int(r) == (num1 + num2):
            print("Bonne réponse !")
        else:
            print("Faux, le résultat était", num1+num2)


    if c == 1:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        mini = min(num1,num2)
        maxi = max(num1,num2)
        r = input(f'{maxi} - {mini} = ')
        if int(r) == (maxi - mini):
            print("Bonne réponse !")
        else:
            print("Faux, le résultat était", maxi-mini)

    if c == 2:
        num1 = random.randint(1,20)
        num2 = random.randint(1,9)
        r = input(f'{num1} x {num2} = ')
        if int(r) == (num1*num2):
            print('Bonne réponse !')

        else:
            print("Faux, le résultat était", num1*num2)

    if c == 3:
        num2 = random.randint(2, 9)
        num1 = random.randrange(num2, 999, num2)

        r = input(f'{num1} : {num2} = ')
        if int(r) == (num1//num2):
            print("Bonne réponse !")

        else:
            print("Faux, le résultat était", num1//num2)

while True:
    choix()

