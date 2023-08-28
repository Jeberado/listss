while True:
    symbol = input('Type your symbol (+, -, /, *): ')
    x = int(input("First digit: "))
    y = int(input("Second digit: "))

    if symbol == "+":
        print(x+y)
    elif symbol == "-":
        print(x-y)
    elif symbol == "/":
        print(x/y)
        if y == 0:
            print('You cant divide on 0')
    elif symbol == "*":
        print(x*y)
    choise = input('Continue? (Y/N) or (y/n) :  ')
    if choise != 'Y' and choise != 'y':
        break