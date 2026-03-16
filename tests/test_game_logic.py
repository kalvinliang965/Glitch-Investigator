from logic_utils import check_guess

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
