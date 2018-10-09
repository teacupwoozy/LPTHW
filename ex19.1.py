def point_count(bird1, bird2, bird3):
    print(f"At this point, bird1 was heard {bird1} times.")
    print(f"At this point, bird2 was heard {bird2} times.")
    print(f"At this point, bird3 was heard {bird3} times.")

print("Transect #1: ")
point_count(5, 0, 2)

print("Transect #2: ")
point_count(1 + 4, 0 + 1 + 3, 8 + 5 + 0)

# This goves "None" Not sure why...?
call_point_count = point_count(2, 5, 6)
print(call_point_count)