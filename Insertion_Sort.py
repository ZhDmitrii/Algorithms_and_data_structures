def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


# my_list = [64, 34, 25, 12, 22, 11, 90]
my_list = input().split(",")
my_list = list(map(int, my_list))
insertion_sort(my_list)
print("Отсортированный список:", my_list)
