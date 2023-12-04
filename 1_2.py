def day1(s):
    arr = []
    numbers = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3hree",
        "four": "f4ur",
        "five": "f5ve",
        "six": "s6x",
        "seven": "s7ven",
        "eight": "e8ght",
        "nine": "n9ne",
    }
    for line in s.splitlines():
        for key, value in numbers.items():
            line = line.replace(key, str(value))

        firstd = 0
        lastd = 0

        for i in line:
            if i.isnumeric():
                if firstd == 0:
                    firstd = int(i)
                lastd = int(i)

        number = firstd * 10 + lastd
        arr.append(number)

    return sum(arr)


with open("1.txt", "r") as f:
    data = f.read()
    print(day1(data))

"""with open("test.txt", "r") as f:
    data = f.read()
    print(day1(data))"""
