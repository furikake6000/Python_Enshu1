def PrintTuple(tuple):
    PrintTupleSub(tuple)
    print()

def PrintTupleSub(tuple):
    for elem in tuple:
        if isinstance(elem, list):
            PrintTupleSub(elem)
        else:
            print(str(elem), end=' ')

if __name__ == '__main__':
    tuple = [[1, 2, 3], [4, 5, [6, 7], 8, 9]]
    PrintTuple(tuple)
