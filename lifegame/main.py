import random
from field import create_field, set_barrier_ether
from initial_value import set_start_point
from element import Barrier, Food, Cell, Builder


# set field
field = create_field()
wholeSize = len(field)

set_barrier_ether(field, wholeSize)


# set start point
set_start_point(field, wholeSize)


# main
while True:
    command = input('Enter or q >> ')
    if command == 'q':
        break
    else:
        for y in range(wholeSize):
            for x in range(wholeSize):
                if field[y][x].name == 'builder':
                    while True:
                        if 'ether' not in [field[y - 1][x].name, field[y + 1][x].name, field[y][x - 1].name, field[y][x + 1].name]:
                            field[y][x] = Barrier()
                            for i in range(100):
                                rand_x = random.randint(1, wholeSize - 2)
                                rand_y = random.randint(1, wholeSize - 2)
                                if field[rand_y][rand_x].name == 'ether':
                                    field[rand_y][rand_x] = Builder(rand_x, rand_y, 9)
                                    break
                            break
                        num = random.randint(0, 3)
                        if num == 0:
                            if field[y - 1][x].name == 'ether':
                                field[y][x].move_north(field)
                                break
                        elif num == 1:
                            if field[y + 1][x].name == 'ether':
                                field[y][x].move_south(field)
                                break
                        elif num == 2:
                            if field[y][x - 1].name == 'ether':
                                field[y][x].move_west(field)
                                break
                        elif num == 3:
                            if field[y][x + 1].name == 'ether':
                                field[y][x].move_east(field)
                                break

                if field[y][x].name == 'cell':
                    if field[y - 1][x].name == 'food':
                        field[y - 1][x] = Cell(x, y - 1, field[y][x].data)

                    if field[y + 1][x].name == 'food':
                        field[y + 1][x] = Cell(x, y + 1, field[y][x].data)

                    if field[y][x - 1].name == 'food':
                        field[y][x - 1] = Cell(x - 1, y, field[y][x].data)

                    if field[y][x + 1].name == 'food':
                        field[y][x + 1] = Cell(x + 1, y, field[y][x].data)

                    num = random.randint(0, 3)
                    if num == 0:
                        field[y][x].move_north(field)
                    elif num == 1:
                        field[y][x].move_south(field)
                    elif num == 2:
                        field[y][x].move_west(field)
                    elif num == 3:
                        field[y][x].move_east(field)

                '''
                if field[y][x].name in ['cell', 'newBornCell']:
                    field[y][x].die
                '''

        if random.random() <= 0.2:
            for i in range(100):
                rand_x = random.randint(1, wholeSize - 2)
                rand_y = random.randint(1, wholeSize - 2)
                if field[rand_y][rand_x].name == 'ether':
                    field[rand_y][rand_x] = Food()
                    break

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
