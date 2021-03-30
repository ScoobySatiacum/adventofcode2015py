#! python3

puzzle_input = []
floor = 0
position = 1

with open('input.txt') as fo:
    for i in fo.read():
        if i == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            break
        position += 1

print(position)