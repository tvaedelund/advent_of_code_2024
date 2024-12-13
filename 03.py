import re

input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# with open('data/03_data.txt', 'r') as file:
#     input = file.read()
#     input = input.replace('\n', '')

def solve_1():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input)
    matches = [(int(x), int(y)) for x, y in matches]
    result = 0
    for m in matches:
        result += m[0] * m[1]
    return result

def solve_2():
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, input)
    do = True
    result = 0
    for match in matches:
        if match == 'do()':
            do = True
        elif match == "don't()":
            do = False
        else:
            if do:
                x, y = match
                result += int(x) * int(y)
    return result

print("Result 1: " + str(solve_1()))
print("Result 2: " + str(solve_2()))
