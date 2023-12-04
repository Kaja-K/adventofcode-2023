def day4(line):
    cards = line.splitlines()
    tickets = [1] * len(cards)

    for id, card in enumerate(cards):
        _, card = card.split(": ")
        l, r = card.split(" | ")
        side1, side2 = set(l.split()), set(r.split())
        count = len(side1 & side2)

        for i in range(count):
            tickets[id + 1 + i] += tickets[id]

    return sum(tickets)


with open("4.txt", "r") as f:
    data = f.read()
    print(day4(data))

# with open("test.txt", "r") as f:
#     data = f.read()
#     print(day4(data))
