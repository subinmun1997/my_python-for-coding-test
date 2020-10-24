def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2 #중간 값 설정
    if array[mid] == target:
        return mid #찾은 경우 mid값 반환
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1) #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else:
        return binary_search(array,target,mid+1,end) #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인

n,target = map(int,input().split())
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)