n = int(input())
nlist = list(map(int,input().split()))
nlist.sort()

m = int(input())
mlist = list(map(int,input().split()))

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        print("yes")
    elif array[mid] > target:
        binary_search(array,target,start,mid-1)
    else:
        binary_search(array,target,mid+1,end)
print("no")


for i in mlist:
    binary_search(nlist,i,0,n-1)