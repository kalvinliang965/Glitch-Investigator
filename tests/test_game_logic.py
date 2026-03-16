from logic_utils import check_guess, reset_game, get_range_for_difficulty, reset_on_difficulty_change

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


def test_easy_range_is_smaller_than_normal():
    # Easy should have a smaller range than Normal (easier to guess)
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    assert (easy_high - easy_low) < (normal_high - normal_low)

def test_hard_range_is_larger_than_normal():
    # Hard should have a larger range than Normal (harder to guess)
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    assert (hard_high - hard_low) > (normal_high - normal_low)

def test_unknown_difficulty_falls_back_to_normal():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1 and high == 100


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


def test_difficulty_change_resets_attempts():
    # Switching difficulty should reset attempts back to 1
    state = {"attempts": 5, "secret": 42, "history": [10, 20], "status": "playing", "difficulty": "Easy"}
    new_state = reset_on_difficulty_change(state, new_difficulty="Hard")
    assert new_state["attempts"] == 1

def test_difficulty_change_clears_history():
    # Switching difficulty should clear the guess history
    state = {"attempts": 3, "secret": 42, "history": [10, 20, 30], "status": "playing", "difficulty": "Easy"}
    new_state = reset_on_difficulty_change(state, new_difficulty="Hard")
    assert new_state["history"] == []

def test_difficulty_change_resets_status():
    # Switching difficulty should reset status to "playing"
    state = {"attempts": 3, "secret": 42, "history": [], "status": "won", "difficulty": "Normal"}
    new_state = reset_on_difficulty_change(state, new_difficulty="Easy")
    assert new_state["status"] == "playing"

def test_difficulty_change_generates_secret_in_new_range():
    # Secret should be within the new difficulty's range after switching
    state = {"attempts": 3, "secret": 99, "history": [], "status": "playing", "difficulty": "Normal"}
    new_state = reset_on_difficulty_change(state, new_difficulty="Easy")
    low, high = get_range_for_difficulty("Easy")
    assert low <= new_state["secret"] <= high

def test_same_difficulty_does_not_reset():
    # If difficulty hasn't changed, the state should be returned unchanged
    state = {"attempts": 3, "secret": 42, "history": [10, 20], "status": "playing", "difficulty": "Normal"}
    new_state = reset_on_difficulty_change(state, new_difficulty="Normal")
    assert new_state["attempts"] == 3
    assert new_state["history"] == [10, 20]
    assert new_state["secret"] == 42
