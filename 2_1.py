def day2(line):
    games = line.splitlines()
    solution = []
    g = 0

    for game in games:
        _, game = game.split(": ")
        sets = game.split("; ")
        g += 1
        is_valid_game = True

        for s in sets:
            s = s.split(", ")
            green = 0
            blue = 0
            red = 0
            for stones in s:
                count, color = stones.split(" ")
                count = int(count)
                if color == "green":
                    green += count
                if color == "blue":
                    blue += count
                if color == "red":
                    red += count
            if green > 13 or blue > 14 or red > 12:
                is_valid_game = False
                break
            else:
                continue

        if is_valid_game:
            solution.append(g)
    return sum(solution)


with open("2.txt", "r") as f:
    data = f.read()
    print(day2(data))

with open("test.txt", "r") as f:
    data = f.read()
    print(day2(data))
