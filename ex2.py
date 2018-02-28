def Factorial(x):
    if not x.isdigit(): return x + 'は自然数ではありません'
    result = 1
    x = int(x)
    while x > 1:
        result *= x
        x -= 1
    return result

if __name__ == '__main__':
    print(Factorial(input('>> ')))
