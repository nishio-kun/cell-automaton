import random
from element import Cell, Builder


def set_start_point(field, wholeSize):
    while True:
        try:
            numOfUnit = int(input('set number of unit (1 ~ 9) >> ')) + 1
            if 1 <= numOfUnit <= 10:
                break
            else:
                print('please input number in 1 ~ 9')
        except ValueError:
            print('please input number')

    while True:
        startPoint = []
        startPointUnique = []

        for i in range(numOfUnit):
            startPoint.append([random.randint(1, wholeSize - 2), random.randint(1, wholeSize - 2)])

        #check overlap
        for point in startPoint:
            if point not in startPointUnique:
                startPointUnique.append(point)

        if len(startPointUnique) == numOfUnit:
            for i in range(numOfUnit - 1):
                field[startPoint[i][1]][startPoint[i][0]] = Cell(startPoint[i][0], startPoint[i][1], i)
            field[startPoint[numOfUnit - 1][1]][startPoint[numOfUnit - 1][0]] = Builder(startPoint[numOfUnit - 1][0], startPoint[numOfUnit - 1][1], 9)
            break

