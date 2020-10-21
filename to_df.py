#! /usr/bin/env python3 

import pandas as pd
import sys
import time
import numpy as np

strat = time.time()
d = []
row = 0
err_row = 0
for line in sys.stdin:
    row += 1
    c = line.strip().split(',')
    front = c[0:12]
    back = c[len(c)-52:len(c)+1]
    front.extend(back)
    #print(len(front))
    if len(front) != 64:
        print(front)
        print(len(front),row,err_row)
        err_row += 1
    else:
        d.append(front)
end1 = time.time()
print(err_row)

column = d[0]
d.pop(0)
df = pd.DataFrame(d,columns=column)
print(column)
#print(type(df))
print(df.iloc[:,0:6])
end2 = time.time()
print(df.shape)
print("cost time:",end1 - strat,end2 - end1)
