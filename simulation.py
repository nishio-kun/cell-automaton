import random
import bomb

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
            if y != 0:      #to stop the bomberman phenomeno
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
while True:
    try:
        size = int(input('set size (recommend: 10 ~ 30) >> '))
        break
    except ValueError:
        print('please input number')

field = [['' for n in range(size)] for m in range(size)]
for y in range(size):
    for x in range(size):
        field[y][x] = Cell(x,y)

#initial value
while True:
    start0 = [random.randint(0,size), random.randint(0,size)]
    start1 = [random.randint(0,size), random.randint(0,size)]

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
    elif command == 'balus':
        bomb.balus(field, command)
    else:
        for y in range(size):
            for x in range(size):
                field[y][x].grow_north()
                field[y][x].grow_south()
                field[y][x].grow_west()
                field[y][x].grow_east()
        bomb.explode(field)
        print()
        for y in range(size):
            print(' ', end='')
            for x in range(size):
                print(str(field[y][x].preData) + ' ', end='')
            print()
        print()

        for y in range(size):
            for x in range(size):
                field[y][x].pay_off()
