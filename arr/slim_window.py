def slimWindow(arr: list, size: int):
    if not arr or len(arr)<size or size==0:
        return []
    
    ans = [max(arr[0: size+1]),]
    for i in range(size, len(arr)):
        if ans[-1] in arr[i-size+1: i]:
            ans.append(max(ans[-1], arr[i]))
        else:
            ans.append(max(arr[i-size+1: size+1]))
    return ans

print(slimWindow([9,3,4,1,5,6], 3))
