
arr = [12, 35, 1, 10, 34, 1]


arr = list(set(arr))


if len(arr) < 2:
    print("Array doesn't have enough unique elements")
else:
    
    arr.sort()


    second_smallest = arr[1]
    second_largest = arr[-2]

    print("Second Smallest:", second_smallest)
    print("Second Largest:", second_largest)

