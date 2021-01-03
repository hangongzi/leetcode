def search_lost_equal(arr: list, target: int)->int:
    low, high = 0, len(arr)-1
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid]<target:
            low = mid+1
        elif arr[mid]>target:
            high = mid-1
        else:
            if mid==len(arr)-1 or arr[mid+1]!=target:
                return mid
            low = mid+1
    return -1


print(search_lost_equal([1,2,3,4,5,5,6,7], 5))
