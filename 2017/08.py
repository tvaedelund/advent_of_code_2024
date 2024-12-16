input = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

with open('2017/data/08.txt', 'r') as file:
    input = file.read()

instructions = input.strip().split('\n')
registers = {}
max_value_held = 0

for instruction in instructions:
    parts = instruction.split()
    reg, op, val, _, cond_reg, cond_op, cond_val = parts
    
    if reg not in registers:
        registers[reg] = 0
    if cond_reg not in registers:
        registers[cond_reg] = 0
    
    condition = f"registers['{cond_reg}'] {cond_op} {cond_val}"
    if eval(condition):
        if op == 'inc':
            registers[reg] += int(val)
        elif op == 'dec':
            registers[reg] -= int(val)

    if registers[reg] > max_value_held: max_value_held = registers[reg]

print("Result 1: " + str(max(registers.values())))
print("Result 2: " + str(max_value_held))
