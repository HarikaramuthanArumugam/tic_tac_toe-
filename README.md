AI Search Algorithm Lab – Tic-Tac-Toe

Project Description

AI Search Algorithm Lab is an interactive web application that demonstrates Artificial Intelligence search techniques through a Tic-Tac-Toe game.

The application provides a game board where users can play and explore how different search algorithms select possible moves. It also provides information about algorithm decisions and game results.

The project is developed using Python and Streamlit.

Objectives

- To understand heuristic search techniques through a practical example.
- To explore how AI evaluates possible game states.
- To compare different search strategies.
- To provide an interactive environment for learning AI search algorithms.

Search Algorithms

1. Greedy Best-First Search

Definition:

Greedy Best-First Search is an informed search algorithm that selects the next state based on a heuristic function. It chooses the state that appears most promising according to the estimated value of the heuristic.

Working Principle:

1. Start with the current game state.
2. Generate the possible next moves.
3. Evaluate the resulting states using a heuristic function.
4. Select the state with the most promising heuristic value.
5. Continue until the goal is reached or the search stops.

Pseudocode:

GreedyBestFirstSearch(initial_state):
    Create a priority queue
    Add initial_state to the queue

    while queue is not empty:
        current = state with best heuristic value

        if current is a goal:
            return current

        Generate possible next states

        for each next_state:
            Evaluate heuristic(next_state)
            Add next_state to the queue

    return failure

Key Point: Greedy Best-First Search focuses on the estimated desirability of a state. It does not necessarily find the optimal solution.

2. A* Search

Definition:

A* Search is an informed search algorithm that evaluates states using both the cost already incurred and the estimated cost remaining to reach the goal.

Its evaluation function is:

"f(n) = g(n) + h(n)"

Where:

- "g(n)" is the cost from the initial state to the current state.
- "h(n)" is the estimated cost from the current state to the goal.
- "f(n)" is the estimated total cost of the solution through that state.

Working Principle:

1. Add the initial state to the priority queue.
2. Calculate the evaluation value for available states.
3. Select the state with the lowest "f(n)" value.
4. Expand the selected state and generate its successors.
5. Update the costs and parent information when a better path is found.
6. Continue until the goal is reached or no states remain.

Pseudocode:

AStarSearch(initial_state):
    Add initial_state to the priority queue
    Set g(initial_state) = 0

    while queue is not empty:
        current = state with lowest f(n)

        if current is a goal:
            return solution path

        for each successor of current:
            Calculate tentative g value

            if the path is better:
                Update g(successor)
                Calculate f = g + h
                Add or update successor in queue

    return failure

Key Point: A* considers both the cost so far and the estimated remaining cost. Under the appropriate conditions, it can find an optimal solution.

3. AO* Search

Definition:

AO* Search is a heuristic search algorithm designed for AND-OR graphs. It is useful when solving a problem may require choosing between alternatives or completing multiple subproblems.

- OR node: Selecting one suitable child may be sufficient.
- AND node: All required child subproblems must be solved.

Working Principle:

1. Begin with the initial problem node.
2. Use heuristic values to estimate the cost of solving the problem.
3. Select the most promising partial solution.
4. Expand an unsolved node.
5. Update the estimated costs of its parent nodes.
6. Mark solved nodes and propagate the updates.
7. Continue until the initial problem is solved or no solution is available.

Pseudocode:

AOStarSearch(initial_node):
    Initialize heuristic values

    while initial_node is not solved:
        Select the most promising unsolved node
        Expand the selected node
        Evaluate its successors

        Update parent cost estimates
        Mark solved nodes

    return solution graph

Key Point: AO* searches for a solution graph rather than necessarily a single path. Its cost calculations depend on whether a node represents an AND choice or an OR choice.

4. Memory-Bounded Heuristic Search

Definition:

Memory-bounded heuristic search refers to heuristic search methods that limit memory consumption while exploring possible states. They are useful when traditional search algorithms require too much memory.

Examples include Simplified Memory-Bounded A* (SMA*) and Recursive Best-First Search (RBFS).

Working Principle:

1. Start from the initial state.
2. Evaluate states using path cost and heuristic information.
3. Expand promising states.
4. Monitor the available memory.
5. When memory is limited, remove or forget less promising states according to the selected method.
6. Retain sufficient information to revisit alternatives when necessary.
7. Continue searching until a solution is found or the search fails.

Pseudocode:

MemoryBoundedSearch(initial_state):
    Initialize the search frontier

    while a solution has not been found:
        Select a promising state
        Expand the selected state

        if the memory limit is reached:
            Remove a less promising state
            Preserve information for reconsideration

        Update evaluation values

    return solution or failure

Key Point: Memory-bounded search methods trade memory usage against search effort. Their completeness and optimality depend on the particular algorithm and its conditions.

Application Workflow

1. Open the application.
2. Select the required search algorithm from the interface.
3. View the Tic-Tac-Toe game board.
4. Make a move using an available cell.
5. Observe the AI's response and any displayed algorithm information.
6. Continue until the game reaches a terminal state.
7. Review the result and game statistics provided by the application.

Sample Output

The application is expected to display the following types of results, depending on the implemented features:

- Interactive Tic-Tac-Toe game board.
- Selected search algorithm.
- AI decision or heuristic information, if supported.
- Game status such as win, loss, or draw.
- Game statistics, if implemented.

Note: The actual output depends on the features implemented in the application. Add screenshots of the running application below.

Application Screenshot

Add a screenshot of the main game interface here.

Algorithm Output

Add screenshots showing the algorithm selection and its corresponding output here.

Technologies Used

- Python
- Streamlit
- Artificial Intelligence search techniques
- Git and GitHub
- Streamlit Community Cloud for deployment

Project Structure

tic_tac_toe-/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

The project structure above is an example based on the main application and dependency files. Keep the filenames consistent with the actual repository.

Installation and Execution

Prerequisites

- Python installed on the system.
- Git installed on the system.
- Required Python libraries listed in "requirements.txt".

Steps

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>

2. Move into the project directory

cd tic_tac_toe-

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python -m streamlit run app.py

The application will start on a local address provided by Streamlit. Open that address in a browser to use the application locally.

Live Demo

Try the deployed application here:

"Open AI Search Algorithm Lab" (YOUR_STREAMLIT_APP_URL)

Replace the placeholder with the public Streamlit URL of the deployed application.

Future Improvements

- Display the sequence of states explored by each algorithm.
- Show heuristic values for possible moves.
- Provide a step-by-step visualization of search decisions.
- Compare the number of explored states and execution time.
- Add more AI search problems and game environments.

Conclusion

This project provides an interactive way to explore Artificial Intelligence search techniques using Tic-Tac-Toe. It connects theoretical concepts with a practical application and helps learners understand how different search strategies evaluate possible states and make decisions.

Author

Developed as an Artificial Intelligence Search Algorithm Lab project.
