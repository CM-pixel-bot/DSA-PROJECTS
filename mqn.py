
arr = [23, 5, 89, 12, 34, 1, 90]
largest = smallest = arr[0]


for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num


print("Largest element:", largest)
print("Smallest element:", smallest)
