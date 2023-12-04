def day2(line):
    games = line.splitlines()
    solution = []

    for game in games:
        _, game = game.split(": ")
        sets = game.split("; ")
        green = 0
        blue = 0
        red = 0

        for s in sets:
            s = s.split(", ")
            for stones in s:
                count, color = stones.split(" ")
                count = int(count)
                if color == "green":
                    green = max(green, count)
                if color == "blue":
                    blue = max(blue, count)
                if color == "red":
                    red = max(red, count)
        power = green * blue * red
        solution.append(power)

    return sum(solution)


with open("2.txt", "r") as f:
    data = f.read()
    print(day2(data))

with open("test.txt", "r") as f:
    data = f.read()
    print(day2(data))
