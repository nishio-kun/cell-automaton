import random

class Cell:
    x = 0
    y = 0
    preData = '-'
    newData = '-'

    def __init__(self, i, j):
        self.x = i
        self.y = j

    def foster(self):
        try:
            field[self.y][self.x-1].newData = self.preData
        except IndexError:
            pass
        try:
            field[self.y][self.x+1].newData = self.preData
        except IndexError:
            pass
        try:
            field[self.y-1][self.x].newData = self.preData
        except IndexError:
            pass
        try:
            field[self.y+1][self.x].newData = self.preData
        except IndexError:
            pass

    def pay_off(self):
        self.preData = self.newData

#bomb
def explode():
    hypocenter = [random.randint(1,8), random.randint(1,8)]
    field[hypocenter[0]][hypocenter[1]].newData = '#'
    field[hypocenter[0]-1][hypocenter[1]].newData = '#'
    field[hypocenter[0]+1][hypocenter[1]].newData = '#'
    field[hypocenter[0]][hypocenter[1]-1].newData = '#'
    field[hypocenter[0]][hypocenter[1]+1].newData = '#'
    
#make field
field = [[] for i in range(10)]
for i in range(10):
    for j in range(10):
        field[i].append(Cell(j, i))

#initial value
while True:
    start0 = [random.randint(0,9), random.randint(0,9)]
    start1 = [random.randint(0,9), random.randint(0,9)]

    if start0 != start1:
        field[start0[0]][start0[1]].preData = 0
        field[start1[0]][start1[1]].preData = 1
        break

#game
while True:
    command = input('q or Enter >> ')
    if command == 'q':
        print('Good Bye')
        break
    else:
        for i in range(10):
            for j in range(10):
                field[i][j].foster()
                print(str(field[i][j].newData) + ' ', end='')
                field[i][j].pay_off()
            print()
