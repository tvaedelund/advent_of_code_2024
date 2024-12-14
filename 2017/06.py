def find_max(banks):
    max_value = max(banks, key=int)
    max_index = banks.index(max_value)
    return max_index

def redistribute(banks, value, pos):
    while value > 0:
        banks[pos] += 1
        value -= 1
        pos = (pos + 1) % len(banks)
        
def solve_1(input):
    banks = list(map(int, input.split()))
    history = []
    while True:
        if banks in history:
            break
        history.append(banks[:])
        max_index = find_max(banks)
        value = int(banks[max_index])
        banks[max_index] = 0
        redistribute(banks, value, (max_index + 1) % len(banks))
    return (len(history), banks)

print("Test 1: " + str((solve_1("0 2 7 0"))[0]))

print("Result 1: " + str((solve_1("4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"))[0]))

def solve_2(input):
    end = (solve_1(input))[1]
    return (solve_1(" ".join(map(str, end))))

print("Test 2: " + str(solve_1("2 4 1 2")))

print("Result 2: " + str(solve_2("4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3")))
