from typing import List
import bisect
def merge(a,m,b,n) :
    
    mp=[]
    for i in range(m):
        bisect.insort(mp, a[i])
    for i in range(n):
        bisect.insort(mp, b[i])
    for i in mp:
        print(i,end=' ')
        
# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
    nums1.append(int(item))
for item in input().split(', '):
    nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
