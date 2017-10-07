import random


class Ether:
    name = 'ether'
    data = ' '


class Barrier:
    name = 'barrier'
    data = '+' 


class Food:
    name = 'food'
    data = '@' 


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

    def move_north(self, field):
        if field[self.y - 1][self.x].name == 'ether':
            field[self.y - 1][self.x] = Cell(self.x, self.y - 1, self.data) 
            field[self.y][self.x] = Ether()

    def move_south(self, field):
        if field[self.y + 1][self.x].name == 'ether':
            field[self.y + 1][self.x] = Cell(self.x, self.y + 1, self.data) 
            field[self.y][self.x] = Ether()

    def move_west(self, field):
        if field[self.y][self.x - 1].name == 'ether':
            field[self.y][self.x - 1] = Cell(self.x - 1, self.y, self.data) 
            field[self.y][self.x] = Ether()

    def move_east(self, field):
        if field[self.y][self.x + 1].name == 'ether':
            field[self.y][self.x + 1] = Cell(self.x + 1, self.y, self.data) 
            field[self.y][self.x] = Ether()

    def divide_north(self, field):
        if field[self.y - 1][self.x].name == 'ether':
            field[self.y - 1][self.x] = Cell(self.x, self.y - 1, self.data) 

    def divide_south(self, field):
        if field[self.y + 1][self.x].name == 'ether':
            field[self.y + 1][self.x] = Cell(self.x, self.y + 1, self.data) 

    def divide_west(self, field):
        if field[self.y][self.x - 1].name == 'ether':
            field[self.y][self.x - 1] = Cell(self.x - 1, self.y, self.data) 

    def divide_east(self, field):
        if field[self.y][self.x + 1].name == 'ether':
            field[self.y][self.x + 1] = Cell(self.x + 1, self.y, self.data) 

    def die(self, field):
        mortalityRate = random.random()
        if motalityRate >= 0.6:
            field[self.y][self.x] = Ether()


class Builder(Cell):
    name = 'newBornBuilder'

    def grow(self):
        self.name = 'builder'

    def move_north(self, field):
        if field[self.y - 1][self.x].name == 'ether':
            field[self.y - 1][self.x] = Builder(self.x, self.y - 1, self.data) 
            field[self.y][self.x] = Barrier()

    def move_south(self, field):
        if field[self.y + 1][self.x].name == 'ether':
            field[self.y + 1][self.x] = Builder(self.x, self.y + 1, self.data) 
            field[self.y][self.x] = Barrier()

    def move_west(self, field):
        if field[self.y][self.x - 1].name == 'ether':
            field[self.y][self.x - 1] = Builder(self.x - 1, self.y, self.data) 
            field[self.y][self.x] = Barrier()

    def move_east(self, field):
        if field[self.y][self.x + 1].name == 'ether':
            field[self.y][self.x + 1] = Builder(self.x + 1, self.y, self.data) 
            field[self.y][self.x] = Barrier()

