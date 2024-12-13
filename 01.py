from collections import Counter

input = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open('data/01_data.txt', 'r') as file:
    input = file.read()

# split input into one array per column
lines = input.strip().split('\n')
column1 = []
column2 = []

for line in lines:
    col1, col2 = map(int, line.split())
    column1.append(col1)
    column2.append(col2)
    
column1 = sorted(column1)
column2 = sorted(column2)

def solve_1():
    return sum(abs(c1 - c2) for c1, c2 in zip(column1, column2))

def solve_2():
    count_column2 = Counter(column2)
    result = 0
    for num in column1:
        if num in count_column2:
            result += num * count_column2[num]
    return result

print("Result 1: " + str(solve_1()))
print("Result 2: " + str(solve_2()))
