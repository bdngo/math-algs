SIZE = 8
def find_paths(start, dest):
    (start_x, start_y), (dest_x, dest_y) = start, dest
    if start_x == dest_x and start_y == dest_y:
        return 1
    if start_y >= SIZE or start_y > dest_y:
        return 0
    if start_x <= 0:
        return find_paths((start_x + 1, start_y + 1), dest)
    if start_x >= SIZE:
        return find_paths((start_x - 1, start_y + 1), dest)
    return find_paths((start_x - 1, start_y + 1), dest) \
            + find_paths((start_x + 1, start_y + 1), dest)

print(find_paths((1, 0), (2, 7)))
