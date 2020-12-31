from numpy import array, flipud, ndarray
from re import match
from random import choice

table = array(9 * [' ']).reshape(3, 3)
cn = [9, 'Draw', ('X', 'O')]
columns = {'a': 0, 'b': 1, 'c': 2}
table_shape = '''
     a   b   c

 1   {} │ {} │ {} 
    ───┼───┼───
 2   {} │ {} │ {} 
    ───┼───┼───
 3   {} │ {} │ {} 

'''

def check_win(x: str):
    for r in range(3):
        for c in range(3):
            if table[r][c]!=' ': continue
            tb = table.copy()
            tb[r][c]=x
            tb2 = (tb==x)
            if tb2[r].all() or tb2[:, c].all() or tb2.diagonal().all() or flipud(tb2).diagonal().all(): return True,r,c
    return False,0,0

def check_board(x: str, y: ndarray):
    cn = (y==x).sum()
    if ' ' in y and cn == 2: return 1
    return 0

def check_cn(x: str):
    for r in range(3):
        for c in range(3):
            if table[r][c] != ' ': continue
            tb = table.copy()
            tb[r][c] = x
            win = [check_board(x, tb[r]), check_board(x, tb[:, c]), check_board(x, tb.diagonal()), check_board(x, flipud(tb).diagonal())]
            if sum(win)>1: return True,r,c
    return False,0,0

question = input('Are you start PC? (y/n): ').lower()
while not question in ('y','n'): question = input('Are you start PC? (y/n): ').lower()
if question == 'y': cn[0]-=1;table[choice([0,2])][choice([0,2])]=cn[2][1]
print(table_shape.format(*table.flatten()))
while cn[0]>0:
    x = input('Enter x,y (example 1a): ')
    if y:=match(r'([1-3])([a-c])$',x):
        row=int(y.group(1))-1;column=columns[y.group(2)]
        if table[row][column]==' ':
            cn[0]-=1;table[row][column]=cn[2][0]
            if cn[0]==0: print(table_shape.format(*table.flatten()));break
            if any(ind:=check_win(cn[2][1])):
                table[ind[1]][ind[2]]=cn[2][1]
                print(table_shape.format(*table.flatten()))
                cn[1] = 'You lost :(';break
            elif any(ind:=check_win(cn[2][0])):
                table[ind[1]][ind[2]] = cn[2][1]
            elif any(ind:=check_cn(cn[2][1])):
                table[ind[1]][ind[2]] = cn[2][1]
            elif any(ind:=check_cn(cn[2][0])):
                if cn[0]==6:
                    ch = [table.diagonal(),flipud(table).diagonal()]
                    for i in ch:
                        tb = table.flatten()
                        if (i!=' ').all():
                            if i[0] == i[2]:
                                empty_indexes = [index for index, val in enumerate(tb) if val == ' ' and index%2!=0]
                            else:
                                empty_indexes = [index for index, val in enumerate(tb) if val == ' ' and index % 2 == 0]
                            tb[choice(empty_indexes)] = cn[2][1]
                            table = tb.reshape(3,3)
                else:
                    table[ind[1]][ind[2]] = cn[2][1]
            else:
                if table[1][1]==' ' and cn[0]==8:
                    table[1][1]=cn[2][1]
                else:
                    tb = table.flatten()
                    empty_indexes = [index for index,val in enumerate(tb) if val==' ']
                    tb[choice(empty_indexes)] = cn[2][1]
                    table = tb.reshape(3,3)
            cn[0]-=1
            print(table_shape.format(*table.flatten()))
        else:
            print(table_shape.format(*table.flatten()),'This index is not empty')
    else:
        print(table_shape.format(*table.flatten()))
print(cn[1])