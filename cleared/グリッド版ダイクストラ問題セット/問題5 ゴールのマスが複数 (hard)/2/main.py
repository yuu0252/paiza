import heapq

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class State:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __hash__(self):
        return (self.x << 16) | self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.cost < other.cost
    
def dijkstra(h, w, t, sx, sy, gy):
    open_list = []
    closed = set()
    heapq.heapify(open_list)
    initial_state = State(sx, sy, t[sy][sx])
    heapq.heappush(open_list, initial_state)

    costs = [0] * w

    while open_list:
        st = heapq.heappop(open_list)

        
        if st in closed:
            continue

        closed.add(st)
        
        if st.y == gy:
            costs[st.x] = st.cost

        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]

            if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                continue

            heapq.heappush(open_list, State(nx, ny, st.cost + t[ny][nx]))

    return costs

h, w = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(h)]

costs = dijkstra(h, w, t, 0, 0, h-1)
for cost in costs:
    print(cost)