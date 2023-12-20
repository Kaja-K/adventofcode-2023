def day9(history):
    numbers = [int(num) for num in history]
    diff = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

    if all(i == 0 for i in diff):
        return numbers[-1]
    else:
        next_v = day9(diff)
        return numbers[-1] + next_v


# with open("9.txt", "r") as f:
#     data = f.read()
#     print(day9(data))

with open("test.txt", "r") as f:
    data = f.read()
    print(day9(data))
