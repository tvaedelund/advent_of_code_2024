input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open('data/02_data.txt', 'r') as file:
    input = file.read()

data = [list(map(int, line.split())) for line in input.strip().split('\n')]

def is_monotonic(arr):
    return all(x <= y for x, y in zip(arr, arr[1:])) or all(x >= y for x, y in zip(arr, arr[1:]))

def is_valid_difference(arr):
    return all(1 <= abs(x - y) <= 3 for x, y in zip(arr, arr[1:]))

results_1 = [is_monotonic(row) and is_valid_difference(row) for row in data]
print("Result 1: " + str(sum(results_1)))

results_2 = []
for row in data:
    valid = False
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if is_monotonic(new_row) and is_valid_difference(new_row):
            valid = True
            break
    results_2.append(valid)

print("Result 2: " + str(sum(results_2)))