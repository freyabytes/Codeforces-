# #####
# This is the easy version of the problem. The difference between the versions is that in this version, in one operation, the coordinate of a point changes by exactly 1
# .

# Unemployed ∗
#  Angel places three points A
# , B
# , and C
#  at the origin.

# You must perform exactly n
#  operations of the following type: choose one of these points and increase or decrease one of its coordinates by 1
# . In other words, if the chosen point has coordinates (x,y)
# , in one operation you may move it to (x+1,y)
# , (x−1,y)
# , (x,y+1)
# , or (x,y−1)
# .

# Unemployed ∗
#  Angel asks you to find the maximum doubled area of triangle ABC
#  after all operations are performed. As she is your idol, you cannot refuse her.

# Since Unemployed ∗
#  Angel is very smart, she can show that the value of interest is always an integer.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.

# The only line of each test case contains one integer n
#  (2≤n≤1000
# ) — the number of operations.

# Output
# For each test case, output one integer — the maximum doubled area of triangle ABC
# .
# #####

import sys



def solve():
    # Read all inputs from satndard input at once and split by whitespace
    input_data=sys.stdin.read().split()
    
    if not input_data:
        return
    
    # t= number of test cases
    t=int(input_data[0])
    
    # Process each n from the remaining data
    for i in range(1,t+1):
        n=int(input_data[i])
        
        # Calculate the maximum doubled area using floor diviison (//)
        ans=(n*n)//4
        
        print(ans)

if __name__ == '__main__':
    solve()