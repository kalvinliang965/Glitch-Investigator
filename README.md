# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### What the app does
This is a number guessing game built with Streamlit. The player guesses a secret number within a range determined by the selected difficulty. After each guess the game gives a hint — either "Go Higher" or "Go Lower" — until the player wins or runs out of attempts. Difficulty controls both the number range and the attempt limit: Easy (1–20, 6 attempts), Normal (1–100, 8 attempts), and Hard (1–200, 5 attempts).

### Bugs I found and how I fixed them

**1. Reversed hints**
The most noticeable bug was that hints were backwards — guessing too high told you to go higher, and guessing too low told you to go lower. Tracing through `check_guess` in `app.py`, the outcome labels (`"Too High"`, `"Too Low"`) were correct but the messages attached to them were swapped. I used AI to locate the exact lines, then fixed the messages so `"Too High"` directs the player lower and `"Too Low"` directs them higher. I followed a TDD approach: wrote a failing pytest first that asserted the message contained the correct direction word, then implemented the fix until the test passed.

**2. Hard difficulty range was easier than Normal**
`get_range_for_difficulty` returned `1–50` for Hard, which is a narrower range than Normal's `1–100` — making Hard easier to guess, not harder. I wrote tests asserting that each difficulty's range should be strictly wider than the one below it, confirmed they failed, then corrected Hard to use `1–200`.

**3. Game state not resetting on New Game**
Clicking "New Game" regenerated the secret but forgot to reset `status`, `attempts`, and `history`. Since `status` was left as `"won"` or `"lost"`, the game hit the status guard and called `st.stop()` immediately — the player could never actually start a new round. I refactored the reset logic into a `reset_game` function in `logic_utils.py` and wrote tests covering each field (`attempts`, `history`, `status`, `secret`), then wired it into the New Game button in `app.py`.

**4. Changing difficulty didn't reset the game**
When the player switched difficulty mid-game the secret stayed the same — potentially a number outside the new range — and the history and attempt count carried over. I added a `difficulty` field to session state and wrote a `reset_on_difficulty_change` function that compares the stored difficulty against the current selection on every rerun. If they differ it calls `reset_game` with the new range and updates the stored difficulty. Tests confirmed it resets all state fields on a change and does nothing when difficulty stays the same.

**5. Submit required two clicks to log a guess**
Typing a guess and clicking Submit on the first click would not log the value — only the second click worked. This is a Streamlit quirk: `st.text_input` only commits its value to session state when the field loses focus or Enter is pressed. Clicking a plain `st.button` directly does not trigger that commit, so on the first click `raw_guess` was still an empty string. The fix was to wrap the text input and submit button inside a `st.form` with `st.form_submit_button`, which batches both events into a single rerun so the value is always captured together with the button click.

### What I learned
Working through these bugs showed how important it is to separate pure logic from UI code. By refactoring functions like `check_guess`, `reset_game`, and `reset_on_difficulty_change` into `logic_utils.py`, I could write fast, isolated pytest tests for each behavior without needing to spin up a Streamlit session. The TDD cycle — write a failing test, implement the fix, confirm green — made it much easier to catch regressions and be confident each fix was complete.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
