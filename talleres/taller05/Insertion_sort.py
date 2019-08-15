# Insertion sort algorithm;

def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while j >= 0:
            if value < list[j]:
                list[j + 1] = list[j]
                list[j] = value
                j -= 1
            else:
                break
list = [7, 8, 45, 1, 9, 10, 2, 15, 0, 5]
insertion_sort(list)
print(list)
