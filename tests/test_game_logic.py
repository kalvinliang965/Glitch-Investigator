from logic_utils import check_guess, reset_game

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_returns_correct_hints():
    # When guess is too high, outcome should be "Too High" and message should direct player LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "lower" in message.lower(), f"Expected hint to say go lower, got: {message}"

    # When guess is too low, outcome should be "Too Low" and message should direct player HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "higher" in message.lower(), f"Expected hint to say go higher, got: {message}"

    # When guess is correct, outcome should be "Win"
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_reset_game_resets_attempts():
    # After reset, attempts should be back to 1
    state = {"attempts": 5, "secret": 42, "history": [10, 20], "status": "won"}
    new_state = reset_game(state, low=1, high=100)
    assert new_state["attempts"] == 1

def test_reset_game_clears_history():
    # After reset, history should be empty
    state = {"attempts": 3, "secret": 42, "history": [10, 20, 30], "status": "lost"}
    new_state = reset_game(state, low=1, high=100)
    assert new_state["history"] == []

def test_reset_game_resets_status():
    # After reset, status should be "playing"
    state = {"attempts": 3, "secret": 42, "history": [], "status": "won"}
    new_state = reset_game(state, low=1, high=100)
    assert new_state["status"] == "playing"

def test_reset_game_changes_secret():
    # After reset, secret should be a new number within the given range
    state = {"attempts": 3, "secret": 42, "history": [], "status": "lost"}
    new_state = reset_game(state, low=1, high=100)
    assert 1 <= new_state["secret"] <= 100

def test_reset_game_respects_difficulty_range():
    # Secret should be within the difficulty range, not always 1-100
    state = {"attempts": 3, "secret": 42, "history": [], "status": "lost"}
    new_state = reset_game(state, low=1, high=20)
    assert 1 <= new_state["secret"] <= 20
