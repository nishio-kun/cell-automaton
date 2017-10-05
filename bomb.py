import random

#bomb

def explode():
    hypocenter = [random.randint(1,8), random.randint(1,8)]
    field[hypocenter[0]][hypocenter[1]].newData = '#'
    field[hypocenter[0]-1][hypocenter[1]].newData = '#'
    field[hypocenter[0]+1][hypocenter[1]].newData = '#'
    field[hypocenter[0]][hypocenter[1]-1].newData = '#'
    field[hypocenter[0]][hypocenter[1]+1].newData = '#'
