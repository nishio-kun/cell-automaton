from element import Ether, Barrier


#make a list which size is (x + 2) * (x + 2)
def create_field():
    while True:
        try:
            size = int(input('set size (recommend: 10 ~ 30) >> '))
            wholeSize = size + 2
            break
        except ValueError:
            print('please input number')

    field = [['a' for n in range(wholeSize)] for m in range(wholeSize)]

    return field


# make frame and fill in it by ether
def set_barrier_ether(field, wholeSize):
    for y in range(wholeSize):
        if y in [0, wholeSize - 1]:
            for x in range(wholeSize):
                field[y][x] = Barrier()
        else:
            for x in [0, wholeSize - 1]:
                field[y][x] = Barrier()
            for x in range(1, wholeSize - 1):
                field[y][x] = Ether()
