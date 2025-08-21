from random import randrange

def isEven(number): 
    return number % 2 == 0

def isOdd(number): 
    return not isEven(number)

if __name__ == "__main__":
    number = randrange(100)
    if isEven(number):
        print(f'{number} is even!')
    else:
        print(f'{number} is odd!')