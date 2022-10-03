
def merge(a,m,b,n) :
    mp=[]
    if m>n:
        ch=m
    else:
        ch=n
    flag=0
    if a[0]<b[0]:
        for i in range(ch+1):
            if (m>i):
                mp.append(a[i])
            elif (flag==0):
                for j in range(n):
                    if (n>j):
                        mp.append(b[j])
                        flag=1
    else:
        for i in range(ch+1):
            if (n>i):
                mp.append(b[i])
            elif (flag==0):
                for j in range(m):
                    if (m>j):
                        mp.append(a[j])
                        flag=1
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
