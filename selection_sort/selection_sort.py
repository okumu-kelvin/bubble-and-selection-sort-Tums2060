def selection_sort(arr):
    n = len(arr)
    
    # print(arr)
    
    for i in range (n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    print("Sorted List: ", arr)
    
    
    
    
def main():
    arr = list(map(int, input("Enter elements, space: ").split()))
    selection_sort(arr)
    
main()