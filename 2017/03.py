def get_coords(n):
    if n == 1:
        return (0, 0)  # Special case for the first number
    
    # Layer calculation: the layer is determined by how far from (0,0) the number lies
    layer = 0
    while (2 * layer + 1) ** 2 < n:
        layer += 1
    
    # Start of the layer
    start_of_layer = (2 * (layer - 1) + 1) ** 2 if layer > 0 else 1
    side_length = 2 * layer  # Side length of the current layer's square
    offset = n - start_of_layer - 1  # Position in the layer
    
    # Determine which side the number lies on
    side = offset // side_length
    position_in_side = offset % side_length
    
    # Calculate coordinates based on the side
    if side == 0:  # Bottom side (moving right)
        x, y = layer, -layer + 1 + position_in_side
    elif side == 1:  # Left side (moving up)
        x, y = layer - 1 - position_in_side, layer
    elif side == 2:  # Top side (moving left)
        x, y = -layer, layer - 1 - position_in_side
    elif side == 3:  # Right side (moving down)
        x, y = -layer + 1 + position_in_side, -layer
    
    return x, y

def solve_1(n):
    x, y = get_coords(n)
    return abs(x) + abs(y)

def get_adjacent_sum(coords, current):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adjacent = [(current[0] + dx, current[1] + dy) for dx, dy in directions]
    adjacent_sum = sum(coords.get(a, 0) for a in adjacent)
    return adjacent_sum

def solve_2():
    i = 1
    result = 0
    coords = {(0,0): 1}
    while result < 277678:
        i += 1
        pos = get_coords(i)
        result = get_adjacent_sum(coords, pos)
        coords[pos] = result
    return result


# def print_spiral(n):
#     coords = {get_coords(i): i for i in range(1, n + 1)}
#     min_x = min(x for x, y in coords.keys())
#     max_x = max(x for x, y in coords.keys())
#     min_y = min(y for x, y in coords.keys())
#     max_y = max(y for x, y in coords.keys())
    
#     for y in range(max_y, min_y - 1, -1):
#         for x in range(min_x, max_x + 1, 1):
#             if (x, y) in coords:
#                 print(f"{coords[(x, y)]:3}", end=" ")
#             else:
#                 print("   ", end=" ")
#         print()

# print_spiral(25)

# print(solve_1(1))
# print(solve_1(12))
# print(solve_1(13))
# print(solve_1(23))
# print(solve_1(1024))
print("Result 1: " + str(solve_1(277678)))
print("Result 2: " + str(solve_2()))
