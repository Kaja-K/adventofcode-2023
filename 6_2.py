def day6(race_duration, record_distance):
    ways = 0
    for hold_time in range(1, race_duration):
        remaining_time = race_duration - hold_time
        velocity = hold_time
        distance = remaining_time * velocity
        if distance > record_distance:
            ways += 1
    return ways


win1 = day6(42686985, 284100511221341)
print(win1)
