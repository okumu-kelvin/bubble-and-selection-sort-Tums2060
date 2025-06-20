def selection_sort(arr):
    n = len(arr)
    
    # print(arr)
    
    for i in range (n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    
        
    
    
    return arr
    
    
    
    
    
    
def main():
    arr = list(map(int, input("Enter elements, space: ").split()))
    sorted_arr = selection_sort(arr)
    print("Sorted List: ", sorted_arr)
    
    
    
if __name__ == "__main__":
    main()