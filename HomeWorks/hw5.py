import time 

def search(nums, target):
    first = 0
    last = len(nums) -1
    while first <= last:
        mid = first + (last - first) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9
start = time.time()
result = search(nums,target)
end = time.time()

print(search(nums,target))
print(f"Execution time: {end - start} seconds")