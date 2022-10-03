from typing import List
def merge(a,m,b,n) :
    mp=[]
    if a[0]<b[0]:
        for i in range(m+1):
            if (m>i):
                mp.append(a[i])
            else:
                for j in range(n):
                    if (n>j):
                        mp.append(b[j])
    else:
        for i in range(n+1):
            if (n>i):
                mp.append(b[i])
            else:
                for j in range(m):
                    if (m>j):
                        mp.append(a[j])
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
