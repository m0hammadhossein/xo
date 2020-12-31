from numpy import array, flipud
from re import match

table = array(9 * [' ']).reshape(3, 3)
cn = [9, 'Draw', ('X', 'O'), 'X']
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
    tb = (table == x)
    for i in range(3):
        if tb[i].all() or tb[:, i].all(): return True
    if tb.diagonal().all() or flipud(tb).diagonal().all(): return True
    return False

print(table_shape.format(*table.flatten()))
while cn[0] > 0:
    x = input('Enter x,y (example 1a): ')
    if y := match(r'([1-3])([a-c])$', x):
        row = int(y.group(1)) - 1
        column = columns[y.group(2)]
        if table[row][column] == ' ':
            table[row][column] = cn[3]
            cn[0] -= 1
            if check_win(cn[3]):
                print(table_shape.format(*table.flatten()))
                cn[1] = f'{cn[3]} is winner'
                break
            else:
                cn[3] = cn[2][1] if cn[3] == cn[2][0] else cn[2][0]
            print(table_shape.format(*table.flatten()))
        else:
            print(table_shape.format(*table.flatten()), 'this index is not empty')
    else:
        print(table_shape.format(*table.flatten()))
print(cn[1])