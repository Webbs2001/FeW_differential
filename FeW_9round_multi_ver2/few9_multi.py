l = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1]
x9 = [0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,0,0]

def fix(var, array):
    con = ''
    for i in range(32):
        con = con + var + str(i) + ' = ' + str(array[i]) + '\n'
    return con

with open('setValue.txt','w') as f:
    # 入力の上位32 bit
    tmp = fix('L', l)
    print(tmp, file = f)
    # 入力の下位32 bit
    tmp = fix('X0_', x0)
    print(tmp, file = f)
    # 出力の上位32 bit
    tmp = fix('X8_', x8)
    print(tmp, file = f)
    # 出力の下位32 bit
    tmp = fix('X9_', x9)
    print(tmp, file = f)

