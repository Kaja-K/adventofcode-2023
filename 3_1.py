def day3(x):
    result = 0
    specials = "!@#$%^&*();:_-=+<>/?"
    lines = x.splitlines()
    has_special = False
    number = ""

    for i, line in enumerate(lines):
        for j, digit in enumerate(line):
            if digit.isnumeric():
                number += digit
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        ik = i + k
                        jl = j + l
                        if (
                            0 <= ik < len(lines)
                            and 0 <= jl < len(line)
                            and lines[ik][jl] in specials
                        ):
                            has_special = True
            else:
                if has_special:
                    result += int(number)
                has_special = False
                number = ""

        if has_special:
            result += int(number)
            has_special = False
            number = ""

    return result


with open("test.txt", "r") as f:
    data = f.read()
    print(day3(data))

with open("3.txt", "r") as f:
    data = f.read()
    print(day3(data))
