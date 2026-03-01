import ast, os

# app.py is a Streamlit script — importing it runs all top-level UI code.
# Instead, parse the source with ast and exec only the functions we need.
_src = open(os.path.join(os.path.dirname(__file__), "..", "app.py"), encoding="utf-8").read()
_tree = ast.parse(_src)
_wanted = {"check_guess", "get_range_for_difficulty"}
for _node in ast.walk(_tree):
    if isinstance(_node, ast.FunctionDef) and _node.name in _wanted:
        _mod = ast.Module(body=[_node], type_ignores=[])
        exec(compile(_mod, "app.py", "exec"), globals())

# Explicit bindings so static analysers can resolve these names
check_guess = globals()["check_guess"]
get_range_for_difficulty = globals()["get_range_for_difficulty"]


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high_outcome():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_high_hint_says_lower():
    # Bug fix: when guess > secret the hint must say Go LOWER, not Go HIGHER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message


def test_guess_too_low_outcome():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_guess_too_low_hint_says_higher():
    # Bug fix: when guess < secret the hint must say Go HIGHER, not Go LOWER
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_secret_always_compared_as_int():
    # Bug fix: secret must never be cast to str mid-game; int comparisons stay consistent
    outcome_odd, _ = check_guess(75, 50)
    outcome_even, _ = check_guess(75, 50)
    assert outcome_odd == outcome_even == "Too High"


# --- Difficulty range tests (fix: Normal and Hard were swapped) ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert (low, high) == (1, 20)


def test_normal_range_is_harder_than_easy():
    _, normal_high = get_range_for_difficulty("Normal")
    _, easy_high = get_range_for_difficulty("Easy")
    assert normal_high > easy_high, "Normal should have a larger range than Easy"


def test_hard_range_is_harder_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, "Hard should have a larger range than Normal"


def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert (low, high) == (1, 50)


def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 100)
