def solve(path):
    directions = path.split(',')
    x, y, z = 0, 0, 0
    max_distance = 0

    for direction in directions:
        if direction == 'n':
            y += 1
            z -= 1
        elif direction == 's':
            y -= 1
            z += 1
        elif direction == 'ne':
            x += 1
            z -= 1
        elif direction == 'nw':
            x -= 1
            y += 1
        elif direction == 'se':
            x += 1
            y -= 1
        elif direction == 'sw':
            x -= 1
            z += 1
        
        current_distance = max(abs(x), abs(y), abs(z))
        if current_distance > max_distance:
            max_distance = current_distance
           
    return (current_distance, max_distance)
    
# print(solve("ne,ne,ne"))  # Output should be (3, 3)
# print(solve("ne,ne,sw,sw"))  # Output should be (0, 2)
# print(solve("ne,ne,s,s"))  # Output should be (2, 2)
# print(solve("se,sw,se,sw,sw"))  # Output should be (3, 3)

with open('2017/data/11.txt', 'r') as file:
    input = file.read().strip()
    
print("Result 1: " + str(solve(input)[0]))
print("Result 2: " + str(solve(input)[1]))
