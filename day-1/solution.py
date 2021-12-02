with open("day-1/input.txt", "r") as infile:
    count = 0
    lines = infile.read().split("\n")
    for index, number in enumerate(lines):
        if int(number) > int(lines[index - 1]):
            count += 1

    print(count)

    triple_count = 0
    previous_value = 10000000
    for index in range(len(lines) - 2):
        value = int(lines[index]) + int(lines[index + 1]) + int(lines[index + 2])
        if int(value) > previous_value:
            triple_count += 1
        previous_value = value

    print(triple_count)
