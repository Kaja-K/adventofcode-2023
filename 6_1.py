def day6(race_duration, record_distance):
    ways = 0
    for hold_time in range(1, race_duration):
        remaining_time = race_duration - hold_time
        velocity = hold_time
        distance = remaining_time * velocity
        if distance > record_distance:
            ways += 1
    return ways


win1 = day6(42, 284)
win2 = day6(68, 1005)
win3 = day6(69, 1122)
win4 = day6(85, 1341)
print(win1 * win2 * win3 * win4)

# test1 = day6(7, 9)
# test2 = day6(15, 40)
# test3 = day6(30, 200)
# print(test1, test2, test3)
