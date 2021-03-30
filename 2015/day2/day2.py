#! python3

total_square_feet = 0

with open('input.txt') as fo:
    for item in fo:
        dimensions = item.split('x')
        length, width, height = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
        new_dimensions = []
        new_dimensions.append(length * width)
        new_dimensions.append(width * height)
        new_dimensions.append(height * length)
        total = 2 * new_dimensions[0] + 2 * new_dimensions[1] + 2 * new_dimensions[2] + min(new_dimensions)
        total_square_feet += total

print(total_square_feet)

total_ribbon = 0

with open('input.txt') as fo:
    for item in fo:
        dimensions = item.split('x')
        dimensions = list(map(int, dimensions))
        dimensions.sort()
        total = (dimensions[0] + dimensions[0] + dimensions[1] + dimensions[1]) + (dimensions[0] * dimensions[1] * dimensions[2])
        total_ribbon += total

print(total_ribbon)