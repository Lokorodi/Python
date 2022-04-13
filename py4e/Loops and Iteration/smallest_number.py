smallest_so_far = 100
print('before', smallest_so_far)

for tinniest in [12, 3, 25, 50, 74, 15, 30]:
    if tinniest < smallest_so_far:
        smallest_so_far = tinniest
    print('after', smallest_so_far)
print('smallest = ', smallest_so_far)
