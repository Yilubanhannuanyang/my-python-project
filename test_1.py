import random

def bubble_sort_advance(arr):
    n = len(arr)
    last_swap_idx = n - 1  # 记录最后一次交换的位置
    for i in range(n):
        swapped = False
        current_end = last_swap_idx
        for j in range(current_end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                last_swap_idx = j  # 更新交换位置
        if not swapped:
            break
    return arr

# 测试：30个100以内随机数
test_arr = [random.randint(0, 99) for _ in range(30)]
print("原数组：", test_arr)
bubble_sort_advance(test_arr)
print("排序后：", test_arr)