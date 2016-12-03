get_input_for_day = lambda day: open('inputs/day_%s_input.txt' % str(day))
part_2 = False


def day_1():
    x = 0
    y = 0
    locations = set()

    facing = "N"
    facing_to_incrementation = {
        "N": 1,
        "E": 1,
        "S": -1,
        "W": -1
    }
    facing_to_axis = {
        "N": "y",
        "E": "x",
        "S": "y",
        "W": "x"
    }
    rotate_facing_right = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"
    }
    rotate_facing_left = {
        "N": "W",
        "E": "N",
        "S": "E",
        "W": "S"
    }

    input_line = get_input_for_day(1).readline()
    for instruction in input_line.split(','):
        instruction = instruction.strip()
        rotation = instruction[0]
        distance = int(instruction[1:])

        if rotation == "R":
            facing = rotate_facing_right[facing]
        else:
            facing = rotate_facing_left[facing]

        for _ in xrange(distance):
            command = "{axis} += {incrementation}".format(
                axis=facing_to_axis[facing],
                incrementation=facing_to_incrementation[facing]
            )
            exec command
            if part_2 and (x, y) in locations:
                return abs(x) + abs(y)
            locations.add((x, y))

    total_dist = abs(x) + abs(y)
    return total_dist


def day_2():
    input_file = get_input_for_day(2)

    x = 1
    y = 1
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    if part_2:
        x = 0
        y = 2
        input_matrix = [
            [0, 0, 1, 0, 0],
            [0, 2, 3, 4, 0],
            [5, 6, 7, 8, 9],
            [0, 'A', 'B', 'C', 0],
            [0, 0, 'D', 0, 0],
        ]

    moves = []
    for line in input_file:
        for char in line:
            if char == "U":
                if not part_2 or (y-1 > -1 and input_matrix[y-1][x] != 0):
                    y = max(y-1, 0)
            if char == "D":
                if not part_2 or (y+1 < len(input_matrix) and input_matrix[y+1][x] != 0):
                    y = min(y+1, len(input_matrix)-1)
            if char == "L":
                if not part_2 or (x-1 > -1 and input_matrix[y][x-1] != 0):
                    x = max(x-1, 0)
            if char == "R":
                if not part_2 or (x+1 < len(input_matrix) and input_matrix[y][x+1] != 0):
                    x = min(x+1, len(input_matrix)-1)
        moves.append(input_matrix[y][x])
    return "".join(str(move) for move in moves)


def day_3():
    input_file = get_input_for_day(3)
    count = 0
    row = 0
    triangles = [
        [],
        [],
        []
    ]
    for line in input_file:
        nums = [piece for piece in line.strip().split(" ") if piece]
        first = int(nums[0])
        second = int(nums[1])
        third = int(nums[2])
        if not part_2:
            if first + second > third and first + third > second and second + third > first:
                count += 1
        else:
            row += 1
            triangles[0].append(first)
            triangles[1].append(second)
            triangles[2].append(third)
            if row % 3 == 0:
                if triangles[0][0] + triangles[0][1] > triangles[0][2] \
                        and triangles[0][0] + triangles[0][2] > triangles[0][1] \
                        and triangles[0][1] + triangles[0][2] > triangles[0][0]:
                    count += 1
                if triangles[1][0] + triangles[1][1] > triangles[1][2] \
                        and triangles[1][0] + triangles[1][2] > triangles[1][1] \
                        and triangles[1][1] + triangles[1][2] > triangles[1][0]:
                    count += 1
                if triangles[2][0] + triangles[2][1] > triangles[2][2] \
                        and triangles[2][0] + triangles[2][2] > triangles[2][1] \
                        and triangles[2][1] + triangles[2][2] > triangles[2][0]:
                    count += 1
                triangles[0] = []
                triangles[1] = []
                triangles[2] = []
    return count


if __name__ == '__main__':
    for day in xrange(1, 26):
        if 'day_%s' % day in dir():
            print 'Day %s:' % day
            part_2 = False
            print ' Part 1:', eval('day_%s()' % day)
            part_2 = True
            print ' Part 2:', eval('day_%s()' % day)