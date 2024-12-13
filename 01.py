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
    result = 0
    for i in range(0, len(column1)):
        result += abs(column1[i] - column2[i])
    return result

def solve_2():
    result = []
    for i in range(len(column1)):
        for j in range(len(column2)):
            if column1[i] == column2[j]:
                result.append(column1[i])
    return sum(result)

print("Result 1: " + str(solve_1()))
print("Result 2: " + str(solve_2()))
