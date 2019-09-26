import numpy as np
'''
[1 12 11 10
 2 13 16 9
 3 14 15 8
 4 5  6  7]


'''

m = -1
n = 0
cnt = 4
lag = 0
MAT = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
cnt_n = 0
cnt_m = 0
od = 4
for i in range(1,17):

    if cnt == cnt_m:
        cnt_m = 0
        lag  = 1
        cnt -= 1

    elif cnt == cnt_n:
        cnt_n = 0
        lag = 0
        od -= 1

    if lag == 0:
        m += 1*pow(-1,od)
        MAT[m][n] = i
        cnt_m += 1
    elif lag == 1:
        n += 1*pow(-1,od)
        MAT[m][n] = i

        cnt_n += 1

print(MAT)
