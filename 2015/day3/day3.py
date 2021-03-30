#! python3

positions = {}
x, y = 0, 0
position = (x, y)
positions[position] = 1

positions2 = {}
x2, y2 = 0, 0
position2 = (x2, y2)

santas_turn = True

with open('input.txt') as fo:
    for item in fo:
        for i in range(len(item)):
            if santas_turn:
                if item[i] == '>': x += 1
                elif item[i] == '<': x -= 1
                elif item[i] == '^': y += 1
                elif item[i] == 'v': y -= 1
                position = (x, y)
                if position not in positions2:
                    if position in positions:
                        positions[position] += 1
                    else:
                        positions[position] = 1
                santas_turn = False
            else:
                if item[i] == '>': x2 += 1
                elif item[i] == '<': x2 -= 1
                elif item[i] == '^': y2 += 1
                elif item[i] == 'v': y2 -= 1
                position2 = (x2, y2)
                if position2 not in positions:
                    if position2 in positions2:
                        positions2[position2] += 1
                    else:
                        positions2[position2] = 1
                santas_turn = True

print(len(positions) + len(positions2))