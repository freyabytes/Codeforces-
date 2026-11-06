# A2. 15K4JR3B (Hard Version)
# time limit per test1 second
# memory limit per test256 megabytes
# — Did you know if you connect Park Kultury, a point not in the northeast, and one more on a map, you'll look like an idiot?
# — No, I did not know that. Is that true?

# This is the hard version of the problem. The difference between the versions is that in this version, in one operation, a point coordinate changes by a power of two.

# Unemployed ∗
#  Angel places three points A
# , B
# , and C
#  at the origin, and also gives you an array a
#  of length n
# .

# You must perform exactly n
#  operations. During the i
# -th operation, choose one of these points and increase or decrease one of its coordinates by 2ai
# . In other words, if the chosen point has coordinates (x,y)
# , then in the i
# -th operation you may move it to (x+2ai,y)
# , (x−2ai,y)
# , (x,y+2ai)
# , or (x,y−2ai)
# .

# Unemployed ∗
#  Angel asks you to find the maximum doubled area of triangle ABC
#  after all operations are performed. As she is your idol, you cannot refuse her.

# Since Unemployed ∗
#  Angel is very smart, she can show that the value of interest is always an integer.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.

# The first line of each test case contains one integer n
#  (2≤n≤100
# ) — the length of array a
#  and the number of operations.

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (0≤ai≤24
# ) — the elements of array a
# .

# Output
# For each test case, output one integer — the maximum doubled area of triangle ABC
import sys



def solve():
    # Read all inputs from satndard input at once and split by whitespace
    input_data=sys.stdin.read().split()
    
    if not input_data:
        return
    
    # t= number of test cases
    iterator=iter(input_data)
    t=int(next(iterator))
    out=[]
    
    for _ in range(t):
        n= int(next(iterator))
        a=[int(next(iterator)) for _ in range(n)]
        
        #Count frequebcies of each power of 2
        cnt = [0] * 25
        for x in a:
            cnt[x]+=1
        total_sum=sum(2**x for x in a)
        
        # rem[i] stores the sum of all elements from bit 0 up to i-1
        rem=[0] * 26
        for i in range(1,26):
            rem[i]=rem[i-1]+cnt[i-1]*(2**(i-1))

        current ={0}
        max_ans=0
        
        for i in range(24,-1,-1):
            next_set=set()
            for d in current:
                for k in range(cnt[i]+1):
                    new_d = abs(2*d +k -(cnt[i]-k))
                    
                    if new_d * (2**i)>rem[i]:
                        final_diff=new_d*(2**i)-rem[i]
                        ans=(total_sum+final_diff) * (total_sum-final_diff)//4
                        max_ans=max(max_ans,ans)
                    else:
                        next_set.add(new_d)
            current=next_set
        for d in current:
            final_diff=d
            ans=(total_sum+final_diff)*(total_sum-final_diff)//4
            max_ans=max(max_ans,ans)
        out.append(str(max_ans))
    
    print('\n'.join(out))
        
if __name__ == '__main__':
    solve()