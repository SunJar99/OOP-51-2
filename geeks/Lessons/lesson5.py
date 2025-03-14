lst = [1,2,4,5,6,7,8,9]

def get_element_by_index(lst, index):
    return lst[index]

print(get_element_by_index(lst=lst, index=4))

lst2 = [1,6,2,7,3,8,4,9,2,423,7,23,1,73,45]

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid + 1
    return -1

print(binary_search(lst, target=9))


def find_element(lst, target):
    
    for i in lst:
        if i == target:
            return True
    return False

print(find_element(lst, 10))



lst3 = [2,4,75,61,821,2,12,35,65]

def bubblesort(lst):
    n = len(lst)
    print("for 1 ", range(n))
    for i in range(n):
        print(i)
        print("for 2--", range(n - i - 1))
        for j in range(n - i - 1):
            print("for 3 ----", j)
            if lst[j] > lst[j + 1]:
                print(f"{lst[j]} ----- {lst[j + 1]}") 
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

bubblesort(lst=lst3)
print(lst3)