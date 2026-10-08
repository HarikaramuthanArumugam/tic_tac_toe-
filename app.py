import streamlit as st
import math

st.set_page_config(
    page_title="AI Search Algorithm Lab",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- DARK THEME AND UI ----------
st.markdown("""
<style>
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #101827 !important;
    color: #F3F6FC !important;
}

[data-testid="stMainBlockContainer"] {
    padding-top: 0.8rem !important;
    padding-bottom: 1rem !important;
    max-width: 100% !important;
}

h1, h2, h3, h4, p, label,
[data-testid="stMarkdownContainer"] {
    color: #F3F6FC !important;
}

[data-testid="stHeader"] {
    background: rgba(16, 24, 39, 0.95) !important;
}

[data-testid="stSidebar"] {
    background: #152236 !important;
}

[data-testid="stMetric"] {
    background: #223750;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #38516F;
}

div.stButton > button {
    background: #223750 !important;
    color: #FFFFFF !important;
    border: 1px solid #52769E !important;
    border-radius: 12px !important;
    min-height: 65px;
    font-size: 23px;
    font-weight: bold;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: #315579 !important;
    border-color: #8CC8FF !important;
}

div.stButton > button:disabled {
    color: #FFFFFF !important;
    opacity: 0.95;
}

[data-testid="stAlert"] {
    border-radius: 10px;
}

hr {
    border-color: #38516F;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🎮 AI Search Algorithm Lab")
st.caption(
    "PRINCIPLES OF ARTIFICIAL INTELLIGENCE  |  "
    "TIC-TAC-TOE SEARCH VISUALIZER"
)

# ---------- ALGORITHMS ----------
ALGORITHMS = {
    "Greedy Best-First Search":
        "Selects a move using an immediate heuristic score. "
        "It does not fully plan for the opponent's future moves.",

    "A* Search — Demo":
        "A* normally uses f(n) = g(n) + h(n). "
        "This prototype uses minimax for its move selection; "
        "it is not a complete A* implementation.",

    "AO* Search — Demo":
        "AO* searches AND-OR graphs. This prototype uses minimax "
        "for move selection; it is not a complete AO* implementation.",

    "Memory-Bounded Search — Demo":
        "This option uses depth-limited minimax. It illustrates "
        "limited-depth search, not a complete memory-bounded algorithm."
}

TESTS = {
    "Fresh game": [""] * 9,

    "Block X from winning": [
        "X", "X", "",
        "", "O", "",
        "", "", ""
    ],

    "Take a winning move": [
        "O", "O", "",
        "X", "X", "",
        "", "", ""
    ],

    "Centre occupied": [
        "", "", "",
        "", "X", "",
        "", "", ""
    ]
}

# ---------- GAME LOGIC ----------
def winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in lines:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]

    if all(board):
        return "Draw"

    return None


def terminal_score(board, depth):
    result = winner(board)

    if result == "O":
        return 10 - depth
    if result == "X":
        return depth - 10
    if result == "Draw":
        return 0

    return None


def heuristic(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    value = 0

    for line in lines:
        cells = [board[i] for i in line]

        if "X" not in cells:
            value += cells.count("O") * 2

        if "O" not in cells:
            value -= cells.count("X") * 2

    return value


def minimax(board, depth, ai_turn,
            alpha=-math.inf, beta=math.inf):

    value = terminal_score(board, depth)

    if value is not None:
        return value, None

    best_move = None

    if ai_turn:
        best_value = -math.inf

        for i in range(9):
            if board[i] == "":
                board[i] = "O"

                value, _ = minimax(
                    board, depth + 1, False, alpha, beta
                )

                board[i] = ""

                if value > best_value:
                    best_value = value
                    best_move = i

                alpha = max(alpha, best_value)

                if alpha >= beta:
                    break

        return best_value, best_move

    best_value = math.inf

    for i in range(9):
        if board[i] == "":
            board[i] = "X"

            value, _ = minimax(
                board, depth + 1, True, alpha, beta
            )

            board[i] = ""

            if value < best_value:
                best_value = value
                best_move = i

            beta = min(beta, best_value)

            if alpha >= beta:
                break

    return best_value, best_move


def limited_minimax(board, depth, ai_turn, limit):
    result = winner(board)

    if result is not None:
        return terminal_score(board, depth), None

    if depth >= limit:
        return heuristic(board), None

    best_move = None

    if ai_turn:
        best_value = -math.inf

        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                value, _ = limited_minimax(
                    board, depth + 1, False, limit
                )
                board[i] = ""

                if value > best_value:
                    best_value = value
                    best_move = i

        return best_value, best_move

    best_value = math.inf

    for i in range(9):
        if board[i] == "":
            board[i] = "X"
            value, _ = limited_minimax(
                board, depth + 1, True, limit
            )
            board[i] = ""

            if value < best_value:
                best_value = value
                best_move = i

    return best_value, best_move


# ---------- AI DECISION ----------
def choose_move(board, algorithm):
    candidates = []

    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            value = heuristic(board)
            board[i] = ""
            candidates.append((value, i))

    if not candidates:
        return None, "No legal moves remain.", []

    if algorithm == "Greedy Best-First Search":
        candidates.sort(key=lambda item: item[0], reverse=True)
        move = candidates[0][1]

        explanation = (
            f"Greedy compared immediate heuristic values and "
            f"selected cell {move + 1}. It does not guarantee "
            "the best final outcome."
        )

    elif algorithm == "Memory-Bounded Search — Demo":
        _, move = limited_minimax(board[:], 0, True, 3)

        explanation = (
            f"Selected cell {move + 1} using depth-limited "
            "minimax with a depth limit of 3. This is a demo, "
            "not a true memory-bounded search implementation."
        )

    else:
        score, move = minimax(board[:], 0, True)

        if algorithm == "A* Search — Demo":
            explanation = (
                f"Selected cell {move + 1} using minimax "
                f"(evaluation score {score}). This is not A*."
            )
        else:
            explanation = (
                f"Selected cell {move + 1} using minimax "
                f"(evaluation score {score}). This is not AO*."
            )

    return move, explanation, candidates


# ---------- SESSION STATE ----------
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "history" not in st.session_state:
    st.session_state.history = []

if "explanation" not in st.session_state:
    st.session_state.explanation = "Choose a square to begin."

if "candidates" not in st.session_state:
    st.session_state.candidates = []

if "last_move" not in st.session_state:
    st.session_state.last_move = None

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("⚙️ Lab Controls")

    algorithm = st.selectbox(
        "Choose Search Algorithm",
        list(ALGORITHMS.keys())
    )

    st.markdown("---")
    st.subheader("🧪 Test Cases")

    test_name = st.selectbox(
        "Choose a test board",
        list(TESTS.keys())
    )

    if st.button("📥 Load Test Case", use_container_width=True):
        st.session_state.board = TESTS[test_name][:]
        st.session_state.history = []
        st.session_state.candidates = []
        st.session_state.last_move = None
        st.session_state.explanation = (
            f"Loaded test case: {test_name}. "
            "The AI will respond after you place X."
        )
        st.rerun()

    if st.button("🔄 Reset Game", use_container_width=True):
        st.session_state.board = [""] * 9
        st.session_state.history = []
        st.session_state.candidates = []
        st.session_state.last_move = None
        st.session_state.explanation = "New game started."
        st.rerun()

    st.markdown("---")
    st.caption(
        "X = Human player\n\n"
        "O = AI player"
    )

# ---------- MAIN DASHBOARD ----------
game_col, info_col = st.columns([1.05, 1])

with game_col:
    st.subheader("🧩 Game Board")
    st.write("Play as X. The AI responds as O.")

    board = st.session_state.board
    game_result = winner(board)

    for row in range(3):
        cols = st.columns(3)

        for col in range(3):
            i = row * 3 + col
            symbol = board[i] if board[i] else "·"

            if cols[col].button(
                symbol,
                key=f"cell_{i}",
                use_container_width=True,
                disabled=(
                    bool(board[i]) or game_result is not None
                )
            ):
                board[i] = "X"

                st.session_state.history.append(
                    f"Human placed X in cell {i + 1}"
                )

                if winner(board) is None:
                    move, explanation, candidates = choose_move(
                        board[:], algorithm
                    )

                    st.session_state.explanation = explanation
                    st.session_state.candidates = candidates

                    if move is not None:
                        board[move] = "O"
                        st.session_state.last_move = move

                        st.session_state.history.append(
                            f"AI placed O in cell {move + 1}"
                        )

                st.rerun()

    game_result = winner(st.session_state.board)

    if game_result == "X":
        st.success("🏆 Human wins!")
    elif game_result == "O":
        st.success("🤖 AI wins!")
    elif game_result == "Draw":
        st.warning("🤝 Draw!")
    else:
        st.info("Your turn: choose any empty cell.")

    st.markdown("### 📊 Game Statistics")

    stat1, stat2 = st.columns(2)

    stat1.metric(
        "Moves played",
        sum(1 for cell in st.session_state.board if cell)
    )

    stat2.metric(
        "Empty cells",
        st.session_state.board.count("")
    )

with info_col:
    st.subheader("🧠 Algorithm Inspector")

    st.markdown(f"**Selected algorithm:** {algorithm}")
    st.write(ALGORITHMS[algorithm])

    st.markdown("---")
    st.markdown("### 🔍 Latest AI Decision")
    st.info(st.session_state.explanation)

    st.markdown("### 📈 Candidate Move Scores")

    candidates = st.session_state.candidates

    if candidates:
        for value, cell in sorted(candidates, reverse=True):
            st.write(f"Cell {cell + 1} — Heuristic: {value}")
    else:
        st.caption(
            "Make a move to display the AI's candidate scores."
        )

# ---------- MOVE HISTORY ----------
st.markdown("---")
st.subheader("📜 Move History")

if st.session_state.history:
    for number, move in enumerate(
        st.session_state.history, start=1
    ):
        st.write(f"**{number}.** {move}")
else:
    st.caption("Your moves and AI decisions will appear here.")

# ---------- TESTING GUIDE ----------
with st.expander("📘 How to test this prototype"):
    st.markdown("""
    1. Select **Greedy Best-First Search**.
    2. Play as X and observe the AI response.
    3. Reset and select a different search option.
    4. Load **Block X from winning** to inspect a defensive position.
    5. Load **Take a winning move** to inspect an immediate win.
    6. Compare the decision explanations and candidate scores.
    """)

st.caption(
    "Educational prototype. Greedy uses a one-step heuristic; "
    "the A*, AO*, and memory-bounded options are demonstrations, "
    "not complete implementations of those algorithms."
)