with open("day-2/input.txt", "r") as infile:
    movements = infile.read().split("\n")
    up_down = 0
    forward = 0

    for movement in movements:
        direction, cardinality = movement.split(" ")
        value = int(cardinality)
        if direction == "forward":
            forward += value
        if direction == "up":
            up_down -= value
        if direction == "down":
            up_down += value

    print("part 1: ", up_down * forward)

    horizontal = 0
    depth = 0
    aim = 0

    for movement in movements:
        direction, cardinality = movement.split(" ")
        value = int(cardinality)
        if direction == "down":
            aim += value
        if direction == "up":
            aim -= value
        if direction == "forward":
            horizontal += value
            depth += value * aim

    print("part 2: ", horizontal * depth)
