from tile import Tile

def bfs(tiles):
    """
    checks if a path exists from start to end
    """
    max_r = len(tiles) - 1
    max_c = len(tiles[0]) - 1

    queue = []
    visited = {}

    queue.append((0, 0))
    visited[0] = set({0})

    while len(queue) > 0:
        node = queue.pop(0)
        if node[0] == max_r and node[1] == max_c:
            return True

        neighbors = []
        neighbors.append((node[0] + 1, node[1]))
        neighbors.append((node[0], node[1] + 1))

        for neighbor in neighbors:

            if neighbor[0] > max_r or neighbor[1] > max_c:
                continue

            if visited.get(neighbor[0]) is None:
                visited[neighbor[0]] = set({})

            if neighbor[1] in visited[neighbor[0]]:
                continue

            visited[neighbor[0]] = set({neighbor[1]})
            if tiles[neighbor[0]][neighbor[1]].passable:
                queue.append(neighbor)
    return False