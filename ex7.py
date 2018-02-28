class MyClass:
    def __init__(self):
        self.numbers=[]

    def AddNumber(self, n):
        self.numbers.append(float(n))

    def SumNumbers(self):
        print(sum(self.numbers))

if __name__ == '__main__':
    m = MyClass()
    m.AddNumber(1)
    m.AddNumber(1)
    m.AddNumber(4)
    m.AddNumber(5)
    m.AddNumber(1)
    m.AddNumber(4)
    m.SumNumbers()
