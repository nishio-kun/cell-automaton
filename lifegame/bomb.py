import random

#bomb
#return the explosion cell at random

def explode(field):
    center = [random.randint(0,9),random.randint(0,9)]  #select the cell which will be exploded
    try:
        field[center[0]][center[1]].newData = '*'
        field[center[0]-1][center[1]].newData = '*'
        field[center[0]-1][center[1]-1].newData = '*'
        field[center[0]+1][center[1]].newData = '*'
        field[center[0]+1][center[1]+1].newData = '*'
        field[center[0]][center[1]-1].newData = '*'
        field[center[0]+1][center[1]-1].newData = '*'
        field[center[0]][center[1]+1].newData = '*'
        field[center[0]-1][center[1]+1].newData = '*'
        """
        for i in range(-2,3):
            for j in range(-2,3):
                if i != j and abs(i) != 2:
                    field[center[0]+j][center[1]+i].newData = '*'
                else:
                    pass
        """

    except IndexError:
        pass


def balus(field, decision):
    if decision == 'balus':
        for i in range(10):
            for j in range(10):
                field[i][j].newData = ' '
                field[i][j].preData = ' '
    else:
        pass
