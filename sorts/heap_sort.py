def heap_sort(arr: list):
    def shift_heap(start, end):
        root = start

        while True:
            child = 2 * root + 1
            if child > end:
                break
            # 找到较大的一个孩子，方面根与后面跟较大的孩子比较
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            # 根与较大的孩子比较，如果小于孩子，则跟孩子交换，将根设定为孩子，进一步优化孩子节点
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in range(len(arr) // 2 - 1, -1, -1):
        shift_heap(start, len(arr) - 1)

    # 堆排序（每次讲root（最大值）放到最后，然后调整大顶堆，直到全部升序）
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        shift_heap(0, end - 1)

    print(arr)


if __name__ == '__main__':
    heap_sort([2, 1, 7, 4, 3, 6])
