def slice_between_first_two(t, value):
    indices = [i for i, v in enumerate(t) if v == value]
    if not indices:
        return tuple()
    if len(indices) == 1:
        return t[indices[0]:]
    return t[indices[0]:indices[1]+1]

print(slice_between_first_two((1, 2, 3), 8))
print(slice_between_first_two((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slice_between_first_two((1, 2, 8, 5, 1, 2, 9), 8))
