largest_so_far = -1
print('largest_so_far = ', largest_so_far)

for largest in [9, 41, 12, 3, 74, 15]:

    if largest > largest_so_far:
        largest_so_far = largest
    print(largest, largest_so_far)
print('updated largest = ', largest_so_far)
