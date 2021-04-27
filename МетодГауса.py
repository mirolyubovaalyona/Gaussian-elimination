import numpy as np
import sys


n = int(input('Количество неизвестных: '))

a = np.zeros((n,n))
b = np.zeros(n)

for i in range(n):
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

for i in range(n):
        b[i] = float(input( 'b['+str(i)+']='))


def f(n, a, b):
    x = np.zeros(n)
    m = np.zeros((n,n+1))
    mm = np.zeros(n+1)

    for i in range(n):
        for j in range(n):
            m[i][j]=a[i][j]
        m[i][n]=b[i]

    for i in range(n+1):
        m[0][i]=m[0][i]/a[0][0]
    print(m)

    for k in range(1, n):
        print(k)

        for kk in range(k):
            for i in range(n+1):
                mm[i]=m[kk][i]*m[k][kk]
            print("mm\n", mm)
            for i in range(n+1):
                m[k][i]-=mm[i]
            print('вычитание предыдущих к\n', m)

        q=m[k][k]
        for j in range(n+1):
            m[k][j]=m[k][j]/q
            print('деление\n', m)

        for kk in range(k):
            for i in range(n+1):
                mm[i]=m[kk][k]*m[k][i]
            for i in range(n+1):
                m[kk][i]-=mm[i]
        print('vz', m)

    for i in range(n):
        x[i]=m[i][n]
        
    return x

x=f(n, a, b)

# Displaying solution
print('Теперь известные элементы: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
