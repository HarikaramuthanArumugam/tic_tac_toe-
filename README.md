# AI Search Algorithm Lab – Tic-Tac-Toe

## 1. Greedy Best-First Search

### Explanation

Greedy Best-First Search is an informed search algorithm that selects the next state based on a heuristic function. It chooses the state that appears most promising according to the heuristic value.

In Tic-Tac-Toe, a heuristic can evaluate possible moves by considering winning opportunities, blocking the opponent, and controlling useful positions on the board.

### Algorithm

1. Start with the current game state.
2. Generate all possible next moves.
3. Evaluate each resulting state using a heuristic function.
4. Select the state with the best heuristic value.
5. Continue until a goal state is reached or no states remain.

### Python Code

```python
import heapq

def greedy_best_first_search(start, goal, graph, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return visited

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 4,
    'E': 0,
    'F': 1
}

print(greedy_best_first_search('A', 'E', graph, heuristic))
```

## 2. A* Search

### Explanation

A* Search is an informed search algorithm that uses both the cost already incurred and the estimated cost remaining to reach the goal.

Its evaluation function is:

**f(n) = g(n) + h(n)**

* `g(n)` represents the cost from the initial state to the current state.
* `h(n)` represents the estimated cost from the current state to the goal.
* `f(n)` represents the estimated total cost.

A* selects the state with the lowest evaluation value.

### Algorithm

1. Add the initial state to the priority queue.
2. Set the initial path cost to zero.
3. Select the state with the lowest `f(n)` value.
4. Check whether the selected state is the goal.
5. Generate successor states and calculate their costs.
6. Update the costs when a better path is found.
7. Repeat until the goal is found or the queue becomes empty.

### Python Code

```python
import heapq

def a_star_search(start, goal, graph, heuristic):
    priority_queue = [(heuristic[start], 0, start)]
    cost = {start: 0}
    parent = {start: None}

    while priority_queue:
        _, current_cost, current = heapq.heappop(priority_queue)

        if current_cost != cost[current]:
            continue

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor, edge_cost in graph.get(current, []):
            new_cost = cost[current] + edge_cost

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                f_value = new_cost + heuristic[neighbor]
                heapq.heappush(
                    priority_queue,
                    (f_value, new_cost, neighbor)
                )

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('E', 1)],
    'E': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 1,
    'E': 0
}

print(a_star_search('A', 'E', graph, heuristic))
```

## 3. AO* Search

### Explanation

AO* Search is a heuristic search algorithm designed for AND-OR graphs.

* **OR node:** One suitable child is enough to solve the node.
* **AND node:** All required child nodes must be solved.

AO* selects promising partial solutions and updates estimated costs as the search progresses. It is useful for problems that can be divided into subproblems.

### Algorithm

1. Start with the initial problem node.
2. Assign heuristic estimates to the nodes.
3. Select the most promising unsolved node.
4. Expand the selected node.
5. Calculate the costs of its alternatives.
6. For an OR node, select the least-cost alternative.
7. For an AND node, combine the costs of all required children.
8. Update parent costs and continue until the initial node is solved.

### Python Code

```python
def ao_star(graph, heuristic, start):
    solution = {}

    def solve(node):
        if node not in graph or not graph[node]:
            return heuristic[node]

        best_cost = float("inf")
        best_child = None

        for option in graph[node]:
            if isinstance(option, list):
                cost = sum(solve(child) for child in option)
            else:
                cost = solve(option)

            if cost < best_cost:
                best_cost = cost
                best_child = option

        solution[node] = best_child
        heuristic[node] = best_cost

        return best_cost

    total_cost = solve(start)
    return total_cost, solution


graph = {
    'A': [['B', 'C'], ['D']],
    'B': [],
    'C': [],
    'D': []
}

heuristic = {
    'A': 10,
    'B': 2,
    'C': 3,
    'D': 7
}

cost, solution = ao_star(graph, heuristic, 'A')

print("Solution cost:", cost)
print("Selected solution:", solution)
```

## 4. Memory-Bounded Heuristic Search

### Explanation

Memory-bounded heuristic search refers to search techniques that limit memory usage while exploring states. Examples include Simplified Memory-Bounded A* (SMA*) and Recursive Best-First Search (RBFS).

These methods are useful when a search problem has too many states to store in memory. Depending on the method, less promising states may be discarded while information is retained to reconsider alternatives later.

### Algorithm

1. Start from the initial state.
2. Evaluate states using path cost and heuristic information.
3. Select a promising state for expansion.
4. Generate successor states.
5. Check whether the memory limit has been reached.
6. If necessary, discard a less promising state according to the chosen method.
7. Preserve enough information to reconsider alternatives.
8. Continue until a solution is found or the search fails.

### Python Code

The following is a simplified memory-limited heuristic search demonstration. It is **not a complete implementation of SMA* or RBFS**.

```python
import heapq

def memory_limited_search(graph, heuristic, start, goal, limit):
    frontier = [(heuristic[start], start)]
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return current

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(
                    frontier,
                    (heuristic[neighbor], neighbor)
                )

        # Keep only the most promising states.
        if len(frontier) > limit:
            frontier = heapq.nsmallest(limit, frontier)
            heapq.heapify(frontier)

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 4,
    'E': 0,
    'F': 1
}

print(memory_limited_search(graph, heuristic, 'A', 'E', 2))
```

## Conclusion

This project explores four heuristic search techniques: Greedy Best-First Search, A* Search, AO* Search, and Memory-Bounded Heuristic Search. These algorithms demonstrate different approaches to evaluating states, selecting promising alternatives, and managing the search process. The examples provide a foundation for understanding AI search concepts through practical Python programs.
