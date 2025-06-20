def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    
    for i in range (n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                
                
    
    print("Sorted: List: ", unsorted_list)
    
    return unsorted_list
    
def main():
    unsorted_list = list(map(int, input("Enter elements, space: ").split()))
    bubble_sort(unsorted_list)
    
if __name__ == "__main__":
    main()
