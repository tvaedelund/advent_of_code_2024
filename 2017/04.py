def solve_1(s: str):
    orig = s.split()
    unique = set(orig)
    return len(unique) == len(orig)

# print(solve_1("aa bb cc dd ee"))
# print(solve_1("aa bb cc dd aa"))
# print(solve_1("aa bb cc dd aaa"))

def solve_2(s: str):
    orig = s.split()
    unique = set(orig)
    revers = set(w[::-1] for w in unique)
    return bool(unique & revers) == False

print(solve_2("abcde fghij"))
print(solve_2("abcde xyz ecdab"))
print(solve_2("a ab abc abd abf abj"))
print(solve_2("iiii oiii ooii oooi oooo"))
print(solve_2("oiii ioii iioi iiio"))

with open('2017/data/04.txt', 'r') as file:
    input = file.read().split('\n')

print("Result1: " + str(sum(solve_1(row) for row in input)))
print("Result2: " + str(sum(solve_2(row) for row in input)))
