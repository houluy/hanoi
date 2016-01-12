from time import sleep
 
def disp_sym(num, sym):
        print(sym*num, end='')
 
#recusion
def hanoi(a, b, c, n, tray_num):
    if n == 1:
        move_tray(a, c)
        disp(tray_num)
        sleep(0.7)
 
    else:
        hanoi(a, c, b, n-1, tray_num)
        move_tray(a, c)
        disp(tray_num)
        sleep(0.7)
        hanoi(b, a, c, n-1, tray_num)
 
def move_tray(a, b):
    for i in a:
        if i != 0:
            for j in b:
                if j != 0:
                    b[b.index(j) - 1] = i
                    a[a.index(i)] = 0
                    return
            b.append(i)
            b.pop(0)
            a[a.index(i)] = 0
            return
     
def disp(tray_num):
    global a, b, c
    for i in range(tray_num):
        for j in ['a', 'b', 'c']:
            disp_sym(5, ' ')
            eval('disp_sym(tray_num - ' + j + "[i], ' ')")
            eval('disp_sym(' + j + "[i], '=')")
            disp_sym(1, '|')
            eval('disp_sym(' + j + "[i], '=')")
            eval('disp_sym(tray_num - ' + j + "[i], ' ')")
 
        print()
 
    print('---------------------------------------------------------------------------')
 
tray_num=int(input("Please input the number of trays:"))
tray=[]
for i in range(tray_num):
    tray.append(i + 1)
a=[0]*tray_num
b=a[:]
c=a[:]
 
a = tray[:]
disp(tray_num)
hanoi(a, b, c, tray_num, tray_num)