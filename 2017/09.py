def solve_1(stream):
    total_score = 0
    current_score = 0
    garbage = False
    i = 0
    garbage_count = 0

    while i < len(stream):
        if stream[i] == '!':
            i += 1
        elif garbage and stream[i] == '>':
            garbage = False
        elif stream[i] == '<' and not garbage:
            garbage = True
        elif stream[i] == '{' and not garbage:
            current_score += 1
        elif stream[i] == '}' and not garbage:
            total_score += current_score
            current_score -= 1
        elif garbage:
            garbage_count += 1
        i += 1
    
    return (total_score, garbage_count)
           
# print(solve_1("{}"))
# print(solve_1("{{{}}}"))
# print(solve_1("{{},{}}"))
# print(solve_1("{{{},{},{{}}}}"))
# print(solve_1("{<a>,<a>,<a>,<a>}"))
# print(solve_1("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
# print(solve_1("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
# print(solve_1("{{<a!>},{<a!>},{<a!>},{<ab>}}"))

# print(solve_1("<>"))
# print(solve_1("<random characters>"))
# print(solve_1("<<<<>"))
# print(solve_1("<{!>}>"))
# print(solve_1("<!!>"))
# print(solve_1("<!!!>>"))
# print(solve_1('<{o"i!a,<{i<a>'))

with open('2017/data/09.txt', 'r') as file:
    input = file.read()

print("Result 1:" + str(solve_1(input)))
