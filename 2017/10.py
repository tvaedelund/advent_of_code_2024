def reverse_sublist(lst, start, length):
    n = len(lst)
    sublist = [lst[(start + i) % n] for i in range(length)]
    sublist.reverse()
    for i in range(length):
        lst[(start + i) % n] = sublist[i]

lst = list(range(256))
input = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]
skip_size = 0
pos = 0
for length in input:
    reverse_sublist(lst, pos, length)
    pos += length
    pos += skip_size
    skip_size += 1

print("Result 1: " + str(lst[0] * lst[1]))
