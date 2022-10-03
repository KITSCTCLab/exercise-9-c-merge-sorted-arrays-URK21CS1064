from typing import List
def merge(a,m,b,n) :
    
    mp=[]
    for i in range(m+1):
        if (m>i):
            mp.append(a[i])
        else:
            for j in range(n):
                if (n>j):
                    mp.append(b[j])
    print(mp)
        
nums1 = []
nums2 = []
for item in input().split(', '):
    nums1.append(int(item))
for item in input().split(', '):
    nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
