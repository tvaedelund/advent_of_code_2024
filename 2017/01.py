def solve_1(captcha):
    return sum(int(captcha[i]) for i in range(len(captcha)) if captcha[i] == captcha[(i + 1) % len(captcha)])

def solve_2(captcha):
    steps = len(captcha) // 2
    return sum(int(captcha[i]) for i in range(len(captcha)) if captcha[i] == captcha[(i + steps) % len(captcha)])

with open('2017/data/01.txt', 'r') as file:
    input = file.read().strip()

print(solve_1("1122"))
print(solve_1("1111"))
print(solve_1("1234"))
print(solve_1("91212129"))
print("Result 1: " + str(solve_1(input)))

print(solve_2("1212"))
print(solve_2("1221"))
print(solve_2("123425"))
print(solve_2("123123"))
print(solve_2("12131415"))
print("Result 2: " + str(solve_2(input)))
