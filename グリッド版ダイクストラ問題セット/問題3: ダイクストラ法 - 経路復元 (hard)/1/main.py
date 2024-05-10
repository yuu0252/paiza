import heapq

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class State:
    def __init__(self, x, y, cost, ref):
        self.x = x
        self.y = y
        self.cost = cost
        self.ref = ref

    def __hash__(self):
        return (self.x << 16) | self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.cost < other.cost
    
def dijkstra(h, w, t, sx, sy, gx, gy):
    open_list = []
    heapq.heapify(open_list)
    closed = set()
    initial_state = State(sx, sy, t[sy][sx], None)
    heapq.heappush(open_list, initial_state)

    
    while open_list:
        st = heapq.heappop(open_list)

        if st.x == gx and st.y == gy:
            return st
        
        if st in closed:
            continue

        closed.add(st)

        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]

            if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                continue

            ncost = st.cost + t[ny][nx]
            heapq.heappush(open_list, State(nx, ny, ncost, st))

    return -1


h, w = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(h)]
st = dijkstra(h, w, t, 0, 0, w-1, h-1)

print(st.cost)

while st:
    print("--")
    for y in range(h):
        for x in range(w):
            s = str(t[y][x])
            if st.x == x and st.y == y:
                s = "*" + s
            else:
                s = " " + s
            print(s, end="")
        print()
    
    st = st.ref