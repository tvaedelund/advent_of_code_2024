input = """0
3
0
1
-3"""

with open('2017/data/05.txt', 'r') as file:
    input = file.read()

data = list(map(int, input.split()))

def solve_1(instructions):
    i = 0
    steps = 0
    while i < len(instructions):
        offset = instructions[i]
        instructions[i] += 1
        i += offset
        steps += 1
    return steps

def solve_2(instructions):
    i = 0
    steps = 0
    while i < len(instructions):
        offset = instructions[i]
        if offset >= 3:
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i += offset
        steps += 1
    return steps

# Create a copy of the data list for each function call to avoid modifying the original data
print("Result 1: " + str(solve_1(data.copy())))
print("Result 2: " + str(solve_2(data.copy())))