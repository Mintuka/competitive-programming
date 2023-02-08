class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        buses = [set(route) for route in routes]
        allRoutes = defaultdict(set)
        for bus,bus_routes in enumerate(buses):
            for route in bus_routes:
                allRoutes[route].add(bus)
                
        steps = 0
        visited = set()
        queue = deque(list(allRoutes[source]))
        while queue:
            size = len(queue)
            for _ in range(size):
                bus = queue.popleft()
                if target in buses[bus]:
                    return steps+1
                if bus in visited:
                    continue
                visited.add(bus)

                new_buses = set()
                for route in buses[bus]:
                    new_buses |= allRoutes[route]
                for bus in new_buses:
                    if bus not in visited:
                        queue.append(bus)
            steps += 1
            
        return -1