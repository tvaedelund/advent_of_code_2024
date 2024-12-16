input = """5 1 9 5
7 5 3
2 4 6 8"""

input = """5 9 2 8
9 4 7 3
3 8 6 5"""

with open('2017/data/02.txt', 'r') as file:
    input = file.read()

spreadsheet = [list(map(int, line.split())) for line in input.strip().split('\n')]

def solve_1(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)

def solve_2(spreadsheet):
    def find_evenly_divisible(row):
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if row[i] % row[j] == 0:
                    return row[i] // row[j]
                elif row[j] % row[i] == 0:
                    return row[j] // row[i]
        return 0

    return sum(find_evenly_divisible(row) for row in spreadsheet)

print("Result 1: " + str(solve_1(spreadsheet)))
print("Result 2: " + str(solve_2(spreadsheet)))
