def search_first_sq(arr: list, target: int)->int:
    low, high = 0, len(arr)-1
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid]==target or arr[mid]<target and arr[mid+1]>target:
            return mid
        elif arr[mid]<target:
            low = mid+1
        elif arr[mid]>target:
            high = mid-1

    return -1


print(search_first_sq([1,2,3,4,6,7], 5))
