def bubble_sort(unsorted_list):
    print(unsorted_list)
    
def main():
    unsorted_list = list(map(int, input("Enter elements: ").split()))
    bubble_sort(unsorted_list)
    
main()