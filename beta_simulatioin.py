import random


class Ether:
    name = 'ether'
    data = ' '


class Cell:
    name = 'newBornCell'
    x = 0
    y = 0
    data = ''

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.data = value

    def grow(self):
        self.name = 'cell'

    def move_north(self):
        if field[y - 1][x].name == 'ether':
            field[y - 1][x] = Cell(x, y - 1, self.data) 
            field[y][x] = Ether()

    def move_south(self):
        if field[y + 1][x].name == 'ether':
            field[y + 1][x] = Cell(x, y + 1, self.data) 
            field[y][x] = Ether()

    def move_west(self):
        if field[y][x - 1].name == 'ether':
            field[y][x - 1] = Cell(x - 1, y, self.data) 
            field[y][x] = Ether()

    def move_east(self):
        if field[y][x + 1].name == 'ether':
            field[y][x + 1] = Cell(x + 1, y, self.data) 
            field[y][x] = Ether()

    def divide_north(self):
        if field[y - 1][x].name == 'ether':
            field[y - 1][x] = Cell(x, y - 1, self.data) 

    def divide_south(self):
        if field[y + 1][x].name == 'ether':
            field[y + 1][x] = Cell(x, y + 1, self.data) 

    def divide_west(self):
        if field[y][x - 1].name == 'ether':
            field[y][x - 1] = Cell(x - 1, y, self.data) 

    def divide_east(self):
        if field[y][x + 1].name == 'ether':
            field[y][x + 1] = Cell(x + 1, y, self.data) 

    def die(self):
        mortalityRate = random.random()
        if motalityRate >= 0.6:
            field[y][x] = Ether()


class Barrier:
    name = 'barrier'
    data = '+' 


class Builder(Cell):
    name = 'newBornBuilder'

    def grow(self):
        self.name = 'builder'

    def move_north(self):
        if field[y - 1][x].name == 'ether':
            field[y - 1][x] = Builder(x, y - 1, self.data) 
            field[y][x] = Barrier()

    def move_south(self):
        if field[y + 1][x].name == 'ether':
            field[y + 1][x] = Builder(x, y + 1, self.data) 
            field[y][x] = Barrier()

    def move_west(self):
        if field[y][x - 1].name == 'ether':
            field[y][x - 1] = Builder(x - 1, y, self.data) 
            field[y][x] = Barrier()

    def move_east(self):
        if field[y][x + 1].name == 'ether':
            field[y][x + 1] = Builder(x + 1, y, self.data) 
            field[y][x] = Barrier()


#make field
while True:
    try:
        size = int(input('set size (recommend: 10 ~ 30) >> '))
        wholeSize = size + 2
        break
    except ValueError:
        print('please input number')

field = [[Ether() for n in range(wholeSize)] for m in range(wholeSize)]

for y in range(wholeSize):
    if y in [0, wholeSize - 1]:
        for x in range(wholeSize):
            field[y][x] = Barrier()
    else:
        for x in [0, wholeSize - 1]:
            field[y][x] = Barrier()


#initial value
while True:
    start0 = [random.randint(1, wholeSize - 2), random.randint(1, wholeSize - 2)]
    start1 = [random.randint(1, wholeSize - 2), random.randint(1, wholeSize - 2)]
    start5 = [random.randint(1, wholeSize - 2), random.randint(1, wholeSize - 2)]

    #check overlap
    startSpot = [start0, start1, start5]
    startSpotUnique = []
    for spot in startSpot:
        if spot not in startSpotUnique:
            startSpotUnique.append(spot)

    if len(startSpotUnique) == 3: 
        field[start0[1]][start0[0]] = Cell(start0[0], start0[1], 0)
        field[start1[1]][start1[0]] = Cell(start1[0], start1[1], 1)
        field[start5[1]][start5[0]] = Builder(start5[0], start5[1], 5)
        break



#game
while True:
    command = input('Enter or q >> ')
    if command == 'q':
        break
    else:
        for y in range(wholeSize):
            for x in range(wholeSize):
                if field[y][x].name == 'cell':
                    num = random.randint(0, 7)
                    if num == 0:
                        field[y][x].move_north()
                    elif num == 1:
                        field[y][x].move_south()
                    elif num == 2:
                        field[y][x].move_west()
                    elif num == 3:
                        field[y][x].move_east()
                    elif num == 4:
                        field[y][x].divide_north()
                    elif num == 5:
                        field[y][x].divide_south()
                    elif num == 6:
                        field[y][x].divide_west()
                    elif num == 7:
                        field[y][x].divide_east()
                if field[y][x].name in ['cell', 'newBornCell']:
                    field[y][x].die
                if field[y][x].name == 'builder':
                    num = random.randint(0, 3)
                    if num == 0:
                        field[y][x].move_north()
                    elif num == 1:
                        field[y][x].move_south()
                    elif num == 2:
                        field[y][x].move_west()
                    elif num == 3:
                        field[y][x].move_east()

        print()
        for y in range(wholeSize):
            print(' ', end='')
            for x in range(wholeSize):
                print(str(field[y][x].data) + ' ', end='')
            print()
        print()

        for y in range(wholeSize):
            for x in range(wholeSize):
                if field[y][x].name in ['newBornCell', 'newBornBuilder']:
                    field[y][x].grow()
