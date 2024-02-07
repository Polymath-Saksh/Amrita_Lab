def binary(arr,n,ele):
    low,high=0,n-1
    
    while high>low:

        mid = (low+high)//2
        if arr[mid] == ele:
            return mid+1
        elif arr[mid]>ele:
            high=mid
        else:
            low=mid

    return -1


if __name__=='__main__':
    arr=[]
    n= int(input("Enter size of array: "))
    for _ in range(n):
        dat=int(input())
        arr.append(dat)
    arr=sorted(arr)

    ele = int(input("Enter element to be search: "))
    bin_val=binary(arr,n,ele)

    if bin_val !=-1:
        print(f'The element is at index {bin_val}')
    else:
        print(f'The element is not present.')