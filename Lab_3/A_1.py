x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
if x1>0 and y1>0 and x2>0 and y2>0:
    print('YES, I')
if x1<0 and y1>0 and x2<0 and y2>0:
    print('YES, II')
if x1<0 and y1<0 and x2<0 and y2<0:
    print('YES, III')
if x1>0 and y1<0 and x2>0 and y2<0:
    print('YES, IV')
if x1==0 or x2 ==0 or y1==0 or y2==0:
    print('x, y не могут быть нулями')
else:
    print('NO')