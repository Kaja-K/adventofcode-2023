def day1(s):
    arr = []
    for line in s.splitlines():
        firstd = 0
        lastd = 0

        for i in line:
            if i.isnumeric():
                if firstd == 0:
                    firstd = int(i)
                    lastd = int(i)
                else:
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
