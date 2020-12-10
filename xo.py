from tabulate import tabulate
from random import choice

table = list(range(9))


def check(x, y: list):
    for i in y:
        if i != x: return False
    return True


def check_board(x, y: list):
    if x == '✖':
        if '❍' in y: return 0
    else:
        if '✖' in y: return 0
    if (y.count(x) > 1):
        return 1
    return 0


def print_tb(x):
    y = [x[i:i + 3] for i in range(0, len(x), 3)]
    return tabulate(y, stralign='center', tablefmt='fancy_grid')


def check_win(x):
    for i in range(9):
        if table[i] in ['✖', '❍']: continue
        tb = table.copy()
        tb[i] = x
        tb2 = [tb[i:i + 3] for i in range(0, 9, 3)]
        tb2.extend(list(zip(*tb2)))
        tb2.extend([tb[0:9:4], tb[2:7:2]])
        win = [check(x, i) for i in tb2]
        if any(win): return (True, i)
    return (False, 0)


def check_cn(x):
    for i in range(9):
        tb = table.copy()
        tb[i] = x
        tb2 = [tb[i:i + 3] for i in range(0, 9, 3)]
        tb2.extend(list(zip(*tb2)))
        tb2.extend([tb[0:9:4], tb[2:7:2]])
        win = [check_board(x, i) for i in tb2]
        if sum(win) > 1: return (True, i)
    return (False, 0)


cn = [9, 'Draw']
question = input('Are you want to start game Pc (y/n)?')
while question.lower() not in ('n', 'y'):
    question = input('Are you want to start game Pc (y/n)?')
if question.lower() == 'y':
    table[choice([0, 2, 6, 8])] = '❍'
    cn[0] -= 1
print(print_tb(table))
while cn[0]:
    x2 = input('Enter number : ')
    if x2.isdigit():
        x2 = int(x2)
        if 0 <= x2 <= 9:
            if table[x2] not in ['✖', '❍']:
                table[x2] = '✖'
                cn[0] -= 1
                if cn[0] == 0:
                    print(print_tb(table))
                    break
                if any(x := check_win('❍')):
                    table[x[1]] = '❍'
                    print(print_tb(table))
                    cn[1] = 'You lost'
                    break
                elif any(x := check_win('✖')):
                    table[x[1]] = '❍'
                elif any(x := check_cn('❍')):
                    table[x[1]] = '❍'
                elif any(x := check_cn('✖')):
                    ch = [i for i in range(0, 9, 2) if table[i] in ['✖', '❍']].__len__()
                    if ch == 3:
                        if table[4] == '✖':
                            ch2 = [i for i in range(0, 9, 2) if table[i] not in ['✖', '❍']]
                        else:
                            ch2 = [i for i in range(1, 8, 2) if table[i] not in ['✖', '❍']]
                        table[choice(ch2)] = '❍'
                    else:
                        table[x[1]] = '❍'
                elif cn[0] == 7:
                    ch = [i for i in range(1, 8, 2) if table[i] not in ['✖', '❍']].__len__()
                    if ch < 4:
                        table[4] = '❍'
                    else:
                        ch = [i for i in range(0, 9, 2) if table[i] not in ['✖', '❍']]
                        table[choice(ch)] = '❍'
                elif cn[0] == 8:
                    if table[4] == '✖':
                        table[choice([0, 2, 6, 8])] = '❍'
                    else:
                        table[4] = '❍'
                else:
                    ch = [i for i in range(0, 9) if table[i] not in ['✖', '❍']]
                    table[choice(ch)] = '❍'
                cn[0] -= 1
                print(print_tb(table))
            else:
                print(print_tb(table))
                print('This index is not empty')
        else:
            print(print_tb(table))
            print('This is not in index')
    else:
        print(print_tb(table))
        print('Please enter number')
print(cn[1])
