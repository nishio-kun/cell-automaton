class Cell:
    preData = '-'
    newData = '-'

    #def effect(self):

    def pay_off(self):
        self.preData = self.newData

    def print_cell(self):
        print(str(newData) + ' ', end='')

def check(x):
    if x in [0, 1]:
        return True
    else:
        return False

def process():
    for i in range(10):
        if i == 0:
            if check(field[0][0].preData):
                field[0][1].newData = field[0][0].preData
                field[1][0].newData = field[0][0].preData
            if check(field[0][9].preData):
                field[0][8].newData = field[0][9].preData
                field[1][9].newData = field[0][9].preData
            for j in range(1, 9):
                if check(field[0][j].preData):
                    field[1][j].newData = field[0][j].preData
                    field[0][j-1].newData = field[0][j].preData
                    field[0][j+1].newData = field[0][j].preData

        elif i == 9:
            if check(field[9][0].preData):
                field[9][1].newData = field[9][0].preData
                field[8][0].newData = field[9][0].preData
            if check(field[9][9].preData):
                field[9][8].newData = field[9][9].preData
                field[8][9].newData = field[9][9].preData
            for j in range(1, 9):
                if check(field[9][j].preData):
                    field[8][j].newData = field[9][j].preData
                    field[9][j-1].newData = field[9][j].preData
                    field[9][j+1].newData = field[9][j].preData

        else:
            for j in range(10):
                if j == 0:
                    if check(field[i][0].preData):
                        field[i-1][0].newData = field[i][0].preData
                        field[i+1][0].newData = field[i][0].preData
                        field[i][1].newData = field[i][0].preData
                if j == 9:
                    if check(field[i][9].preData):
                        field[i-1][9].newData = field[i][9].preData
                        field[i+1][9].newData = field[i][9].preData
                        field[i][8].newData = field[i][9].preData
                if j not in [0, 9] and check(field[i][j].preData):
                    field[i-1][j].newData = field[i][j].preData
                    field[i+1][j].newData = field[i][j].preData
                    field[i][j-1].newData = field[i][j].preData
                    field[i][j+1].newData = field[i][j].preData

#make field
field = [[Cell() for i in range(10)] for j in range(10)]

#initial value
field[0][9].newData = 0
field[9][0].newData = 1

#main
while True:
    command = input('n or <Enter> >> ')
    if command == 'q':
        print('Good Bye')
        break
    else:
        process()

        for i in range(10):
            for j in range(10):
                print(str(field[i][j].newData) + ' ', end='')
                field[i][j].pay_off()
            print()
