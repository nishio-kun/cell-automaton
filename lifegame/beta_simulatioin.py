import random
from field import create_field, set_barrier_ether
from initial_value import set_start_point


def start():
    while True:
        print('input "s" to start')
        print('input "o" to option')
        print('input "q" to quit')
        initialCommand = input()
        if initialCommand == "s":
            break
        elif initialCommand == "o":
            pass
        elif initialCommand == "q":
            break
        else:
            pass 


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
                if field[y][x].name == 'cell':
                    num = random.randint(0, 7)
                    if num == 0:
                        field[y][x].move_north(field)
                    elif num == 1:
                        field[y][x].move_south(field)
                    elif num == 2:
                        field[y][x].move_west(field)
                    elif num == 3:
                        field[y][x].move_east(field)
                    elif num == 4:
                        field[y][x].divide_north(field)
                    elif num == 5:
                        field[y][x].divide_south(field)
                    elif num == 6:
                        field[y][x].divide_west(field)
                    elif num == 7:
                        field[y][x].divide_east(field)
                if field[y][x].name in ['cell', 'newBornCell']:
                    field[y][x].die
                if field[y][x].name == 'builder':
                    while True:
                        if 'ether' not in [field[y - 1][x].name, field[y + 1][x].name, field[y][x - 1].name, field[y][x + 1].name]:
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
