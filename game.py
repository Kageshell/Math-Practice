from random import randint
def choix():
    c = randint(0,3)

    if c == 0:
        num1 = randint(1,100)
        num2 = randint(1,100)
        r = input(f'{num1} + {num2} = ')
        print(int(r) == (num1 + num2))

    if c == 1:
        num1 = randint(1,100)
        num2 = randint(1,100)
        r = input(f'{num1} - {num2} = ')
        print(float(r) == (num1 - num2))

choix()
