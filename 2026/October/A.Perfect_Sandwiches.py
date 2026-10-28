
import math
t=int(input())
res=[]
for i in range(t):
    a,b=map(int,input().split())
 
    
    if b>=a:
        res.append(-1)
    else:
        res.append(min(b,a-b))
    

print(*res,sep="\n")