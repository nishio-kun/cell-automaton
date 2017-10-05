import random

def check_cell(num):
    if num in [0, 1]:
        return True
    else:
        return False

class Cell:
    x = 0
    y = 0
    preData = '-'
    newData = '-'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def grow_north(self):
        if check_cell(self.preData):
            if y != 0:
                try:
                    field[self.y-1][self.x].newData = self.preData
                except IndexError:
                    pass

    def grow_south(self):
        if check_cell(self.preData):
            try:
                field[self.y+1][self.x].newData = self.preData
            except IndexError:
                pass

    def grow_west(self):
        if check_cell(self.preData):
            if x != 0:
                try:
                    field[self.y][self.x-1].newData = self.preData
                except IndexError:
                    pass

    def grow_east(self):
        if check_cell(self.preData):
            try:
                field[self.y][self.x+1].newData = self.preData
            except IndexError:
                pass

    def pay_off(self):
        self.preData = self.newData

#make field
field = [['' for n in range(10)] for m in range(10)]
for y in range(10):
    for x in range(10):
        field[y][x] = Cell(x,y)

while True:
    start0 = [random.randint(0,9), random.randint(0,9)]
    start1 = [random.randint(0,9), random.randint(0,9)]

    if start0 != start1:
        field[start0[1]][start0[0]].preData = 0
        field[start0[1]][start0[0]].newData = 0
        field[start1[1]][start1[0]].preData = 1
        field[start1[1]][start1[0]].newData = 1
        break

#game
while True:
    command = input('Enter or q >> ')
    if command == 'q':
        break
    else:
        for y in range(10):
            for x in range(10):
                field[y][x].grow_north()
                field[y][x].grow_south()
                field[y][x].grow_west()
                field[y][x].grow_east()
        print()
        for y in range(10):
            print(' ', end='')
            for x in range(10):
                print(str(field[y][x].preData) + ' ', end='')
            print()
        print()
        for y in range(10):
            for x in range(10):
                field[y][x].pay_off()
