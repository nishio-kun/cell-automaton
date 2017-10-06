# coding : utf-8
#wall
import random

def wall(field):
    for i in range(3):
        wall_cell = [random.randint(0,9),random.randint(0,9)]
        field[wall_cell[0]][wall_cell[1]].newData = "|"

#how can we fix the wall Cell?
#ランダムじゃなくてコマンド入力する時にどこに壁を作るかを指定できるようにする
