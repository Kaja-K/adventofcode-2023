def day4(line):
    cards = line.splitlines()
    points = 0

    for card in cards:
        _, card = card.split(": ")
        sets = card.split(" | ")
        side1, side2 = sets[0].split(), sets[1].split()

        card_points = 0
        point = 1

        for num in side1:
            if num in side2:
                card_points = 2 ** (point - 1)
                point += 1

        points += card_points

    return points


with open("4.txt", "r") as f:
    data = f.read()
    print(day4(data))

with open("test.txt", "r") as f:
    data = f.read()
    print(day4(data))
