class TribIterator:
    t1 = t2 = 0
    t3 = 1

    def __init__(self, size):
        self.x = 0
        self.size = size

    def __next__(self):
        self.x += 1
        if self.x > self.size:
            raise StopIteration
        if self.x == 1 or self.x == 2:
            return 0
        if self.x == 3:
            return 1
        self.t1, self.t2, self.t3 = self.t2, self.t3, self.t1 + self.t2 + self.t3
        return self.t3

    def __iter__(self):
        return self

number = int(input("Введите количество чисел"))
trib = TribIterator(number)
for i in trib:
    print(i)
