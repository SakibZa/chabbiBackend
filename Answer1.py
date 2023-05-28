def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_idx = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [int(num) for num in input_list]

sorted_list = selection_sort(input_list)
print("Sorted list:", sorted_list)
