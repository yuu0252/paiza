import heapq

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class State:
    def __init__(self, x, y, ticket, cost):
        self.x = x
        self.y = y
        self.ticket = ticket
        self.cost = cost

    def __hash__(self):
        return (self.x << 16) | self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.ticket == other.ticket
    
    def __lt__(self, other):
        return self.cost < other.cost

def dijkstra(h, w, t, sx, sy, gx, gy, ticket):
    open_list = []
    heapq.heapify(open_list)
    closed = set()
    initial_state = State(sx, sy, ticket, t[sy][sx])
    heapq.heappush(open_list, initial_state)

    if ticket > 0:
        initial_state_use_ticket = State(sx, sy, ticket - 1, 0)
        heapq.heappush(open_list, initial_state_use_ticket)

    while open_list:
        st = heapq.heappop(open_list)

        if st.x == gx and st.y == gy:
            return st.cost
        
        if st in closed:
            continue

        closed.add(st)

        for i in range(4):
            nx = st.x + dx[i]
            ny = st.y + dy[i]

            if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                continue

            cost = st.cost

            heapq.heappush(open_list, State(nx, ny, st.ticket, cost + t[ny][nx]))
            if st.ticket > 0:
                heapq.heappush(open_list, State(nx, ny, st.ticket - 1, cost))

    return -1

h, w = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(h)]
n = int(input())
cost = dijkstra(h, w, t, 0, 0, w-1, h-1, n)
print(cost)